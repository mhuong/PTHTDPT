import cv2  #cài thư viện cv2

image = cv2.imread(r'images.jpg ') # Đọc hình ảnh

height, width = image.shape[:2] # chia chiều cao và chiều rộng cho 2 để lấy tâm của hình ảnh
center = (width/2, height/2) # lấy tọa độ tâm của hình ảnh để tạo ma trận xoay 2D

rotate_matrix = cv2.getRotationMatrix2D(center=center, angle=45, scale=1) # using cv2.getRotationMatrix2D () để lấy ma trận xoay

rotated_image = cv2.warpAffine(src=image, M=rotate_matrix, dsize=(width, height)) # xoay hình ảnh bằng cv2.warpAffine

cv2.imshow('Original image', image)
cv2.imshow('Rotated image', rotated_image) # đợi vô thời hạn, nhấn bất kỳ phím nào trên bàn phím để thoát
cv2.waitKey(0)
cv2.imwrite('rotated_image.jpg', rotated_image) # lưu hình ảnh đã xoay vào đĩa