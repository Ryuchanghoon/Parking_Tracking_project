import easyocr
import cv2
import numpy as np

def extract_text_from_image(image_path):
    reader = easyocr.Reader(['ko'], gpu=False)
    img = cv2.imread(image_path)
    text = reader.readtext(img, detail=0)
    return text



def track_text_in_video(video_path, texts):
    cap = cv2.VideoCapture(video_path)
    tracker = cv2.TrackerKCF_create() ## 
    
    ret, frame = cap.read()
    if not ret:
        print("비디오를 읽을 수 없습니다.")
        return
    
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    
    reader = easyocr.Reader(['ko'], gpu=False) # 여러 언어 한꺼번에 설정 가능.
    result = reader.readtext(gray_frame)


    bbox = None
    for res in result:
        detected_text, bbox_coords = res[1], res[0]
        if detected_text in texts:
            bbox = cv2.boundingRect(np.array(bbox_coords))
            break

    if bbox is None:
        print("추적할 텍스트를 찾을 수 없습니다.")
        return
    
  
    tracker.init(frame, bbox)

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        
        success, bbox = tracker.update(frame)
        
        if success:
          
            p1 = (int(bbox[0]), int(bbox[1]))
            p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
            cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)
        
        cv2.imshow('Tracking', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

image_file = 'test_license_plate.png'
video_file = 'tracking_ocr_edit.mp4'


texts = extract_text_from_image(image_file)
print("추출 텍스트:", texts)


track_text_in_video(video_file, texts)