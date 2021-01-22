from cv2 import cv2
cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)

cap.set(10,100)
result=True

while (result):
    success,img=cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        cv2.imwrite("NewImage.jpg",img)
        cap.release()
        cv2.destroyAllWindows()
        break




    
    



