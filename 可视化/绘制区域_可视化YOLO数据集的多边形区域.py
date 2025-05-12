import os
import cv2
import numpy as np

# 设置文件夹路径
images_dir = 'D:\dataset\yx_region_foreign_object/images'
labels_dir = 'D:\dataset\yx_region_foreign_object/labels'
output_dir = r'D:\dataset\yx_region_foreign_object\region_result'
classes_file = 'D:\dataset\yx_region_foreign_object/classes.txt'

# 读取类别名
with open(classes_file, 'r') as f:
    classes = [line.strip() for line in f.readlines()]

# 确保输出文件夹存在
os.makedirs(output_dir, exist_ok=True)

# 获取所有图片文件
image_files = [f for f in os.listdir(images_dir) if f.endswith(('.jpg', '.png', '.jpeg'))]

# 遍历每张图片
for image_file in image_files:
    # 读取对应的标签文件
    label_file = os.path.join(labels_dir,
                              image_file.replace('.jpg', '.txt').replace('.png', '.txt').replace('.jpeg', '.txt'))

    if not os.path.exists(label_file):
        print(f'Warning: Label file {label_file} does not exist. Skipping {image_file}.')
        continue

    # 读取图片
    image = cv2.imread(os.path.join(images_dir, image_file))
    height, width, _ = image.shape

    # 读取标签文件
    with open(label_file, 'r') as f:
        labels = f.readlines()

    # 遍历标签文件中的每一行（每个标签对应一个区域）
    for label in labels:
        label_parts = label.strip().split()
        class_id = int(label_parts[0])

        # 获取该类别的名称
        class_name = classes[class_id] if class_id < len(classes) else 'Unknown'

        # 获取归一化后的坐标
        coords = np.array([float(coord) for coord in label_parts[1:]])

        # 将归一化坐标转换为图片中的像素坐标
        polygon = coords.reshape(-1, 2) * [width, height]

        # 绘制多边形
        polygon = polygon.astype(int)
        cv2.polylines(image, [polygon], isClosed=True, color=(0, 255, 0), thickness=2)

        # 在区域内写上类别名
        cv2.putText(image, class_name, tuple(polygon[0]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    # 保存绘制后的图片
    output_path = os.path.join(output_dir, image_file)
    cv2.imwrite(output_path, image)
    print(f'Saved image with labels: {output_path}')

print('Processing complete.')
