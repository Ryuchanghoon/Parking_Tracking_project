import cv2
from ultralytics import YOLO



model = YOLO('yolov8n.pt')

video_path = 'parking_entrance.mp4'

vehicle_class_ids = [2, 3, 5, 7]  # 2: 'car', 3: 'motorcycle', 5: 'bus', 7: 'truck'


cap = cv2.VideoCapture(video_path)

while cap.isOpened():
    ret, frame = cap.read()
    
    if not ret:
        break
    
    results = model(frame)
    
    for result in results:
        boxes = result.boxes 
        
        for box in boxes:
            class_id = int(box.cls) 
            if class_id in vehicle_class_ids:
                x1, y1, x2, y2 = map(int, box.xyxy[0]) 
                confidence = box.conf.item() 
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, f'Vehicle {class_id} {confidence:.2f}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow('Vehicle Tracking', frame)
    
    
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()