import cv2


video_path = 'parking_entrance.mp4'

# coordinate for check bounding box
top_left = (146, 151)
bottom_right = (672, 400) # y값 범위 좁히고 싶음 여기 수정.


cap = cv2.VideoCapture(video_path)



frame_width = int(cap.get(3)) # 읽힌 동영상 width
frame_height = int(cap.get(4)) # 읽힌 동영상 height


print(f'frame width: {frame_width}')
print(f'frame height: {frame_height}')

while cap.isOpened():
    ret, frame = cap.read()
    
    if not ret:
        break
    
    cv2.rectangle(frame, top_left, bottom_right, (255, 0, 0), 2)
    
    
    cv2.imshow('Frame', frame)
    
    
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()