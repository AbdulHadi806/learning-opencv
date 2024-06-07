import numpy as np
import cv2

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

# Initialize pencil position
pencil_position = (0, 0)

while True:
    ret, frame = cap.read()

    # converting video gray scale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255,0,0, 5))
        # Update pencil position to the center of the face
        pencil_position = (x + w // 2, y + h // 2)
        roi_gray = gray[y:y+w, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
        for (ex, ey, ew, eh) in eyes:
            # Extract the region of interest (eye)
            eye_roi = roi_color[ey:ey+eh, ex:ex+ew]
            # Apply Gaussian blur to the eye region
            blurred_eye = cv2.GaussianBlur(eye_roi, (25, 25), 0)
            # Replace the eye region with the blurred image
            roi_color[ey:ey+eh, ex:ex+ew] = blurred_eye
    
    # Draw a circle representing the pencil
    cv2.circle(frame, pencil_position, 5, (0, 255, 0), -1)
        
    cv2.imshow('frame', frame)
    
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
