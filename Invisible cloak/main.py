import cv2
import numpy as np
if __name__ == "__main__":
    cam=cv2.VideoCapture(0)
    time=0
    background=cam.read()[1]
    while True:
        background=cam.read()[1]
        text=''
        if time<50:
            text='Taking Background Image Plz get aside'
            cv2.putText(background,text,(10,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),1)
        elif 120>time:
            cv2.putText(background,str(3-(time-50)//30),(200,200),cv2.FONT_HERSHEY_SIMPLEX,3,(0,0,0),5)
        else:
            
            cv2.destroyAllWindows()
            break
        cv2.imshow('image',background)
        if cv2.waitKey(70)==ord('q'):
            cv2.destroyAllWindows()
            break
        time+=1
             
            

    while True:
        image=cam.read()[1]
        mask=cv2.inRange(image,np.array([0,0,0]),np.array([50,50,50]))
        one=cv2.bitwise_and(background,background,mask=mask)
        mask=cv2.bitwise_not(mask)
        two=cv2.bitwise_and(image,image,mask=mask)
        cv2.imshow('mask',one+two)
   
        
        if cv2.waitKey(70)==ord('q'):
            cv2.destroyAllWindows()
            break
    



        
    cam.release()
    
    