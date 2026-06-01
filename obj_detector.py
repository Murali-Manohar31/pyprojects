from ultralytics import YOLO
import cv2
import time

model=YOLO("yolov8n.pt")

cap=cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannnot access the Camera")
    exit()
    
prev_time=0
while True:
    ret,frame=cap.read()
    
    if not ret:
        print("failed to grab frame")
        break
#YOLO Detection
results=model(frame)
annotated_frame = results[0].plot()

current_time=time.time()
fps=1/(current_time-prev_time)
prev_time=current_time