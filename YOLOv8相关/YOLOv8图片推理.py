'''
官方推理

from ultralytics import YOLO

model = YOLO(r'D:\dataset\01_all_models/best_rope_detect.pt')
print(model.names)
print(model.names[model.predict(r"E:\pythonProject\ultralytics-8.1.0\1729741486735.jpg")[0].probs.top1])
'''


# 遍历推理 用于后处理
from ultralytics import YOLO
import time, os, cv2

# Load a pre-trained YOLO model
model = YOLO("/media/can/pythonprojects/ultralytics-8.1.0/yolov8n.pt")
# model = YOLO("/media/hugocan/can/pythonprojects/ultralytics-8.3.85/yolo11n.pt")
# 设置图片所在文件夹路径
image_folder = "/media/can/dataset/test_pic_500"

# 获取文件夹中所有图片的路径
image_paths = [os.path.join(image_folder, f) for f in os.listdir(image_folder) if f.endswith(('.jpg', '.png', '.jpeg'))]  # 只获取图片文件

# 初始化计时器
start_time = time.time()

# 遍历每一张图片进行处理
for image_path in image_paths:
    # 使用cv2读取图片
    img = cv2.imread(image_path)
    # 将BGR图像转换为RGB（YOLO模型通常使用RGB格式）
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # 每次传入一张图片进行预测
    model.predict(image_path)

# 结束计时
end_time = time.time()

# 计算推理时间并转换为毫秒
inference_time_ms = (end_time - start_time) * 1000
inference_time_seconds = end_time - start_time

# 计算 FPS
total_images = len(image_paths)  # 遍历的图片总数
fps = total_images / inference_time_seconds

# 打印推理时间
print(f"========== Inference Time: {inference_time_ms:.2f} ms ==== FPS: {fps:.2f}")
