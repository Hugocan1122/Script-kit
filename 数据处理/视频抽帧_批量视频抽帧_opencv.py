import cv2, os, glob


'''
# 单个视频

frame_interval = 15

# 视频文件路径
video_path = r'E:/pythonProject/work/video_test/door_xianchang/west_192.168.1.203_19_2024073117480553.mp4'
# 输出文件夹路径
output_folder = 'E:\pythonProject\work\out_images_west'

# 确保输出文件夹存在
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 打开视频文件
cap = cv2.VideoCapture(video_path)

# 检查视频是否成功打开
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

frame_rate = cap.get(cv2.CAP_PROP_FPS)  # 获取视频的帧率
current_frame = 0
frame_num = 0
while True:
    # 读取一帧
    ret, frame = cap.read()

    # 如果正确读取帧，ret为True
    if not ret:
        print("Reached end of video or cannot fetch frame.")
        break
    if current_frame % frame_interval == 0:
        # 保存帧为图片
        frame_num += 1
        frame_name = os.path.join(output_folder, video_path.split("/")[-1][:-4] + '_' +f'frame_{frame_num}.jpg')
        cv2.imwrite(frame_name, frame)
        print(f'Saved {frame_name}')
    # frame_name = os.path.join(output_folder, video_path.split("/")[-1][:-4] + f'frame_{current_frame}.jpg')
    # cv2.imwrite(frame_name, frame)
    # print(f'Saved {frame_name}')


    current_frame += 1


# 释放视频捕获对象
cap.release()
print("Done!")
'''
# 批量视频
def cut_one_video(video_path, output_folder):
    frame_interval = 20

    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 打开视频文件
    cap = cv2.VideoCapture(video_path)

    # 检查视频是否成功打开
    if not cap.isOpened():
        print("Error: Could not open video.")
        exit()

    frame_rate = cap.get(cv2.CAP_PROP_FPS)  # 获取视频的帧率
    current_frame = 0
    frame_num = 0
    while True:
        # 读取一帧
        ret, frame = cap.read()

        # 如果正确读取帧，ret为True
        if not ret:
            print("Reached end of video or cannot fetch frame.")
            break
        if current_frame % frame_interval == 0:
            # 保存帧为图片
            frame_num += 1
            frame_name = os.path.join(output_folder, video_path.split("/")[-1][:-4] + '_' + f'frame_{frame_num}.jpg')
            cv2.imwrite(frame_name, frame)
            print(f'Saved {frame_name}')
        # frame_name = os.path.join(output_folder, video_path.split("/")[-1][:-4] + f'frame_{current_frame}.jpg')
        # cv2.imwrite(frame_name, frame)
        # print(f'Saved {frame_name}')
        current_frame += 1

    # 释放视频捕获对象
    cap.release()
    print("Done!")


video_need_to_cut_dir = r'D:\dataset\wheel_resister\video/*.mp4'
save_dir = r'D:\dataset\wheel_resister\new_images'
ls = glob.glob(video_need_to_cut_dir)
correct_ls = []
for i in ls:
    correct_ls.append(i.replace('\\', '/'))
# ls = ['D:/dataset/cz_20241025_data_add/lift_video/192.168.66.212_01_20241025173621345.mp4', 'D:/dataset/cz_20241025_data_add/lift_video/192.168.66.212_02_20241025174333348.mp4']
num = 0
for i in correct_ls:
    cut_one_video(i, save_dir)
    num += 1
    print(i)
    print(num, '/', len(ls))
