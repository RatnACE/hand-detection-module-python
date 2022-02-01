import cv2
import mediapipe as mp
import time

class handsDetector():
    def __init__(self, mode=False,maxHands=2, complexity =1, detectionCon=0.5,trackCon=0.5):
        self.mode=mode
        self.maxHands=maxHands
        self.complexity = complexity
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.mphands = mp.solutions.hands
        self.hands = self.mphands.Hands(self.mode, self.maxHands,self.complexity,self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
    def findHands(self,img,draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.rio =self.hands.process(imgRGB)
        #print(rio.multi_hand_landmarks)
        if self.rio.multi_hand_landmarks:
            for handLms in self.rio.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms,self.mphands.HAND_CONNECTIONS)

        return img
    def findPositoin(self,img,handNo= 0,draw =True):
        lmlist =[]
        if self.rio.multi_hand_landmarks:
            hand1 = self.rio.multi_hand_landmarks[handNo]
            for id, lm in enumerate(hand1.landmark):
                # print(id ,lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                #print(id, cx, cy)
                lmlist.append([id,cx,cy])
                if draw:
                    # if id in (0, 4, 8, 12, 16, 20):
                    cv2.circle(img, (cx, cy), 7, (0, 0, 255), cv2.FILLED)

        return lmlist

def main():
    pt = 0
    ct = 0
    cap = cv2.VideoCapture(0)
    detector = handsDetector()
    while True:
        sucess, img = cap.read()
        img = detector.findHands(img)
        lmlist = detector.findPositoin(img)
        if len(lmlist)!=0:
            print(lmlist[4])
        ct = time.time()
        fps = 1 / (ct - pt)
        pt = ct

        cv2.putText(img, str(int(fps)), (10, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 210, 178), 3)

        cv2.imshow("captured", img)
        cv2.waitKey(1)




if __name__ == "__main__":
    main()