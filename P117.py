import cv2
vid= cv2.VideoCapture(0)
if(vid.isOpened()==False):
    print("Unable To Read")

height=int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(height)

width=int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
print(width)

fps=int(vid.get(cv2.CAP_PROP_FPS))
print(fps)

out=cv2.VideoWriter('yes.MP4',cv2.VideoWriter_fourcc(*'DIVX'),30,(width,height))
while(True):
    ret,frame=vid.read()
    cv2.imshow('Web cAm',frame)
    out.write(frame)
    if cv2.waitKey(2)==32:
        break
vid.release
out.release
cv2.destroyAllWindows()