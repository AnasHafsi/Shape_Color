import imutils

import cv2
from shapedetect import shapeDet
from colordet import colDet


def imm(rr):
    cv2.imshow('image', rr)


cam = cv2.VideoCapture(0)
while True:
    ret_val, img = cam.read()
    cv2.imshow('cmx0bFF', img)
    key = cv2.waitKey(1)
    if key == 97:
        print("NK")
    elif key == 27:
        break  # esc to quit
    elif key == 98:
        cv2.imwrite("Test.jpg", img)
        print(img)
    resized = imutils.resize(img, width=300)
    ratio = img.shape[0] / float(resized.shape[0])

    blurred = cv2.GaussianBlur(resized, (5, 5), 0)
    gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
    cl = cv2.cvtColor(blurred, cv2.COLOR_BGR2LAB)
    thresh = cv2.threshold(gray, 60, 255, cv2.THRESH_BINARY)[1]
    imm(thresh)
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    sd = shapeDet()
    cd = colDet()

    for c in cnts:
        M = cv2.moments(c)
        cX = int((M["m10"] / M["m00"]) * ratio)
        cY = int((M["m01"] / M["m00"]) * ratio)
        shape = sd.detect(c)
        color = cd.nm(cl, c)
        txt = "{} {}".format(color, shape)
        c = c.astype("float")
        c *= ratio
        c = c.astype("int")
        cv2.drawContours(img, [c], -1, (100, 0, 255), 2)
        cv2.putText(img, txt, (cX, cY),
                    cv2.FONT_HERSHEY_DUPLEX, 0.5, (200, 200, 200), 2)
    imm(img)
cv2.destroyAllWindows()
