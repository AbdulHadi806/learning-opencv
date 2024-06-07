import os
import cv2
import numpy as np

people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
DIR = r"D:\opencv\opencv-learning\assets\Faces\train"

features = []
labels = []

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)
        
        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            
            img_array = cv2.imread(img_path)
            gray = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)
            
            faces_rect = face_cascade.detectMultiScale(gray, 1.1, 4)
            
            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)
                
create_train()
print('Training Done------------')

features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer = cv2.face.LBPHFaceRecognizer_create()


face_recognizer.train(features, labels)

save_dir = r"D:\opencv\opencv-learning\face_recognition"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# Save the trained model and the data
face_recognizer.save(os.path.join(save_dir, 'face_trained.yml'))
np.save(os.path.join(save_dir, 'features.npy'), features)
np.save(os.path.join(save_dir, 'labels.npy'), labels)

print('Model and data saved successfully!')
