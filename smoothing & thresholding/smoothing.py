import numpy as np
import cv2

def nothing(*arg):
    pass
cv2.namedWindow('thresh')
cap = cv2.VideoCapture(0)
cv2.createTrackbar('RU', 'thresh', 0, 255, nothing)
cv2.createTrackbar('GU', 'thresh', 0, 255, nothing)
cv2.createTrackbar('BU', 'thresh', 0, 255, nothing)
cv2.createTrackbar('RL', 'thresh', 0, 255, nothing)
cv2.createTrackbar('GL', 'thresh', 0, 255, nothing)
cv2.createTrackbar('BL', 'thresh', 0, 255, nothing)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    GU = cv2.getTrackbarPos('GU', 'thresh')
    RU = cv2.getTrackbarPos('RU', 'thresh')
    BU = cv2.getTrackbarPos('BU', 'thresh')
    RL = cv2.getTrackbarPos('RL', 'thresh')
    GL = cv2.getTrackbarPos('GL', 'thresh')
    BL = cv2.getTrackbarPos('RL', 'thresh')


    upper = np.array([RU, GU, BU])
    lower = np.array([RL, GL, BL])

    mask = cv2.inRange(hsv, lower, upper)

    res = cv2.bitwise_and(frame, frame, mask = mask)

    
    kernel = np.ones((15,15), np.float32)/255
    smoothed = cv2.filter2D(res, -1, kernel)


    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    cv2.imshow('smoothed', smoothed)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
cap.release()
