import os, csv
from ultralytics import YOLO
from sklearn.metrics import confusion_matrix, precision_recall_fscore_support
import numpy as np
np.set_printoptions(threshold=np.inf)


# 加载模型
model_helmet = YOLO(r'D:\dataset\01_all_models/model.pt')
print(model_helmet.names)

# 数据集文件夹路径
dataset_path = r"D:\dataset"
# 保存的csv文件路径
save_path = r"files/confusion_matrix_with_labels_and_metrics.csv"

model_classes = {
    0: 'CeJiaLiZhuMoHaoBanPoSun',
    1: 'CeJiaZheDuan',
    2: 'CheLunLunWangQueSun',
    3: 'CheLunLunYuanQueSun',
    4: 'ChengZaiAnCuoWei',
    5: 'DangJianLuoMuDiuShi',
    6: 'DangJianLuoMuSongDong'
}

reversed_class_name = {v: k for k, v in model_classes.items()}

dim = len(model_helmet.names)
confusion_matrix = np.zeros((dim, dim), dtype=int)

# 获取类别名称
class_names = list(os.listdir(dataset_path))  # 子文件夹名即类别名
class_names.sort()  # 确保顺序一致

# 初始化存储真实标签和预测标签的列表
y_true = []
y_pred = []
predict_class_dict = {}  # 存放class_idx和class_name的对应关系
# 遍历每个类别的文件夹
for dir_idx, class_name in enumerate(class_names):
    predict_class_dict[str(dir_idx)] = class_name
    class_index = reversed_class_name.get(class_name)  # 获取类别所在的序号 对应当前混淆矩阵的行和列
    class_folder = os.path.join(dataset_path, class_name)
    for image_name in os.listdir(class_folder):
        # 图片路径
        image_path = os.path.join(class_folder, image_name)
        if not image_path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            continue

        # 预测单张图片
        prediction = model_helmet.predict(image_path)[0]
        predicted_class_index = prediction.probs.top1  # 获取预测类别索引

        confusion_matrix[reversed_class_name.get(class_name)][predicted_class_index] += 1

print(confusion_matrix)

# 对混淆矩阵做后处理计算指标
def calculate_metrics(matrix):
    n_classes = matrix.shape[0]
    total_samples = np.sum(matrix)
    metrics = {}

    for i in range(n_classes):
        TP = matrix[i, i]
        FP = np.sum(matrix[:, i]) - TP
        FN = np.sum(matrix[i, :]) - TP
        TN = total_samples - (TP + FP + FN)

        precision = TP / (TP + FP) if (TP + FP) > 0 else 0
        recall = TP / (TP + FN) if (TP + FN) > 0 else 0
        specificity = TN / (TN + FP) if (TN + FP) > 0 else 0

        metrics[i] = {
            "Precision": precision,
            "Recall": recall,
            "Specificity": specificity,
        }

    return metrics

results = calculate_metrics(confusion_matrix)

class_names = [model_classes[i] for i in range(len(model_classes))]
# 打开 CSV 文件以写入
with open(save_path, mode="w", newline="") as file:
    writer = csv.writer(file)

    # 写入第一行（包含类别名称和指标名称）
    header = [""] + class_names + ["Precision", "Recall", "Specificity"]
    writer.writerow(header)

    # 写入每一行（类别名称 + 矩阵数据 + 指标）
    for i, row in enumerate(confusion_matrix):
        metrics = results[i]
        writer.writerow(
            [class_names[i]] + row.tolist() +
            [f"{metrics['Precision']:.2f}", f"{metrics['Recall']:.2f}", f"{metrics['Specificity']:.2f}"]
        )

print("混淆矩阵及其指标已成功写入到 confusion_matrix_with_labels_and_metrics.csv 文件中。")