import cv2
import numpy as np

COLOR_RANGES = {
    'Yellow': [(5, 25, 80), (35, 85, 110)],
    'Red':    [(160, 100, 100), (180, 255, 255)],
    'Green':  [(40, 50, 50), (90, 255, 255)],
}

video_path = 'traffic_1.mp4'  
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Cannot open video.")
    exit()

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
out = cv2.VideoWriter('output_detected.mp4', fourcc, fps, (width, height))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    detected_color = "None"

    for color, ranges in COLOR_RANGES.items():
        
        lower, upper = ranges
        mask = cv2.inRange(hsv, np.array(lower), np.array(upper))
 
        non_zero = cv2.countNonZero(mask)
        if non_zero > 200: 
            detected_color = color

    cv2.putText(frame, f"Detected: {detected_color}", (50, 100),
                cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 4)

    out.write(frame)
    resized_frame = cv2.resize(frame, (640, 360))

    cv2.imshow('Resized Video', resized_frame)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
cap.release()
out.release()
cv2.destroyAllWindows()
