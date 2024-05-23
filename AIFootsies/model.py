from ultralytics import YOLO

# Build a YOLOv9c model from pretrained weight
model = YOLO('yolov8n.yaml')

# Display model information (optional)
model.info()

# Train the model on the COCO8 example dataset for 100 epochs
results = model.train(data='datasets/data.yaml', epochs=10, imgsz=640)

# Run inference with the YOLOv9c model on the 'bus.jpg' image
results = model('datasets/train/images/frame-3_png.rf.dd13cda6c304c4b6af6296ff369c09ed.jpg')