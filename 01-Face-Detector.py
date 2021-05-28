
   # Introduction Face detector 
print("Hello")

import cv2
#import numpy as np

print(cv2.__version__)
#print(numpy__version__


# Face Detection
'''
-> Face detection is the process of automatically locating human faces in visul meadia (digital or video)

-> Two popular types of face Detectors image_recongnition libray
supports. 

-> Hog Face Detector(popular face detector) 

-> CNN based Face Detector in Dlib
     
              :  HOG FACE DETECTOR :

-> A hog (histogram of oriented gradients) is generally used for objects detection.
-> A Hog relies on distribution of intensity gradients or edge directions
  
  Pros
  . Faster while using in cpu very light weight
  . Works under small occlusion
  
  Cons
  . Min size of face should be 80*80px
  . Does not work for side face or high extrems of non-frontal faces like looking down or up
  . Does not work under heavy occlusion (sunglass ,hat/cap,scarf,beard etc)
  
                 2 CNN FACE DETECTOR IN DLIB :
  This is advanced face detctor 
  .This method uses object-Detector with cnn based features.
  . The traning proess is simple .no need for large amount of training data.
  
               Pros
 . Detect the multiple face  orientations
 . Works with medium occulusion
 . Fast on GPU
               Cons
 . Very slow cpu
 
 Conversion of face using nural network based to detect the face
 
      
        
'''