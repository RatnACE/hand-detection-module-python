import cv2
import mediapipe as mp
import time


cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw =mp.solutions.drawing_utils
pt=0
ct=0
while True:
    sucess, img=cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    rio = hands.process(imgRGB)
    #print(rio.multi_hand_landmarks)

    if rio.multi_hand_landmarks:
        for handLms in rio.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
               # print(id ,lm)
                h,w,c= img.shape
                cx,cy =int(lm.x*w) ,int(lm.y*h)
                #print(id,cx,cy)
                if id in (0,4,8,12,16,20) :
                    cv2.circle(img,(cx,cy),15,(0,0,255), cv2.FILLED)
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)



    ct=time.time()
    fps=1/(ct-pt)
    pt=ct

    cv2.putText(img,str(int(fps)),(10,50),cv2.FONT_HERSHEY_PLAIN,3,(255,210,178),3)

    cv2.imshow("captured", img)
    cv2.waitKey(1)
