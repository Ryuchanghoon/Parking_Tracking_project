import numpy as np
import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img


input_image_path = 'custom_data/0/0.png'
output_dir = 'custom_data/0'
os.makedirs(output_dir, exist_ok=True)


img = load_img(input_image_path)
x = img_to_array(img)
x = np.expand_dims(x, axis=0)


datagen = ImageDataGenerator(
    rotation_range=50,              # 각도 변환
    width_shift_range=0.1,          # 가로 이동
    height_shift_range=0.1,         # 세로 이동
    shear_range=50,                 # 전단 변환
    zoom_range=[0.5, 1.5],          # 확대/축소 변환
    brightness_range=[0.1, 2.0],    # 밝기 조정
    channel_shift_range=150,        # 채널 이동
    fill_mode='constant',           # 채우기 모드
    cval=0,                         # 채우기 값
    horizontal_flip=False,           # 좌우 반전
    vertical_flip=False,            # 상하 반전
    rescale=1./255,                 # 스케일링(정규화 0~1 값)
    preprocessing_function=lambda x: x + np.random.normal(0, 0.05, x.shape)  # 노이즈
)


i = 0
for batch in datagen.flow(x, batch_size=1, save_to_dir=output_dir, save_prefix='aug', save_format='png'):
    i += 1
    if i >= 200:
        break 

print('Done')