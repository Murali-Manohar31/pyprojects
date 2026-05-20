from ultralytics import YOLO
import cv2
import time

model=YOLO("yolov8n.pt")

cap=cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannnot access the Camera")
    exit()