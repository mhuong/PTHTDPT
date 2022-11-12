from PIL import Image
from numpy import asarray
# tải hình ảnh
image = Image.open('images.jpg')
# chuyển đổi hình ảnh sang mảng numpy
data = asarray(image)
print(type(data))
# tóm tắt hình dạng
print(data.shape)

# tạo hình ảnh Gối
image2 = Image.fromarray(data)
print(type(image2))

#tóm tắt chi tiết hình ảnh
print(image2.mode)
print(image2.size)