# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 17:47:00 2020

@author: offic
"""


'''
               Real time Face Detection
 . A real time face detection system can identify face from a vide frame.
 
 -> The mechanism is very similar to detection from image with following changes
  -> Get the webcam Video
  
  -> Loop through every single video frame image and do face detection

  Step 1 Get the default webcam video
    import face_recognition
    import cv2
    # Get the webcam #0 (the default one,1,2 etc means additional attached cams)
    
    web_cam_video_stream = cv2.VideoCapture(0)(default index means default camera but camera is change then 1,2,or any other index)
    
 Step 2: Initialize empty array for face locations
     
    all_face_locations =[]
 Step 3: Create an outer while loop to loop through each frame of video
     
      while True :

 Step 4: Get single frame of video as image
  
   #get current frame
 (return)  ret,current_frame =webcam_video_stream.read()
 
 step 5: Resize the frame to a quarter of size so that the computer can proces
 it faster 
   
 current_frame_small =cv2.resize(current_frame,(0,0),fx=0.25,fy=0.25)
 
 Step 6 : Find the total number of faces
#find all face locations using face_locations() function
#model can be 'cnn' or 'hog'
# number of_times_to_upsample =1 higher detect and more faces
 
 all face_locations =face_recognition.face_locations(current_frame_small,model="hog")
 
 Step 7

  Step 8 : Correct the co-ordinate location to the change the while resizeing to 1/4 size inside the loop
 
    top_pos  =top_pos*4
    right_pos =top_pos*4
    bottom_pos=top_pos*4
    left_pos  =top_pos*4
    
    Step 9: Draw rectangle around each face location in the main video frame inside the loop
    
    cv2.rectangle(current_frame,left_pos,top_pos),(right_pos,bottom_pos),(0,0,255),2)(direction,color,thickness)
  
    Step 10:
    
   Step 11: Display the current frame outside the while loop
      cv2.imshow("Webcam Video",current_frame)
  Step 12 : Wait for a key press to break the while loop
    
     #Press 'q' on the keyboard to break the while loop!
       if cv2.waitKey(1) & 0xFF==ord('q'):
            break
  Step 13: Once Loop breaks,release the camera and close all open windows
       #Release the Webcam resource
   webcam_video_stream.release()
   cv2.destroyAllWinodws()
  '''
import cv2
import face_recognition

# default camera indexe
webcam_video_stream = cv2.VideoCapture(0)

#initialize the array variable to hold all face locations in the frame

all_face_locations =[]

#loop through ecery frame in the video
while True:#means the no face detector true means 
    #get the current frame from the video stream as an image
    ret,current_frame =webcam_video_stream.read()
    #resize the current frame to 1/4 size to process faster
    current_frame_small =cv2.resize(current_frame,(0,0),fx=0.25,fy=0.25)
    
    #detect the all faces in the image
    #arguments are image ,no of times to upsample model
    
    all_face_locations =face_recognition.face_locations(current_frame_small,model='hog')
    
    #looping through the face locations
    for index,current_face_location in enumerate(all_face_locations):
    
    #splitting the tuple to get four position values of current face 
        
        top_pos,right_pos,bottom_pos,left_pos = current_face_location
        
     #change the position magnitude to fit the actual size video frame
     
        top_pos = top_pos*4
        right_pos =right_pos*4
        bottom_pos =bottom_pos*4
        left_pos =left_pos*4
    
    #printing the locations of current face index
    print('Found face {} at top:{},right:{},bottom:{},left:{}'.format(index+1,top_pos,right_pos,bottom_pos,left_pos))
    #draw rectangle around the face detected
    
     
    cv2.rectangle(current_frame,(left_pos,top_pos,),(right_pos,bottom_pos),(0,0,255),2)
    
    
    #showing the current face with dynamic
    
    cv2.imshow("Web Cam video"+str(index+1),current_frame)
    
   
# this is 0xFF is a 32 bit 
    if cv2.waitKey(1) & 0xFF ==ord('q'):# so is very imp other wise my camera always on not closed so very imp to close the camera
        
        break

webcam_video_stream.release()# this function to release the camera 
cv2.destroyAllWindows()

    



  