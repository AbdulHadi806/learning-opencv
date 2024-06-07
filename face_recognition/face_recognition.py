import numpy as np 
import cv2

harr_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']

# features = np.load('./features.npy')
# labels = np.load('./labels.npy')

face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read(r'D:\opencv\opencv-learning\face_recognition\face_trained.yml')

img = cv2.imread(r'D:\opencv\opencv-learning\assets\Faces\val\elton_john\2.jpg')
cv2.imshow('img', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces_rect = harr_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+h]
    
    label, confidence = face_recognizer.predict(faces_roi)
    
    cv2.putText(img, str(people[label]), (20, 20), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), 2)
    
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
cv2.imshow("Detected img", img)
cv2.waitKey(0)