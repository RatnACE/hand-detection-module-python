import cv2
import mediapipe as mp
import time
import handtrackingmodule as ht

pt = 0
ct = 0
cap = cv2.VideoCapture(0)
detector = ht.handsDetector()
while True:
    sucess, img = cap.read()
    img = detector.findHands(img)
    lmlist = detector.findPositoin(img,draw=False)
    if len(lmlist)!=0:
        print(lmlist[4])
    ct = time.time()
    fps = 1 / (ct - pt)
    pt = ct

    cv2.putText(img, str(int(fps)), (10, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 210, 178), 3)

    cv2.imshow("captured", img)
    cv2.waitKey(1)