import cv2
import os



video_path = 'parking_entrance.mp4'
output_dir = 'test_entrance_img'


if not os.path.exists(output_dir):
    os.makedirs(output_dir)


cap = cv2.VideoCapture(video_path)
frame_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    
    if not ret:
        print("프레임 획득 X")
        break

    # 프레임을 화면에 표시
    cv2.imshow('Video', frame)

    # 키보드 입력 대기
    key = cv2.waitKey(1) & 0xFF
    
    # q 키 누름 저장
    if key == ord('q'):
        frame_filename = os.path.join(output_dir, f'test_entrance_frame_{frame_count:04d}.png')
        cv2.imwrite(frame_filename, frame)
        print(f'Saved {frame_filename}')
        frame_count += 1

    # ESC 키 탈출
    if key == 27:
        break


cap.release()
cv2.destroyAllWindows()
