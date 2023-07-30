import cv2
import numpy as np

img = np.zeros((512,512,3))

def draw(event,x,y,flag,params):
    if event == 1:
        cv2.circle(img,center=(x,y),radius=10, color=(0,0,255),thickness=-1)

cv2.namedWindow(winname="window")
cv2.setMouseCallback("window",draw)



while True:

    cv2.imshow("window",img)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cv2.destroyAllWindows()



