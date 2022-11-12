#viết code hiển thị hình anh,Chuyển đổi sang thang độ xám,làm mờ hinhf ảnh,Phát hiện cạnh
#giải thíc code.
import cv2

# đọc hình ảnh
image = cv2.imread('images.jpg')
#Chuyển đổi sang thang độ xám
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#làm mờ hinhf ảnh
blurred_image = cv2.GaussianBlur(image, (7,7), 0)
#Phát hiện cạnh
canny = cv2.Canny(blurred_image, 10, 30)

# Hiển thị cả 3 hình ảnh
cv2.imshow("Original Image", image)
cv2.imshow("Gray Image", gray_image)
cv2.imshow("Blurred Image", blurred_image)

cv2.imshow("Canny with low thresholds", canny)
cv2.waitKey(0)
