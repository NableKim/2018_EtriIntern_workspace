#include <stdio.h>
#include <opencv2/core/core_c.h>
#include <opencv2/imgproc/imgproc_c.h>
#include <opencv2/highgui/highgui_c.h>

int main(int argc, char** argv) {
	IplImage *image1 = cvLoadImage("sample1.jpg", CV_LOAD_IMAGE_COLOR);
	IplImage *image2 = cvLoadImage("sample2.jpg", CV_LOAD_IMAGE_COLOR);
	IplImage *image_add = cvCreateImage(cvGetSize(image1), IPL_DEPTH_8U, 3);
	//IPIamge *image_sub = cvCreateImage(cvGetSize(image1), IPL_DEPTH_8U, 3);
	//IPIamge *image_mul = cvCreateImage(cvGetSize(image1), IPL_DEPTH_8U, 3);
	//IPIamge *image_div = cvCreateImage(cvGetSize(image1), IPL_DEPTH_8U, 3);
	//IPIamge *image_gray1 = cvCreateImage(cvGetSize(image1), IPL_DEPTH_8U, 1);
	//IPIamge *image_gray2 = cvCreateImage(cvGetSize(image1), IPL_DEPTH_8U, 1);
	//IPIamge *image_white = cvCreateImage(cvGetSize(image1), IPL_DEPTH_8U, 1);
	//IPIamge *image_gray_sub = cvCreateImage(cvGetSize(image1), IPL_DEPTH_8U, 1);

	// Create Window
	cvNamedWindow("IMAGE_1", CV_WINDOW_AUTOSIZE);
	cvNamedWindow("IMAGE_2", CV_WINDOW_AUTOSIZE);
	cvNamedWindow("IMAGE_ADDITION", CV_WINDOW_AUTOSIZE);

	// Process source
	cvAdd(image1, image2, image_add, NULL);

	// Show result
	cvShowImage("IMAGE_1", image1);
	cvShowImage("IMAGE_2", image2);
	cvShowImage("IMAGE_ADDITION", image_add);

	// wait for key input
	cvWaitKey(0);

	// free resource
	cvReleaseImage(&image1);
	cvReleaseImage(&image2);
	cvReleaseImage(&image_add);

	// delete all windows
	cvDestroyAllWindows();

	return 0;
}
