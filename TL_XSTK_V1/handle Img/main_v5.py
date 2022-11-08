import matplotlib.pyplot as plt
import numpy as np
import cv2

img=cv2.imread('n.jpg',0)

#create list of values 0-255
values=[i for i in range(256)]

#set width and height of image
width=img.shape[0]
height=img.shape[1]

#for each intensity level
for i in range(256):
  #count number of pixels with that intensity
  values[i]=np.sum(img==i)

#initialize list for frequency probabilities
prob=[0 for i in range(256)]

#calculate frequency probabilities
for i in range(256):
  prob[i]=values[i]/(width*height)

#initialize list for cumulative probabilities
cum_prob=[0 for i in range(256)]

#calculate cumulative probabilities
cum_prob[0]=prob[0]
for i in range(1,256):
  cum_prob[i]=cum_prob[i-1]+prob[i]

#initialize list for cumulative probabilities multiplied by 255
cum_prob_255=[0 for i in range(256)]

#calculate cumulative probabilities multiplied by 255
for i in range(256):
  cum_prob_255[i]=round(cum_prob[i]*255)

#initialize list for new intensity values
new_values=[0 for i in range(256)]

#calculate new intensity values
for i in range(256):
  new_values[i]=cum_prob_255[i]

#initialize list for new image
new_img=[0 for i in range(width*height)]

#calculate new image
for i in range(width):
  for j in range(height):
    new_img[i*height+j]=new_values[img[i][j]]

#reshape new image
new_img=np.reshape(new_img,(width,height))

# show original image
plt.imshow(img,cmap='gray')
plt.title('Original Image')
plt.show()

# show new image
plt.imshow(new_img,cmap='gray')
plt.title('New Image')
plt.show()

#plot histogram of original image
plt.hist(img.ravel(),256,[0,256])
plt.title('Histogram of Original Image')
plt.show()

#plot histogram of new image
plt.hist(new_img.ravel(),256,[0,256])
plt.title('Histogram of New Image')
plt.show()