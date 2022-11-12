import cv2
image = cv2.imread(r"images.jpg")
(h, w, d) = image.shape
print("width={}, height={}, depth={}".format(w, h, d))