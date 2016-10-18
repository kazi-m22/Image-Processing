import cv2
import numpy as np

img = cv2.imread('messi.jpg')

ret, thresh = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)
ret2, thresh2 = cv2.adaptiveThreshold(thresh, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,115, 1)

cv2.imshow('thresh', thresh)
cv2.imshow('thresh2', thresh2)
cv2.waitKey(0)
cv2.destroyAllWindows()
