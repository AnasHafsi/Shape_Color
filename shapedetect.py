import cv2


class shapeDet:
	def __init__(self):
        # init Pass on self
		pass

	def detect(self,cont):
		# init sh & apx contour
		shape = "undef"
		peri = cv2.arcLength(cont, True)
		approx = cv2.approxPolyDP(cont, 0.02 * peri, True)
		print(len(approx))
		if len(approx) == 3:
			shape = "triangle"
		elif len(approx) == 4:
			(x, y, w, h) = cv2.boundingRect(approx)
			ar = float(w) / float(h)
			shape = "square" if ar >= 0.95 and ar <= 1.05 else "rectangle"
		elif len(approx) == 5:
			shape = "Moul 5"
		else:
			shape = "Circle I Guess"
        #Salina
		extract="{} at {}".format(shape,approx)
		print(extract)
		return shape
