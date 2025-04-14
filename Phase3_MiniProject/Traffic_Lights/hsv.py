import cv2
import numpy as np

# Initialize the mouse callback function
def get_hsv_values(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:  # Left mouse button click
        # Get the pixel at (x, y)
        pixel_bgr = frame[y, x]
        
        # Convert the pixel from BGR to HSV
        pixel_hsv = cv2.cvtColor(np.uint8([[pixel_bgr]]), cv2.COLOR_BGR2HSV)
        
        # Get HSV values
        h, s, v = pixel_hsv[0][0]
        
        # Print the HSV values
        print(f"HSV Values at ({x}, {y}): H = {h}, S = {s}, V = {v}")

# Capture video from a file or camera
cap = cv2.VideoCapture('traffic_1.mp4')  # Use 0 for webcam

# Create a named window
cv2.namedWindow('Video Window')

# Set the callback function for mouse events
cv2.setMouseCallback('Video Window', get_hsv_values)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Display the video frame
    cv2.imshow('Video Window', frame)

    # Wait for a key press (1ms delay)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
