from ultralytics import YOLO

# Load a model

model = YOLO("E:\pythonProject\work_team\TFDS\TFDS_Detect\models\detect_one_stage\extra32_default.pt")  # load a custom trained model

# Export the model
model.export(format="onnx", dynamic=True)