import cv2
import numpy as np

# 定义输入数据
polygon_data = [
            {
                "polygons":  [
                    [0.0125, 0.5417], [0.0797, 0.3806], [0.2375, 0.3583], [0.4078, 0.3722], [0.4562, 0.4139],
                    [0.4656, 0.625], [0.5625, 0.95], [0.0656, 0.9722], [0.0172, 0.7583]
                ],
                "region_id": "dress shoes"
            },
            {
                "polygons": [
                    [0.0563, 0.3278], [0.0172, 0.4028], [0.0234, 0.6944], [0.0641, 0.95], [0.5734, 0.9389],
                    [0.4516, 0.5917], [0.4516, 0.2361], [0.2328, 0.1778]
                ],
                "region_id": "helmet"
            }

        ]


# 定义图片路径
image_path = r'D:\BaiduNetdiskDownload/2025-02-18T07_50_42_482419_2.jpg'  # 输入图片路径
output_path = r'D:\BaiduNetdiskDownload/2025-02-18T07_50_42_482419_2.jpg'  # 保存图片路径

# 读取图片
image = cv2.imread(image_path)
if image is None:
    raise FileNotFoundError(f"Image not found at {image_path}")

# 获取图片的尺寸
image_height, image_width = image.shape[:2]

# 定义颜色列表（不同多边形不同颜色）
colors = [(255, 0, 255), (124, 0, 124), (0, 0, 255), (255, 255, 0)]

# 绘制每个多边形
for i, data in enumerate(polygon_data):
    relative_coordinates = data["polygons"]
    region_id = data["region_id"]

    # 转换相对坐标为像素坐标
    pixel_coordinates = [
        (int(x * image_width), int(y * image_height)) for x, y in relative_coordinates
    ]

    # 将第一个点加到最后，形成闭合多边形
    pixel_coordinates.append(pixel_coordinates[0])

    # 绘制多边形
    color = colors[i % len(colors)]  # 循环使用颜色
    cv2.polylines(image, [np.array(pixel_coordinates)], isClosed=True, color=color, thickness=2)

    # 计算多边形的中心点位置
    center_x = int(np.mean([coord[0] for coord in pixel_coordinates[:-1]]))  # 排除闭合的最后一个点
    center_y = int(np.mean([coord[1] for coord in pixel_coordinates[:-1]]))

    # 在中心区域标注 region_id
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(image, region_id, (center_x - 40, center_y), font, 0.7, (0, 0, 255), 2)

# 保存结果图片
cv2.imwrite(output_path, image)

print(f"Polygons drawn and saved to {output_path}")
