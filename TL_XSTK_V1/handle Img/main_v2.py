import numpy as np
import cv2
import matplotlib.pyplot as plt

name_img="unsplash.jpg"
# 1. Read image
img = cv2.imread(name_img, 0)
# 2. Calculate histogram
hist, bins = np.histogram(img.flatten(), 256, [0, 256])

# 3. Calculate cdf
cdf = hist.cumsum()
print(cdf)
cdf_normalized = cdf * hist.max() / cdf.max()
# 4. Calculate cdf_m
cdf_m = np.ma.masked_equal(cdf, 0)
cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
cdf = np.ma.filled(cdf_m, 0).astype('uint8')
# 5. Calculate new image
img2 = cdf[img]
# 6. Calculate new histogram
hist, bins = np.histogram(img2.flatten(), 256, [0, 256])
# 7. Calculate new cdf
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max() / cdf.max()
# 8. Plot
plt.subplot(221)
plt.imshow(img, 'gray')
plt.title('Original')
plt.subplot(222)
plt.plot(cdf_normalized, color='b')
plt.hist(img.flatten(), 256, [0, 256], color='r')
plt.xlim([0, 256])
plt.legend(('cdf', 'histogram'), loc='upper left')
plt.title('Histogram')
plt.subplot(223)
plt.imshow(img2, 'gray')
plt.title('Equalized')
plt.subplot(224)
plt.plot(cdf_normalized, color='b')
plt.hist(img2.flatten(), 256, [0, 256], color='r')
plt.xlim([0, 256])
plt.legend(('cdf', 'histogram'), loc='upper left')
plt.title('Histogram')
plt.show()
