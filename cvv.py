
import cv2
import numpy as np


def show_webcam(mirror=False):
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
    cv2.destroyAllWindows()


def main():
    show_webcam(mirror=True)


if __name__ == '__main__':
    main()

