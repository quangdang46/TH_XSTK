import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('image.jpg',0)
def compute_histogram(img):
	histogram = np.zeros(256)
	for i in range(img.shape[0]):
		for j in range(img.shape[1]):
			histogram[img[i,j]] += 1
	return histogram

def compute_cumulative_histogram(histogram):
	cumulative_histogram = np.zeros(256)
	cumulative_histogram[0] = histogram[0]
	for i in range(1,256):
		cumulative_histogram[i] = cumulative_histogram[i-1] + histogram[i]
	return cumulative_histogram
	
def compute_mapping_function(cumulative_histogram):
	mapping_function = np.zeros(256)
	for i in range(256):
		mapping_function[i] = 255 * cumulative_histogram[i] / cumulative_histogram[255]
	return mapping_function

def histogram_equalization(img):
	histogram = compute_histogram(img)
	cumulative_histogram = compute_cumulative_histogram(histogram)
	mapping_function = compute_mapping_function(cumulative_histogram)
	img_equalized = np.zeros(img.shape)
	for i in range(img.shape[0]):
		for j in range(img.shape[1]):
			img_equalized[i,j] = mapping_function[img[i,j]]
	return img_equalized

img_equalized = histogram_equalization(img)
plt.subplot(121)
plt.imshow(img,cmap = 'gray')
plt.title('Original Image')
plt.xticks([])
plt.yticks([])
plt.subplot(122)
plt.imshow(img_equalized,cmap = 'gray')
plt.title('Equalized Image')
plt.xticks([])
plt.yticks([])
# display the histogram of the original image
plt.figure()
plt.hist(img.ravel(),256,[0,256])
plt.title('Histogram of Original Image')
# display the histogram of the equalized image
plt.figure()
plt.hist(img_equalized.ravel(),256,[0,256])
plt.title('Histogram of Equalized Image')
plt.show()


