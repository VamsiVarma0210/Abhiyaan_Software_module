import cv2  
import numpy as np

# Storing original image and coverting to hsv
org_image = cv2.imread("abhiyaan_opencv_qn1.png")
hsv_original = cv2.cvtColor(org_image, cv2.COLOR_BGR2HSV)

# Storing the cropped image and converting to hsv
roi = cv2.imread("cone1.png")
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)


roi_hist = cv2.calcHist([hsv_roi], [0, 1], None, [180, 256], [0, 180, 0, 256])
mask = cv2.calcBackProject([hsv_original], [0, 1], roi_hist, [0, 180, 0, 256], 1)

# Filtering the noises
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
dst = cv2.filter2D(mask, -1, kernel)
ret, dst = cv2.threshold(dst, 100, 255, cv2.THRESH_BINARY)

# Drawing boxes on original image by taking contours in threshold image
contours, _ = cv2.findContours(dst, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
for c in contours:
    rect = cv2.boundingRect(c)
    x,y,w,h = rect
    cv2.rectangle(org_image,(x,y),(x+w,y+h),(0,255,0),2)

# Display original image with boxes
cv2.imshow("obj_detect",org_image)


cv2.waitKey(100000)  
