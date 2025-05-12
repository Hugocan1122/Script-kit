from ultralytics import YOLO

# Load a model
if __name__ == '__main__':
    model = YOLO("yolov8n.pt")  # build from YAML and transfer weights

    # Train the model
    results = model.train(data=r"E:\pythonProject\ultralytics-8.1.0\ultralytics\cfg\datasets\door_detect.yaml", epochs=10, imgsz=640, batch=4)
