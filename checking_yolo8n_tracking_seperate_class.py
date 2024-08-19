import cv2
from ultralytics import YOLO



model = YOLO('yolov8n.pt')

video_path = 'parking_entrance.mp4'

vehicle_class_ids = [2, 3, 5, 7]  # 2: 'car', 3: 'motorcycle', 5: 'bus', 7: 'truck'

top_left = (176, 230)
bottom_right = (601, 352)


vehicle_count = 0

previous_vehicles = []

cap = cv2.VideoCapture(video_path)


while cap.isOpened():
    ret, frame = cap.read()
    
    if not ret:
        break
    
    results = model(frame)
    
    current_vehicles = []


    for result in results:
        boxes = result.boxes 
        

        # 차량 bounding box
        for box in boxes:
            class_id = int(box.cls) 
            if class_id in vehicle_class_ids:
                x1, y1, x2, y2 = map(int, box.xyxy[0]) 
                confidence = box.conf.item()


                ### bounding box 안에 있는거 checking
                if x1 >= top_left[0] and y1 >= top_left[1] and x2 <= bottom_right[0] and y2 <= bottom_right[1]:
                    current_vehicles.append((x1, y1, x2, y2))


                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(frame, f'Vehicle {class_id} {confidence:.2f}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)


                    # bounding box 지나간거 checking
                    if any([
                        x1 < top_left[0] and x2 > top_left[0],  # 차량 왼쪽 진입
                        x1 < bottom_right[0] and x2 > bottom_right[0],  # 차량 오른쪽 탈출
                        y1 < top_left[1] and y2 > top_left[1],  # 차량 위 진입
                        y1 < bottom_right[1] and y2 > bottom_right[1]  # 차량 아래로 탈출
                    ]):
                        if (x1, y1, x2, y2) not in previous_vehicles:
                            vehicle_count += 1
                            print(f'Vehicle count: {vehicle_count}')
    
    
    ## 주차장 입구 bounding box
    cv2.rectangle(frame, top_left, bottom_right, (255, 0, 0), 2)


    cv2.imshow('Vehicle Tracking', frame)
    
    
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

    previous_vehicles = current_vehicles

cap.release()
cv2.destroyAllWindows()

print(f'count vehicle in bounding box: {vehicle_count}')