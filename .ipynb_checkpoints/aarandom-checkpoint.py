import sys
import os
import cv2 as cv
import numpy as np


def main(argv):
    ## [load]
    # default_file = 'aeval2.bmp'
    # filename = argv[0] if len(argv) > 0 else default_file
#     filename='philipl3.bmp'
    filename='coins.jpg'

    # Loads an image
    src = cv.imread(os.path.join('Images',filename))

    # Check if image is loaded fine
    if src is None:
        print ('Error opening image!')
        print ('Usage: hough_circle.py [image_name -- default ' + filename + '] \n')
        return -1
    ## [load]

    ## [convert_to_gray]
    # Convert it to gray
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    ## [convert_to_gray]

    ## [reduce_noise]
    # Reduce the noise to avoid false circle detection
    gray = cv.medianBlur(gray, 5)
    ## [reduce_noise]

    ## [houghcircles]
    rows = gray.shape[0]
    circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, rows / 8,
                               param1=100, param2=30,
                               minRadius=1, maxRadius=30)
    ## [houghcircles]

    ## [draw]
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            center = (i[0], i[1])
            # circle center
            cv.circle(src, center, 1, (0, 100, 100), 3)
            # circle outline
            radius = i[2]
            cv.circle(src, center, radius, (255, 0, 255), 3)
    ## [draw]

    ## [display]
    cv.imshow("detected circles", src)
    while 1:
        if cv.waitKey(1) == ord('q'):
            break
# # When everything done, release the capture
#     cap.release()
    cv.destroyAllWindows()
    # I don't know why we need these 4 lines but it works
    cv.waitKey(1)
    cv.waitKey(1)
    cv.waitKey(1)
    cv.waitKey(1)
    return 0


if __name__ == "__main__":
    main(sys.argv[1:])