import cv2
import numpy as np
import time
import PoseModule as pm

cap = cv2.VideoCapture("C:\\Users\\ritik\\Desktop\\project\\AI GYM TRAINER\\gh.mp4")

detector = pm.poseDetector()
count = 0
dir = 0
pTime = 0
while True:
    success, img = cap.read()
    # img = cv2.imread("active.png")
    img = cv2.resize(img, (1280, 720))
    img = detector.findPose(img, False)
    lmList = detector.findPosition(img, False)
    # print(lmList)
    if len(lmList) != 0:
        # Right side for Glute Bridge
        # rightLeg_angle = detector.findAngle(img, 24, 26, 28)
        # Left side for Glute Bridge
        leftLeg_angle = detector.findAngle(img, 11, 23, 25)
        
        # Angle Range to Percentage
        per = np.interp(leftLeg_angle, (136, 182), (0, 100))
        bar = np.interp(leftLeg_angle, (136, 182), (650, 100))

        # Glute bridge
        color = (235, 185, 47)
        if per == 100:
            color = (0, 255, 0)
            if dir == 0:
                count += 0.5
                dir = 1
        if per == 0:
            color = (0, 255, 0)
            if dir == 1:
                count += 0.5
                dir = 0

        # Draw Bar
        cv2.rectangle(img, (1100, 100), (1150, 650), color, 3)
        cv2.rectangle(img, (1100, int(bar)), (1150, 650), color, cv2.FILLED)
        cv2.putText(img, f'{int(per)} %', (1100, 75),
                    cv2.FONT_HERSHEY_PLAIN, 4, color, 4)

        # Draw Count
        cv2.circle(img, (95, 625), 80, (0, 255, 0), cv2.FILLED)
        cv2.putText(img, str(int(count)), (46, 680),
                    cv2.FONT_HERSHEY_PLAIN, 10, (255, 255, 255), 15)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5,
                (255, 0, 0), 5)

    cv2.imshow("Image", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
