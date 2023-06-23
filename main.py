import torch.cuda
from ultralytics.yolo.engine.model import YOLO

model = YOLO("runs/detect/train12/weights/best.pt")
model2 = YOLO("yolov8m.pt")


def predict():
    results = model.predict(source="C:\\Users\Dev_ARAF\Desktop\\20230530_100124.jpg", device=1, stream=False, save=True)
    #for result in results:
     #print(result.boxes)  # xa ya xb yb % class


def exportONNX():
    model.export(format="onnx", opset=10)


def learning():
    model2.train(data="custom.yaml", batch=16, epochs=33 ,
                 device=1, plots=True, lr0=0.008, lrf=0.008)


if __name__ == '__main__':
    print(torch.cuda.get_device_name())
    print(torch.__version__)
    print(torch.version.cuda)
    #learning()
    predict()
    #exportONNX()