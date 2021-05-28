# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 12:55:47 2020

@author: offic
"""

''' 
Step 1 : Import Required Packages
 import required packages 
 import face_recognition
 import cv2

Step 2 : 
 loading the image to detect 
  image_to_detect =cv2.imread('two-people.jpg')
Step 3 : Find and print total number of faces
 # find all face locations using face_locations() function
 # model can be 'cnn' or 'hog'
 # number_of_times_to_upsameple =1 heigher and detect more faces
 means number of face to detect the object  
 all 
 
 Step 3 Find and print total number of faces
 
 Step 4:Loop through faces
 
 Step 5: Position of faces right ,top,bottom,left position and pixel value find
 
 Setp 6: Slice Image array by positions inside the loop
  
   current_face_image =image_to_detect[top_pos:bottom_pos,left_pos,:right_pos,left_pos]
   

 Step 7: Show each sliced face inside the loop
  
    cv2.imshow("Face No:"+str(index),current_face_image)
 
  
  # code
  
'''
  
import cv2
import face_recognition

#loading the image to detect 

image_to_detect = cv2.imread('images/leza.jpg')

# detect all faces in the 
# aarguments all faces in the no,of times to up sample,model
#changes the model  hog  to cnn  (cnn for advance for nural network )
#hog besically is very fast but cnn is very slow
 
all_face_locations =face_recognition. face_locations(image_to_detect,model='hog')


print('There are {} no of faces in this image'.format(len(all_face_locations)))

#looping through the face locations

for index,current_face_location in enumerate(all_face_locations):
    
    #splitting the tuple to get four position values of current face 
    top_pos,right_pos,bottom_pos,left_pos = current_face_location
    
    print('found face {} at top :{},right:{},bottom:{},left:{}'.format(index+1,top_pos,right_pos,bottom_pos,left_pos))
    
    # slicing the locations of current face
    current_face_image = image_to_detect[top_pos:bottom_pos:,left_pos:right_pos]
    # showing  the current face with dynamic title
    
    cv2.imshow('face no' +str(index+1),current_face_image)
    

cv2.imshow('test',image_to_detect)

cv2.waitKey(0)
cv2.destroyAllWindows()
   