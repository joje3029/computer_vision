import cv2
import time
import HandTrackingModule as htm
import pyautogui

def jump():
    pyautogui.keyDown('space')
    time.sleep(0)
    print("jump")
    pyautogui.keyUp('space')

cap= cv2.VideoCapture(0)


detector = htm.handDetector(detectionCon=0.75)

while True:

    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    # print(lmList)</span>

    if len(lmList) != 0:
        if lmList[8][2] < lmList[6][2]: # y 방향일때 2 , x 방향일때 1</span>
            jump()
            cv2.putText(img, "jump", (100, 70), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 3)

        if lmList[20][2] < lmList[18][2]:
            pyautogui.keyDown('down')
            time.sleep(0)
            print("down")
            cv2.putText(img, "Down", (480, 70), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 3)
        else:
            pyautogui.keyUp('down')


    cv2.imshow("Dino Hand Tracking", img)
    cv2.waitKey(1)