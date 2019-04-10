import numpy as np 
import cv2

global brush
drawing = False
ix,iy = -1,-1

def nothing(x):
    pass

def size(x):
    brush = x

def draw_circle(event,x,y,flag,param):
    global drawing,ix,iy
    if event == cv2.EVENT_FLAG_LBUTTON:
        drawing = True
        ix,iy = x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing==True:
            cv2.circle(image,(x,y),brush,(R,G,B),-1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.circle(image,(x,y),brush,(R,G,B),-1)
        

image = np.zeros((512,512,3),np.uint8)
cv2.namedWindow('fr')
cv2.createTrackbar('R','fr',0,255,nothing)
cv2.createTrackbar('G','fr',0,255,nothing)
cv2.createTrackbar('B','fr',0,255,nothing)
cv2.createTrackbar('S','fr',0,1,nothing)
cv2.createTrackbar('brushsize','fr',0,100,size)
cv2.setMouseCallback('fr',draw_circle)

while(1):
    cv2.imshow('fr',image)
    k = cv2.waitKey(1) & 0xFF
    S = cv2.getTrackbarPos('S','fr')
    if k == 27:
        break
    if S == 0:
        image[:] = 0
    else:
        R = cv2.getTrackbarPos('R','fr')
        G = cv2.getTrackbarPos('G','fr')
        B = cv2.getTrackbarPos('B','fr')
        brush = cv2.getTrackbarPos('brushsize','fr')
    

cv2.destroyAllWindows()