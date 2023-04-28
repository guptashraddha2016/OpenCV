import cv2

cap = cv2.VideoCapture('sample.mp4')

frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)

fps = cap.get(cv2.CAP_PROP_FPS)

height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)


fourcc = cv2.VideoWriter_fourcc(*'DVIX')
out = cv2.VideoWriter('reve.avi',fourcc,fps,(int(height*0.5),int(width*0.5)))

print(f"frames is {frames}")
print(f"fps{fps}")

frame_index = frames-1

if(cap.isOpened()):
    while(frame_index!=0):
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
        ret, frame = cap.read()

        frame = cv2.resize(frame, (int(height*0.5),int(width*0.5)))

        cv2.imshow('winname',frame)

        out.write(frame)
        frame_index = frame_index-1

        if(frame_index%100==0):
            print(frame_index)

        if(cv2.waitKey(2)==ord('q')):
            break

out.release()
cap.release()
cv2.destroyAllWindows()


