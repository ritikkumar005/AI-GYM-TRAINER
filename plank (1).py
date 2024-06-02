import cv2
import numpy as np
import time
import PoseModule as pm

cap = cv2.VideoCapture("C:\\Users\\ritik\\Desktop\\project\\AI GYM TRAINER\\plank.mp4")
detector = pm.poseDetector( )



while True:
    success, img = cap.read()
    img= cv2.resize(img,(1280,720))
    img=detector.findPose(img,False)
    lmList = detector.findPosition(img,False)
    #print(lmList)

    if len(lmList) != 0 :
        angle = detector.findAngle(img,11,23,25)
        per= np.interp(angle,(183,190),(0,100))
        bar = np.interp(angle,(180,192),(600,100))
       # print(angle , per)


    # Draw Bar
        cv2.rectangle(img, (1100, 100), (1175, 650), (0,255,0), 3)
        cv2.rectangle(img, (1100, int(bar)), (1175, 650), (0,255,0), cv2.FILLED)
        cv2.putText(img, f'{int(per)} %', (1100, 75), cv2.FONT_HERSHEY_PLAIN, 4,
                    (0,255,0), 4)


       


        





    cv2.imshow("Image",img)
    cv2.waitKey(1)
   