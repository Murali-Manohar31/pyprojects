from ultralytics import YOLO
from collections import defaultdict
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
    results= model(frame)
    object_counts=defaultdict(int)
    for result in results:
        boxes=result.boxes
        
        for box in boxes:
            cls = int(box.cls[0])
            class_name=model.names[cls]
            object_counts[class_name] +=1
    cv2.imshow("Object Detector",frame)
    

#YOLO Detection
    results=model(frame)
    annotated_frame = results[0].plot()

    current_time=time.time()
    fps=1/(current_time-prev_time)
    prev_time=current_time

    cv2.putText(
        annotated_frame,
        f"FPS: {int(fps)}",(20,40),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2   
)

    cv2.imshow("Real-Time Object Detector ",annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()