import sys
import os

import numpy as np
import matplotlib.pyplot as plt
import requests
from io import BytesIO

from PIL import Image
from scipy.fftpack import fft2,fftfreq

#get image from url
#url = input("Enter image url: ")
url = 'https://upload.wikimedia.org/wikipedia/en/7/7d/Lenna_%28test_image%29.png'
response = requests.get(url)
img = np.mean(np.asarray(Image.open(BytesIO(response.content))),axis = 2)

#fft image
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))

#define filter
[im_x,im_y] = img.shape
filter = np.zeros([im_x,im_y])
filter_radius = 50
filter[im_x/2 - radius:im_x/2 + radius, im_y/2 - radius:imyx/2 + radius] = 1

#display fft
plt.subplot(2,2,1)
plt.imshow(img)
plt.subplot(2,2,2)
plt.imshow(magnitude_spectrum)
plt.subplot(2,2,3)
plt.imshow(filter)
plt.subplot(2,2,4)
plt.show()

#user generates spectral filter

#display

#og image
#filtered image
#
                   
