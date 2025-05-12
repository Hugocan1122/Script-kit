from sahi.predict import predict
from sahi import AutoDetectionModel
from sahi.predict import get_sliced_prediction
from IPython.display import Image

yolov8_model_path = "/mnt/T4/PycharmProjects/yolov8/logo_detect_test_yolov8/weight/best.pt"  # 读取模型的路径
mode = 0  # 0:单张 1:批量

pic_filename = "/mnt/T4/PycharmProjects/yolov8/logo_detect_test_yolov8/images/test_2.png"  # 推理单张图片的路径
pic_save_dir = "images_infer_result/"
pic_dir = "/mnt/T4/PycharmProjects/yolov8/logo_detect_test_yolov8/images"  # 批量处理的文件夹名


if mode == 0:
    # 单张图片推理 结果保存在pic_save_dir下
    detection_model = AutoDetectionModel.from_pretrained(
        model_type="yolov8",
        model_path=yolov8_model_path,
        confidence_threshold=0.5,  # 置信度阈值
        device="cuda:0",
    )

    result = get_sliced_prediction(
        pic_filename,
        detection_model,
        slice_height=256,
        slice_width=256,
        overlap_height_ratio=0.2,
        overlap_width_ratio=0.2,
    )
    result.export_visuals(export_dir=pic_save_dir, file_name="result1",hide_labels=True, hide_conf=True)

elif mode == 1:
    # 批量推理 结果保存在runs下
    result = predict(
        model_type="yolov8",
        model_path=yolov8_model_path,
        model_device="cuda:0'",
        model_confidence_threshold=0.4,  # 置信度阈值
        source=pic_dir,
        slice_height=256,
        slice_width=256,
        overlap_height_ratio=0.2,
        overlap_width_ratio=0.2,
        visual_text_size=2,
        visual_text_thickness=1,
        visual_hide_labels=True,  # 是否隐藏置信度和labels
        visual_hide_conf=True
    )

