# tải và hiển thị hình ảnh bằng Matplotlib
from matplotlib import image
from matplotlib import pyplot
# tải hình ảnh dưới dạng mảng pixel
image = image.imread('images.jpg')
# tóm tắt hình dạng của mảng pixel
print(image.dtype)
print(image.shape)
# hiển thị mảng pixel dưới dạng hình ảnh
pyplot.imshow(image)
pyplot.show()