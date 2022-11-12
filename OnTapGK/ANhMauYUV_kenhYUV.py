import cv2  #khai báo thư viện
image = cv2.imread(r"images.jpg")
yuv_img = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
cv2.imshow('Y channel', yuv_img[:, :, 0])
cv2.imshow('U channel', yuv_img[:, :, 1])
cv2.imshow('V channel', yuv_img[:, :, 2])
cv2.waitKey()