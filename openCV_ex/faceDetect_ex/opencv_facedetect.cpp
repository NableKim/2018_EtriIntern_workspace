#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <linux/fb.h>
#include <unistd.h>
#include <sys/mman.h>
#include <sys/ioctl.h>

#include <opencv2/core/core.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/objdetect/objdetect.hpp>

#define FBDEV   "/dev/fb0"
#define CAMERA_COUNT    1
#define CAM_WIDTH   640
#define CAM_HEIGHT 480

using namespace cv;

const static char* cascade_name = "/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml";

int main(int argc, char** argv)
{
    int fbfd;   // File descriptor for frame buffer
    struct fb_var_screeninfo vinfo; // Struct for frame buffer info
    struct fb_fix_screeninfo finfo; // ?

    unsigned char *buffer, r, g, b;
    unsigned int x, y, t, i, j, screensize;
    unsigned short *pfbmap, *pOutdata, pixel;   
    CvCapture* capture; // Variable for camera
    CascadeClassifier cascade;  // Classifier for face detect
    IplImage *frame;    // Variable for image
    CvPoint pt1, pt2;   // Variable for two points of retrieved face

    // Call cascade for face detect
    if(!cascade.load(cascade_name)) {
        perror("load()");
        return -1;
    }

    // Set a camera you gonna use
    capture = cvCaptureFromCAM(0);
    if(capture == 0) {
        perror("OpenCV : open WebCam\n");
        return -1;
    }

    // Set capture property
    cvSetCaptureProperty(capture, CV_CAP_PROP_FRAME_WIDTH, CAM_WIDTH);
    cvSetCaptureProperty(capture, CV_CAP_PROP_FRAME_HEIGHT, CAM_HEIGHT);

    // Open frame buffer
    fbfd = open(FBDEV, O_RDWR);
    if(fbfd == -1) {
        perror("open() : framebuffer device");
        return EXIT_FAILURE;
    }

    // Get info about FB
    if(ioctl(fbfd, FBIOGET_VSCREENINFO, &vinfo) == -1) {
        perror("Error reading variable information.");
        exit(EXIT_FAILURE);
    }

    // Get memory space for FB
    screensize = vinfo.xres * vinfo.yres * 2;
    pfbmap = (unsigned short *)mmap(NULL, screensize, PROT_READ | PROT_WRITE, MAP_SHARED, fbfd, 0);

    if((int)pfbmap == -1) {
        perror("mmap() : framebuffer device to memory");
        return EXIT_FAILURE;
    }
    memset(pfbmap, 0 , screensize);

    // Get memory space for image being printed
    pOutdata = (unsigned short*)malloc(screensize);
    memset(pOutdata, 0, screensize);

    for(i=t=b=g=r=0; i<CAMERA_COUNT; i++) {
        cvGrabFrame(capture);   // get one photo from camera
        frame = cvRetrieveFrame(capture);   // get image data from photo
   
        // copy image for camera capture with other name
        Mat image;
        cvtColor(Mat(frame), image, CV_BGR2GRAY);   // Changed into gray color values to detect face
        equalizeHist(image, image); // to raise face perception rate

        // detect face in a photo
        std::vector<Rect> faces;
        cascade.detectMultiScale(image, faces, 1.1, 2, 0|CV_HAAR_SCALE_IMAGE, Size(30, 30));

        for(j=0; j<faces.size(); j++) {
            // get edge points of face frame
            pt1.x = faces[j].x;
            pt1.y = faces[j].y;

            pt2.x = (faces[j].x + faces[j].width);
            pt2.y = (faces[j].y + faces[j].height);

            // draw rectangle on a image frame
            cvRectangle(frame, pt1, pt2, CV_RGB(255, 0, 0), 3, 8, 0);
        }

        // Get imgdata from IPLimage class
        buffer = (uchar*)frame->imageData;

        
        for(x=0; x<frame->height; x++) {
            t = x * frame->width;
            for(y=0; y<frame->width; y++) {
                r = *(buffer + (t+y)*3 + 2);
                g = *(buffer + (t+y)*3 + 1);
                b = *(buffer + (t+y)*3 + 0);
                pixel = ((r>>3)<<11)|((g>>2)<<5)|(b>>3);

                pOutdata[y+t+(vinfo.xres-frame->width)*x]=pixel;
            }
        }
        memcpy(pfbmap, pOutdata, screensize);
    };

    // free memory resource
    munmap(pfbmap, screensize);
    free(pOutdata);

    close(fbfd);
    return 0;
}

