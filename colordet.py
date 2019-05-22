
from collections import OrderedDict

import numpy as np
from scipy.spatial import distance as dist

import cv2


class colDet:
    def __init__(self):
        clrs = OrderedDict({
            "red": (255, 0, 0),
            "Black": (0, 0, 0),
            "White": (255, 255, 255),
            "green": (0, 255, 0),
            "blue": (0, 0, 255)})
        self.lab = np.zeros((len(clrs), 1, 3), dtype="uint8")
        self.clrNms = []
        for (i, (name, rgb)) in enumerate(clrs.items()):
            self.lab[i] = rgb
            self.clrNms.append(name)
        self.lab = cv2.cvtColor(self.lab, cv2.COLOR_RGB2LAB)

    def nm(self, img, c):
        mask = np.zeros(img.shape[:2], dtype="uint8")
        cv2.drawContours(mask, [c], -1, 255, -1)
        mask = cv2.erode(mask, None, iterations=2)
        mean = cv2.mean(img, mask=mask)[:3]
        minDist = (np.inf, None)
        for (i, row) in enumerate(self.lab):
            d = dist.euclidean(row[0], mean)
            if d < minDist[0]:
                minDist = (d, i)
        return self.clrNms[minDist[1]]
