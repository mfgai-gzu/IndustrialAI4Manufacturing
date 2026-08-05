from ultralytics import YOLO

# 加载官方预训练YOLOv8n模型
model = YOLO("yolov8n.pt")
print("✅ Ultralytics与PyTorch环境连通正常，项目开发就绪")