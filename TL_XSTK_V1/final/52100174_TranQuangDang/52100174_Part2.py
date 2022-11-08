import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
# Histogram
try:
  img=np.array(Image.open('mo1.jpg').convert('L'))
except:
  print("Unable to load image")
  exit()
# img=np.array([[4,4,4,4,4],[3,4,5,4,3],[3,5,5,5,3],[3,4,5,4,3],[4,4,4,4,4]])

# Tính số lượng pixel của ảnh
def pixel_count(img):
  return img.shape[0]*img.shape[1]
# highest gray value
def highest_gray_value(img):
  highest_gray_value=0
  for i in range(img.shape[0]):
    for j in range(img.shape[1]):
      if img[i][j]>highest_gray_value:
        highest_gray_value=img[i][j]
  return highest_gray_value
# find minimum bits
def find_minimum_bits(img):
  return len(bin(highest_gray_value(img)))-2
# find max gray level by bits
bits=find_minimum_bits(img)
def max_gray_level_by_bits(bits):
  return 2**bits-1
# tạo từ điển để lưu trữ tần suất của từng giá trị pixel
def pixel_frequency(img):
  pixel_frequency={}
  for i in range(img.shape[0]):
    for j in range(img.shape[1]):
      if img[i][j] in pixel_frequency:
        pixel_frequency[img[i][j]]+=1
      else:
        pixel_frequency[img[i][j]]=1
  return pixel_frequency

# thêm giá trị key không có trong từ điển
def add_key_to_dict(pixel_frequency_dict):
  max_pixel_value=max_gray_level_by_bits(bits)
  for i in range(max_pixel_value+1):
    if i not in pixel_frequency_dict:
      pixel_frequency_dict[i]=0
  return pixel_frequency_dict
pixel_frequency_dict=add_key_to_dict(pixel_frequency(img))
# Săp xếp từ điển theo thứ tự tăng dần theo key
def sort_dictionary(pixel_dictionary):
  return dict((sorted(pixel_dictionary.items(), key=lambda x: x[0])))
# Tính xác suất của từng pixel
pixel_dictionary = sort_dictionary(pixel_frequency_dict)
# Tính xác suất của từng pixel
def pixel_probability(pixel_dictionary):
  pixel_probability={}
  for i in pixel_dictionary:
    pixel_probability[i]=pixel_dictionary[i]/pixel_count(img)
  return pixel_probability
pixel_probability_dict = pixel_probability(pixel_dictionary)
# tính cumulative probability
def cumulative_probability(pixel_probability_dict):
  max_pixel_value=max_gray_level_by_bits(bits)
  cumulative_probability={}
  cumulative_probability[0]=pixel_probability_dict[0]
  for i in range(1,max_pixel_value+1):
    cumulative_probability[i]=cumulative_probability[i-1]+pixel_probability_dict[i]
  return cumulative_probability
cumulative_probability_dict = cumulative_probability(pixel_probability_dict)
# round cumulative probability
def round_cumulative_probability(cumulative_probability_dict):
  index=max_gray_level_by_bits(bits)
  round_cumulative_probability={}
  for i in cumulative_probability_dict:
    round_cumulative_probability[i]=round(cumulative_probability_dict[i]*index)
  return round_cumulative_probability
round_cumulative_probability_dict = round_cumulative_probability(cumulative_probability_dict)
# Tạo ảnh mới
def new_image(img,round_cumulative_probability_dict):
  new_img=np.zeros((img.shape[0],img.shape[1]))
  for i in range(img.shape[0]):
    for j in range(img.shape[1]):
      new_img[i][j]=round_cumulative_probability_dict[img[i][j]]
  return new_img
new_img=new_image(img,round_cumulative_probability_dict)
# Plot
plt.figure(figsize=(8,8))
plt.subplot(2,2,1)
plt.imshow(img,cmap='gray')
plt.title('Original Image')
plt.subplot(2,2,2)
plt.hist(img.ravel(),256,[0,256])
plt.title('Histogram of Original Image')
plt.subplot(2,2,3)
plt.imshow(new_img,cmap='gray')
plt.title('New Image')
plt.subplot(2,2,4)
plt.hist(new_img.ravel(),256,[0,256])
plt.title('Histogram of New Image')
plt.show()
