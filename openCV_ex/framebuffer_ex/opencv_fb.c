#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <linux/fb.h>
#include <sys/mman.h>
#include <sys/ioctl.h>

#include <opencv2/core/core_c.h>
#include <opencv2/imgproc/imgproc_c.h>
#include <opencv2/highgui/highgui_c.h>

#define FBDEV "/dev/fb0"
#define CAMERA_COUNT 100
#define CAM_WIDTH 640
#define CAM_HEIGHT 480

int main(int argc, char** argv)
{
	int fbfd;
	struct fb_var_screeninfo vinfo;	// a struct for storing FB info
	//struct fb_fix_screnninfo finfo;

	unsigned char *buffer, r, g, b;
	unsigned int x, y, t, i, screensize;
	unsigned short *pfbmap, *pOutdata, pixel;	// FB buffer, rgb Data
	CvCapture* capture;	// Camera Variable

	IplImage *frame;	// Image Variable

	capture = cvCaptureFromCAM(0);	// Set a camera you gonna use
	if(capture == 0) {
		perror("OpenCV : open WebCam\n");
		return -1;
	}

	// Set capture property
	cvSetCaptureProperty(capture, CV_CAP_PROP_FRAME_WIDTH, CAM_WIDTH);
	cvSetCaptureProperty(capture, CV_CAP_PROP_FRAME_HEIGHT, CAM_HEIGHT);	

	// Open FB
	fbfd = open(FBDEV, O_RDWR);
	if(fbfd == -1) {
		perror("open() : framebuffer device");
		return EXIT_FAILURE;
	}

	// Get FB info
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
	memset(pfbmap, 0, screensize);

	// Change an image to pixel values and copy them to memory space for FB 
	pOutdata = (unsigned short*)malloc(screensize);
	memset(pOutdata, 0, screensize);
	for(i=t=b=g=r=0; i<CAMERA_COUNT; i++) {
		cvGrabFrame(capture); // Get an image from camera
		frame = cvRetrieveFrame(capture);
		buffer = (uchar*)frame->imageData;

		for(x=0; x<frame->height; x++) {
			t=x*frame->width;
			for(y=0; y<frame->width; y++) {
				r = *(buffer + (t+y)*3 + 2);
				g = *(buffer + (t+y)*3 + 1);
				b = *(buffer + (t+y)*3 + 0);
				pixel = ((r>>3)<<11)|((g>>2)<<5)|(b>>3);
				pOutdata[y+t+(vinfo.xres-frame->width)*x]=pixel;
			}
		}

		memcpy(pfbmap, pOutdata, screensize);
	}

	// free memory
	munmap(pfbmap, frame->width*frame->height*2);
	free(pOutdata);

	close(fbfd);
	return 0;
}
