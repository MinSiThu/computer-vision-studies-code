# -*- coding: utf-8 -*-
"""SIFT.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZJ5UznCU_KuVOzo6p-PpSzpE3lPG-Bvc
"""

# Commented out IPython magic to ensure Python compatibility.
import cv2
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

image = cv2.imread("lenna.png")
image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
plt.imshow(image)
plt.show()

sift = cv2.xfeatures2d.SIFT_create()
keypoints, descriptors = sift.detectAndCompute(image,None)

output = cv2.drawKeypoints(image,keypoints,image.copy())
plt.imshow(output)
plt.show()