# tải và hiển thị hình ảnh với Pillow
from PIL import Image
# Mở thư mục làm việc của biểu mẫu hình ảnh
image = Image.open('images.jpg')
# tóm tắt một số chi tiết về hình ảnh
print(image.format)
print(image.size)
print(image.mode)
# hiển thị hình ảnh
image.show()