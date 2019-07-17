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
img = np.asarray(Image.open(BytesIO(response.content)))

#display image
plt.imshow(img)
p.tl.show

#fft image
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))

#display fft
plt.imshow(img)
print(magnitude_spectrum.shape)

plt.imshow(magnitude_spectrum[:,:,1])
plt.show()

#user generates spectral filter

#display

#og image
#filtered image
#
                   
