from cv2 import cv2
import numpy as np

img=cv2.imread("")
imgResize=cv2.resize(img,(1536,864))

imgBlur=cv2.pyrDown(imgResize)
num_iter = 5
for _ in range(num_iter):
    imgBlur= cv2.bilateralFilter(imgBlur, d=9, sigmaColor=9, sigmaSpace=7)
imgRGB=cv2.pyrUp(imgBlur)

imgGray=cv2.cvtColor(imgRGB,cv2.COLOR_RGB2GRAY)
imgBLUR=cv2.medianBlur(imgGray,7)

imgEdge=cv2.adaptiveThreshold(imgBLUR,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,9,2)
imgEdge = img2 = cv2.merge((imgEdge,imgEdge,imgEdge))
print(imgRGB.shape)
print(imgEdge.shape)
array=cv2.bitwise_and(imgRGB,imgEdge)
cv2.imshow('Image',array) 
cv2.imwrite("CartoonTower.jpg",array)
cv2.waitKey(0)