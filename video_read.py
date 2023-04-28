import cv2

#instance of video capture
cap = cv2.VideoCapture(0)

# checking if the camera is opened or not
opned = cap.isOpened()

#fourcc - four character code for determingin the codec of the video file
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

#getting the properties of the video using video capture instance
height= cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
fps = cap.get(cv2.CAP_PROP_FPS)

#output video writer creation
out = cv2.VideoWriter('jj.avi',fourcc,fps,(int(width),int(height)))

print("Frames are {}".format(fps))

#Showing and storing the live camers feed
#check if camera is opened

if(opned):
    #Run until it remains open
    while(cap.isOpend()):
        #Get the frame from Video Capture Instance
        ret, frame = cap.read()
        #return ret variable tells if the frame is returned successfully
        if(ret==True):
            cv2.imshow('winname',frame)

            #writting the frame to video output
            out.write(frame)
            #wait for 2 milliseconds for each frame
            # if user press 'esc' key then exit loop
            if(cv2.waitKey(2)==27):
                break

out.release()
cap.release()
cv2.destroyAllWindows()

            



