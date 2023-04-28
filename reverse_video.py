import cv2

#video capture instance
cap = cv2.VideoCapture('sample.mp4')

#total number of frames in video
frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)

#frames per second of video
fps = cap.get(cv2.CAP_PROP_FPS)

#height and width of video
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)

#intitating the output writter for video
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('reverse.avi',fourcc,fps,((int(width*0.5),int(height*0.5))))

print(f"No.of frames are {frames}")
print(f"FPS is {fps}")

frame_index = frames-1

#checking if the video instance is ready
if(cap.isOpened()):
    #reading till the end of the video
    while(frame_index!=0):
        # we set the current frame position to last frame
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
        ret,frame = cap.read()

        #resize the frame
        frame = cv2.resize(frame,(int(width*0.5),int(height*0.5)))

        # to show the reversing video
        cv2.imshow('winname',frame)

        #writting the reversed video
        out.write(frame)

        frame_index = frame_index-1

        #printing the progress
        if(frame_index%100==0):
            print(frame_index)

        if(cv2.waitKey(2)==ord('q')):
            break
out.release()
cap.release()
cv2.destroyAllWindows()

