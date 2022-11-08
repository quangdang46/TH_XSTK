import matplotlib.pyplot as plt
import numpy as np
import cv2

def histogram(data, bins=10):
  data = np.array(data)
  min = data.min()
  max = data.max()
  bins = np.linspace(min, max, bins)
  binwidth = bins[1] - bins[0]
  bincenters = bins[:-1] + binwidth/2
  hist = np.histogram(data, bins)[0]
  return hist, bincenters

def interp(array, xp, fp):
  indices = np.searchsorted(xp, array)
  indices = np.clip(indices, 0, len(fp)-1)
  return fp[indices]

def cumsum(a):
  a = np.array(a).flatten()
  b = [a[0]]
  for i in a[1:]:
    b.append(b[-1] + i)
  return np.array(b)


def flatten(listOfLists):
  return [ item for elem in listOfLists for item in elem ]

def histeq(im,nbr_bins=256):
  imhist,bins = histogram(flatten(im),nbr_bins)
  cdf = cumsum(imhist) # cumulative distribution function
  cdf = 255 * cdf / cdf[-1] # normalize
  im2 = interp(flatten(im),bins[:-1],cdf)
  return im2.reshape(im.shape), cdf

'''
[[147 147 149 ... 183 182 182] 
 [143 144 147 ... 185 184 182] 
 [148 149 152 ... 186 185 184] 
 ...
 [161 160 160 ... 155 156 156] 
 [161 159 160 ... 155 156 156] 
 [161 159 160 ... 155 157 156]]
'''

# plot
def show(x,title):
  plt.subplot(2,2,x)
  plt.title(title)


img=cv2.imread('unsplash.jpg',0)


# histogram equalization
img2,cdf = histeq(img)

show(1,'original')
plt.hist(img.flatten(),256,[0,256], color = 'r')

show(2,'histogram equalization')
plt.hist(img2.flatten(),256,[0,256], color = 'r')

show(3,'original')
plt.imshow(img, cmap='gray')

show(4,'histogram equalization')
plt.imshow(img2, cmap='gray')

plt.show()


