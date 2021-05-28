  



 #Blur faces tows stay anonoymous
 #slice frame image array by positioms current _face_image=current_frame[top_pos:bottom_pos,left_pos:right_pos]
 # Blur the current face image
 #current_face_image =cv2.GaussianBlur(current_face_image,(99,99),30)
    
 # Put the blurred face region back into frame image
 #current_frame[top_pos:bottom_pos,left_pos:right_pos]=current_face_image 
 
        

 
import cv2
import face_recognition

# default camera function
webcam_video_stream = cv2.VideoCapture(0)

#initialize the array variable to hold all face locations in the frame

all_face_locations =[]# means index find the face of locations

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
    
        #slicing the current face from main image
        current_face_image = current_frame[top_pos:bottom_pos,left_pos:right_pos]
        #cv2.GaussianBlur(source(src),kernel size(Ksize),deviation(sigmaX))

        current_face_image =cv2.GaussianBlur(current_face_image,(99,99),30)
     
        #paste the blurred face into the actual frame
     
        current_frame[top_pos:bottom_pos,left_pos:right_pos] = current_face_image
     
        #draw rectangle around the face detected
        cv2.rectangle(current_frame,(left_pos,top_pos,),(right_pos,bottom_pos),(0,0,255),2)
    
    
        #showing the current face with reactangle drwan
    
    cv2.imshow("Web Cam video",current_frame)
    
   
# this is 0xFF is a 32 bit 
    if cv2.waitKey(1) & 0xFF ==ord('q'):# so is very imp other wise my camera always on not closed so very imp to close the camera
        
        break

webcam_video_stream.release()# this function to release the camera 
cv2.destroyAllWindows()