import cv2
import numpy as np

# 图像路径
img_pth = r'D:\BaiduNetdiskDownload/1741065394423.png'
# 输出路径
out_pth = r'D:\BaiduNetdiskDownload/' + img_pth.split('/')[-1]
print(out_pth)

# 加载原始图像
image = cv2.imread(img_pth)
# 获取原始图像的尺寸
height, width = image.shape[:2]

# 设置缩放比例（例如缩小到原图的50%）
scale_factor = 0.5
resized_image = cv2.resize(image, (int(width * scale_factor), int(height * scale_factor)))

# 存储点击点的列表
points = []

# 回调函数，用于处理鼠标点击事件
def click_event(event, x, y, flags, param):
    global points
    if event == cv2.EVENT_LBUTTONDOWN:
        # 将点击的坐标按缩放比例调整
        x_resized = int(x / scale_factor)
        y_resized = int(y / scale_factor)
        points.append([x_resized, y_resized])
        # 在缩放后的图像上显示当前点击的点
        cv2.circle(resized_image, (x, y), 5, (0, 0, 255), -1)
        cv2.imshow("Resized Image", resized_image)

# 显示缩放后的图像并等待点击
cv2.imshow("Resized Image", resized_image)
cv2.setMouseCallback("Resized Image", click_event)

while True:
    # 按下 'q' 键退出
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

# 计算相对坐标并打印
relative_coords = [[round(x / width, 4), round(y / height, 4)] for [x, y] in points]
print("Relative Coordinates:", relative_coords)

# 在原始图像上绘制红色线条，连接点击的点
for i in range(len(points)):
    start_point = tuple([points[i][0], points[i][1]])  # 使用原始坐标
    end_point = tuple([points[(i + 1) % len(points)][0], points[(i + 1) % len(points)][1]])
    cv2.line(image, start_point, end_point, (0, 255, 255), 2)

# 显示绘制的区域
cv2.imshow("Image with Region", image)

# 保存原始尺寸的图像
cv2.imwrite(out_pth, image)

cv2.waitKey(0)
cv2.destroyAllWindows()
