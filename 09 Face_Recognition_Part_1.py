# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 19:08:42 2020

@author: offic
"""


"""
  Face Recongnition/Classification
 Find the in out database of known people who has the closest measurements to our test image,
 
   # Face Alignent
 -> face alignment plays an important role in face recognition,because it is often used as a per-processing step.
  
  -> the automatic detection of the face and eye region and align face based on translation,sclae,and rotation
   
  -> scaling  means height and width
  -> Orientation means changing the angle
     # Feature  Extraction
    Pass the detected and pre-Processed face into a pre-trained face recognizer
    that is capable of producing 128-D embedding
    
    # so openface library for face recognition
     
     Reusing the Image Face Detection Code
    
      Step 1: Load Sample Images and Extract the face Encodings
      
      # load a sample a picture and extract face encodings.
      # Return a list of 128- Dimensional face encodings
      # (one are getting the first face(assuming only one face ))
      
      # load next sample picture and extract face encodings.
      
       grayscale_image = face_recogntion.load_image_file("images/samples/gray_scale.jpg")
       
       gray_scale_encoding = face_recognition_encodings(gray_scale_image)[0]
       
       Step 2: Create an array to save the encodings
         
           known_face_encodings = [lena_face_encoding,grayscale_encoding]
      Step 3: Create another array to held labels
      
         known_face_names =["Lena","Gray Scale"]
       
      
      
"""
