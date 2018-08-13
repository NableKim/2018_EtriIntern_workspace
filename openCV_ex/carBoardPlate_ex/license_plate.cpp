#include <opencv2/opencv.hpp>
#include <iostream>
#include <cstdlib>  // for abs()
#include <vector>

using namespace cv;
using namespace std;

int main()
{
    Mat image, image2, image3, drawing; // matrix for image
    Rect rect, temp_rect;
    vector<vector<Point>> contours; // Vectors for 'findContours' function
    vector<Vec4i> hierarchy;

    double ratio, delta_x, delta_y, gradient;
    int select, plate_width, count, friend_count = 0, refinery_count = 0;

    image = imread("/home/pi/kss/openCV_ex/car_image.jpg"); // Load ad image file
    image3 = imread("/home/pi/kss/openCV_ex/car_image.jpg"); // Load ad image file

    imshow("Original", image);
    waitKey(0);

    //---  Pre-process ---
    // conver to gray image
    cvtColor(image, image2, CV_BGR2GRAY);
    imshow("Original->Gray", image2);
    waitKey(0);

    // Getting edges by Canny algorithm
    Canny(image2, image2, 100, 300, 3);
    imshow("Original->Gray->Canny", image2);
    waitKey(0);

    drawing = Mat::zeros(image.rows, image.cols, CV_8UC3);

    //--- Getting contours ---
    // Finding contours
    /*
     * void findContours()
     * function : finds contours in a binary image
     * parameter :
     *  InputOutputArray image : Source Image 
     *  OutputArrayOfArrays contours : Detected contours
     *  OutputArray hierarchy : Optional output vector containing information about the image topology
     *  int mode : Contour retrieval mode
     *  int method : Contour approximation method
     *  Point offset=Point() : 
     * */
    findContours(image2, contours, hierarchy, CV_RETR_TREE, CV_CHAIN_APPROX_SIMPLE, Point());
    vector<vector<Point>> contours_poly(contours.size());
    vector<Rect> boundRect(contours.size());
    vector<Rect> boundRect2(contours.size());

    // Bind rectangle to every contours
    for(int i=0; i<contours.size(); i++) {
        approxPolyDP(Mat(contours[i]), contours_poly[i], 1, true);
        boundRect[i] = boundingRect(Mat(contours_poly[i]));
    }

    cout << "boundRect Size : " << boundRect.size() << endl;
    
    // Filtering recognized rectangles
    for(int i=0; i<contours.size(); i++) {
        ratio = (double) boundRect[i].height / boundRect[i].width;

        // Filtering rectangles height/width ratio and size
        if((ratio <= 2.5) && (ratio >= 0.5) && (boundRect[i].area() <= 800) && (boundRect[i].area() >= 400)) {
            /*
             * void drawContours() 
             * function : Draw contours outlines or filled contours
             * paramaters :
             *  InputOutputArray image : Destination image 
             *  InputOutputOfArrays contours : All the input contours
             *  int contourldx : Parameter indicating a contour
             *  const Scalar& color : Color
             *  int thickness=1 :
             *  int lineType=8 : 
             *  InputArray hierarchy=noArray() : 
             *  int maxLevel=INT_MAX : Maximal level for drawn contours
             *  Point offset=Point() : 
             * */
            drawContours(drawing, contours, i, Scalar(0, 255, 255), 1, 8, hierarchy, 1, Point());
            rectangle(drawing, boundRect[i].tl(), boundRect[i].br(), Scalar(255, 0 ,0), 1, 8, 0);
            rectangle(image3, boundRect[i].tl(), boundRect[i].br(), Scalar(0, 255, 0), 1, 8, 0);

            // Include only suitable rectangles
            //refinery_count += 1;
            boundRect2[refinery_count++] = boundRect[i];
        }            
    }

    boundRect2.resize(refinery_count); // Resize refinery rectangle array
    cout << "boundRect2 Size : " << boundRect2.size() << endl;

    imshow("Original->Gray->Canny->Contours&Rectangles", drawing);
    waitKey(0);

    //--- Get only car number plate area ---
    // Bubble sort in accordance with X-coordinate
    for(int i=0; i<boundRect2.size()-1; i++) {
        for(int j=0; j<(boundRect2.size()-i-1); j++) {
            if(boundRect2[j].tl().x > boundRect2[j+1].tl().x) {
                temp_rect = boundRect2[j];
                boundRect2[j]=boundRect2[j+1];
                boundRect2[j+1]=temp_rect;    
            }
        }
    }

    // Snake moves to right, for eating his friend.
    for(int i=0; i<boundRect2.size(); i++) {
        count = 0;
        for(int j=i+1; j<boundRect2.size(); j++) {
            // x_distance between two points
            delta_x = abs(boundRect2[j].tl().x - boundRect2[i].tl().x);
            if(delta_x > 200)
                break;

            // y_distance between two points
            delta_y = abs(boundRect2[j].tl().y - boundRect2[i].tl().y);

            if(delta_x == 0)
                delta_x = 1;
            if(delta_y == 0)
                delta_y = 1;

            // Get gradient
            gradient = delta_y / delta_x;
            cout << "gradient : " << gradient << endl;
            
            if(gradient < 0.25)
                count += 1;
        }
       
        // find a rectangle with max count
        if(count > friend_count) {
            select = i; // Save most full snake number
            friend_count = count; // Renewal number of friends hunting
            rectangle(image3, boundRect2[select].tl(), boundRect2[select].br(), Scalar(255, 0, 0), 1, 8, 0);
            plate_width = delta_x;
        }
    }

    rectangle(image3, boundRect2[select].tl(), boundRect2[select].br(), Scalar(0, 0, 255), 2, 8, 0);
    line(image3, boundRect2[select].tl(), Point(boundRect2[select].tl().x+plate_width, boundRect2[select].tl().y), Scalar(0, 0, 255), 1, 8, 0);

    imshow("Rectangles on original", image3);
    waitKey(0);

    // Shows license plate and save image file
    imshow("Region of interest", image(Rect(boundRect2[select].tl().x-20, boundRect2[select].tl().y-20, plate_width+60, plate_width*0.3)));
    waitKey(0);

    imwrite("/home/pi/kss/openCV_ex/car_plate_image.jpg", image(Rect(boundRect2[select].tl().x-20, boundRect2[select].tl().y-20, plate_width+60, plate_width*0.3)));

    exit(0);
    //return 0;
}
