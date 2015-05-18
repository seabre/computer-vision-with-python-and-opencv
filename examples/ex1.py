import cv2

cam = cv2.VideoCapture(0)

w = "Example 1"
cv2.namedWindow(w, cv2.CV_WINDOW_AUTOSIZE)

while True:
    cv2.imshow(w, cam.read()[1])

    # If you don't have this, the window
    # won't show.
    key = cv2.waitKey(10)
    if key == 27:
        cv2.destroyWindow(w)
        break
