import cv2


def draw_bounding_box(event, x, y, flags, param):
    global x1, y1, x2, y2, drawing

    if event == cv2.EVENT_LBUTTONDOWN: 
        drawing = True
        x1, y1 = x, y

    elif event == cv2.EVENT_MOUSEMOVE: 
        if drawing:
            img_copy = img.copy()
            cv2.rectangle(img_copy, (x1, y1), (x, y), (0, 255, 0), 2)
            cv2.imshow("Image", img_copy)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        x2, y2 = x, y
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.imshow("Image", img)
        print(f"Bounding box coordinates: ({x1}, {y1}), ({x2}, {y2})")


drawing = False
x1, y1, x2, y2 = -1, -1, -1, -1


img = cv2.imread('test_entrance_img/test_entrance_frame_0000.png')

cv2.namedWindow("Image")
cv2.setMouseCallback("Image", draw_bounding_box)

while True:
    cv2.imshow("Image", img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"): 
        break

cv2.destroyAllWindows()

## Bounding box coordinates: (146, 151), (672, 449)