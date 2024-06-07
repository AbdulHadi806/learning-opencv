import numpy as np
import cv2

# Capture video from the default camera
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the video capture
    ret, frame = cap.read()

    if not ret:
        break

    # Get the width and height of the frame
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Create an empty image with the same shape as the frame
    image = np.zeros(frame.shape, np.uint8)

    # Resize the frame to half its size
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

    # Draw lines on the frame
    frame_with_lines = cv2.line(frame.copy(), (0, 0), (width, height), (255, 0, 0), 10)
    frame_with_lines = cv2.line(frame_with_lines, (0, height), (width, 0), (0, 255, 0), 10)
    frame_with_lines = cv2.rectangle(frame_with_lines, (0, 0), (300, 300), (128, 128, 128), 20)
    frame_with_lines = cv2.circle(frame_with_lines, (0, 0), 60, (128, 128, 128), 20)
    font = cv2.FONT_HERSHEY_SIMPLEX
    frame_with_lines = cv2.putText(frame_with_lines, 'Abdul is a Pro', (200, height - 10), font, 1, (0, 0, 0), 5, cv2.LINE_AA)
    
    # Place the smaller frames into the larger image
    image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    image[height//2:, :width//2] = smaller_frame
    image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    image[height//2:, width//2:] = smaller_frame

    # Show the manipulated frame
    cv2.imshow('frame', frame_with_lines)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release the video capture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
