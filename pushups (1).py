import cv2
import numpy as np
import time
import PoseModule as pm

cap = cv2.VideoCapture("C:\\Users\\ritik\\Desktop\\project\\AI GYM TRAINER\\pushups.mp4")

detector = pm.poseDetector()
count = 0
dir = 0
pTime = 0
while True:
    success, img = cap.read()
    img = cv2.resize(img, (1280, 720))
    img = detector.findPose(img, False)
    lmList = detector.findPosition(img, False)
    # print(lmList)
    if len(lmList) != 0:
        # Right Arm
        rightArm_angle = detector.findAngle(img, 12, 14, 16)
        # Left  leftArm_angle = detector.findAngle(img, 11, 13, 15)
        # Right side for pushups
        # rightLeg_angle = detector.findAngle(img, 24, 26, 28)
        # Left side for pushups
        # leftLeg_angle = detector.findAngle(img, 11, 23, 25)
        
        per = np.interp(rightArm_angle, (60, 152), (0, 100))
        bar = np.interp(rightArm_angle, (60, 152), (650, 100))

        # Check for the pushups
        color = (255, 0, 255)
        if per == 100:
            color = (0, 0, 0)
            if dir == 0:
                count += 0.5
                dir = 1
        if per == 0:
            color = (0, 0, 0)
            if dir == 1:
                count += 0.5
                dir = 0
                
        
        
        # Draw Bar
        cv2.rectangle(img, (1100, 100), (1175, 650), color, 3)
        cv2.rectangle(img, (1100, int(bar)), (1175, 650), color, cv2.FILLED)
        cv2.putText(img, f'{int(per)} %', (1100, 75), cv2.FONT_HERSHEY_PLAIN, 4,
                    color, 4)

        #  Count
        cv2.rectangle(img, (0, 450), (250, 720), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, str(int(count)), (45, 670), cv2.FONT_HERSHEY_PLAIN, 15,
                    (255, 0, 0), 25)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5,
                (255, 0, 0), 5)

    cv2.imshow("Image", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
