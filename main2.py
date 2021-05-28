# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 11:51:52 2020

@author: offic
"""


import cv2
import dlib
import face_recognition

img =cv2.imread('lena.png')

#
print(cv2.__version__)
print(dlib.__version__)
print(face_recognition.__version__)

cv2.imshow("Original",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

