import cv2

def diff_img(prev, curr, nxt):
  i = cv2.absdiff(curr, prev)
  j = cv2.absdiff(nxt, curr)
  return cv2.bitwise_and(j, i)

cam = cv2.VideoCapture(0)

w = "Example 3"
cv2.namedWindow(w, cv2.CV_WINDOW_AUTOSIZE)

prev_img = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
curr_img = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
next_img = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)

while True:
    cv2.imshow(w, diff_img(prev_img, curr_img, next_img))

    prev_img = curr_img
    curr_img = next_img
    next_img = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)

    # If you don't have this, the window
    # won't show.
    key = cv2.waitKey(10)
    if key == 27:
        cv2.destroyWindow(w)
        break
