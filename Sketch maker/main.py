import cv2
cam=cv2.VideoCapture(0)
while True:
    image=cam.read()[1]
    grey=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    res=cv2.Canny(grey,10,200)
    cv2.imshow('s',res)
    if cv2.waitKey(50)==ord('q'):
        cv2.destroyAllWindows()
        break
cam.release()