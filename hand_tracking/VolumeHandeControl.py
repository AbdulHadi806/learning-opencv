import cv2
import time
import handTrackingModule as htm
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import numpy as np

wCam, hCam = 640, 460

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

cTime = 0
pTime = 0

detector = htm.handDetector(detectionCon=0.7)

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))


# volume.GetMute()
# volume.GetMasterVolumeLevel()
volRange = volume.GetVolumeRange()
# volume.setMasterVolumeLevel(0, None)
minVol = volRange[0]
maxVol = volRange[1]

vol = 0
vol_for_bar_tracking = 400
vol_percentage = 0

while True:
    success, img = cap.read()
    
    img = detector.findHands(img, draw=True)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        
        x1, y1 = lmList[4][1], lmList[4][2] # get only thumb tip
        x2, y2 = lmList[8][1], lmList[8][2] # get only index_finger_tip
        
        cx, cy = (x1+x2)//2, (y1+y2)//2 # get center point of line
        
        cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
        cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)
        
        length_of_line = math.hypot(x2-x1, y2-y1)
        print(length_of_line)
        if length_of_line < 50:
            cv2.circle(img, (cx, cy), 10, (0, 250, 0), cv2.FILLED)
            
        vol = np.interp(length_of_line, [50, 150], [minVol, maxVol])
        vol_for_bar_tracking = np.interp(length_of_line, [50, 150], [400, 150])
        vol_percentage = np.interp(length_of_line, [50, 150], [0, 100])
        try:
            volume.SetMasterVolumeLevel(vol, None)
        except Exception as e:
            print("Error:", e)
            
        cv2.rectangle(img, (50, 150), (85, 400), (0, 255, 0), 3)
        cv2.rectangle(img, (50, int(vol_for_bar_tracking)), (85, 400), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, f"{str(int(vol_percentage))} %", (40, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)

        
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime=cTime
    
    cv2.putText(img, str(int(fps)), (40, 70), cv2.FONT_HERSHEY_COMPLEX, 1, ( 255, 0, 0), 3)
    
    cv2.imshow('Video', img)
    
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()