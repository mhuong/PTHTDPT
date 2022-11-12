import cv2

# đọc hình ảnh
image = cv2.imread('images.jpg')
#Chuyển đổi sang thang độ xám
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#làm mờ hinhf ảnh
blurred_image = cv2.GaussianBlur(image, (7,7), 0)

canny = cv2.Canny(blurred_image, 30, 100)

# Hiển thị cả 3 hình ảnh
cv2.imshow("Original Image", image)
cv2.imshow("Gray Image", gray_image)
cv2.imshow("Blurred Image", blurred_image)

cv2.imshow("Canny with low thresholds", canny)

#Giá trị trả về của đường bao là một danh sách đơn giản chứa số đường bao được tìm thấy.
# Lấy chiều dài của nó sẽ cho chúng ta số lượng đồ vật được tìm thấy.
contours, hierarchy= cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("Number of objects found = ", len(contours))
cv2.drawContours(image, contours, -1, (0,255,0), 2)
cv2.imshow("objects Found", image)
cv2.waitKey(0)


