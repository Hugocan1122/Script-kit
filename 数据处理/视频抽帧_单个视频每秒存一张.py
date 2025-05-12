import cv2

# 设置视频路径
video_path = r'E:/pythonProject/work/test_dress_detect/192.168.1.201_32_20241120155155197.mp4'
output_folder = 'bt_dress_1120'

# 打开视频文件
cap = cv2.VideoCapture(video_path)

# 获取视频的帧率
fps = int(cap.get(cv2.CAP_PROP_FPS))

# 确保输出文件夹存在
import os

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

frame_count = 0
while True:
    # 读取视频帧
    ret, frame = cap.read()
    if not ret:
        break

    # 如果当前帧是每秒的第一帧，保存图片
    if frame_count % fps == 0:
        frame_time = frame_count // fps
        filename = os.path.join(output_folder, video_path.split("/")[-1][:-4] + f'1107_frame_{frame_time}.jpg')
        cv2.imwrite(filename, frame)
        print(f'Saved {filename}')

    frame_count += 1

# 释放视频对象
cap.release()
print('完成!')
