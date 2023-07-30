import cv2
import numpy as np

img = np.zeros((512,512,3))

flags = False
ix = -1
iy = -1

def draw(event,x,y,flag,params):

    global flags,ix,iy

    if event == 1:
        flags = True
        ix = x
        iy = y

    elif event == 0:
        if flags == True:
            cv2.rectangle(img, pt1=(ix, iy), pt2=(x, y), color=(0, 255, 0), thickness=-1)


    elif event == 4:
        flags = False
        cv2.rectangle(img, pt1=(ix, iy), pt2=(x, y), color=(0, 255, 0), thickness=-1)


cv2.namedWindow(winname="window")
cv2.setMouseCallback("window",draw)

while True:
    cv2.imshow("window",img)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cv2.destroyAllWindows()