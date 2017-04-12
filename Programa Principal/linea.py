import numpy as np
import cv2

cap = cv2.VideoCapture(1)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #Convertirlo a espacio de color HSV
    #Se crea un array con las posiciones minimas y maximas
    lower=np.array([0,0,0])
    upper=np.array([255,255,50])
 
    #Deteccion de colores
    mask = cv2.inRange(hsv, lower, upper)
    
    #edges = cv2.Canny(mask,50,150,apertureSize = 3)
    minLineLength = 100
    maxLineGap = 10
    lines = cv2.HoughLinesP(mask,1,np.pi/180,100,minLineLength,maxLineGap)
    try:
        for x1,y1,x2,y2 in lines[1]:
            cv2.circle(frame,(x1,y1),5,(0,0,255),-1)
            cv2.circle(frame,(x2,y2),5,(255,0,0),-1)
            print x1
    except:
        continue
    
    cv2.imshow('linea',frame)
    cv2.imshow('mask', mask)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

