import cv2
import numpy as np 

#read the image
img = cv2.imread('1.jpg',1)

while(1):
    # covert the image to HSV format
    hsv =  cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    #set the limit of the color of which you want to detect in HSV format
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])  

    lower_green = np.array([40, 100,100],np.uint8)
    upper_green = np.array([60, 255, 255],np.uint8)

    #creating seperate mask for 2 colors(green,blue)
    mask1 = cv2.inRange(hsv,lower_blue,upper_blue)
    mask2 = cv2.inRange(hsv,lower_green,upper_green)

    #combining 2 masks into 1 mask so that we can apply it to the final image
    mask = cv2.bitwise_or(mask1,mask2)

    #masking the image so that we can get the final result
    res = cv2.bitwise_and(img,img, mask= mask)
    #displaying the result
    cv2.imshow('frame',img)
    cv2.imshow('mask',mask)
    cv2.imshow('result',res)
    k = cv2.waitKey(0) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()