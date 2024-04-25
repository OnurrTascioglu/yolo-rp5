import cv2
import time
import threading
import numpy as np
from ultralytics import YOLO
from utils.constants import *
from controllers.step_controller import StepController

# model = YOLO("yolo-Weights/yolov8n.pt")
# model = YOLO("yolo-Weights/yolov8n_float32.tflite")
# model = YOLO("yolo-Weights/yolov8n_float16.tflite")
# model = YOLO("yolo-Weights/yolov8n_int8.tflite")
# model = YOLO("yolo-Weights/yolov8n_integer_quant.tflite")
model = YOLO("yolo-Weights/yolov8n_full_integer_quant.tflite")
time.sleep(15)

## R&D models
# model = YOLO("yolo-Weights/yolov8-n-voc_coco-pruned48.onnx")
# model = YOLO("yolo-Weights/yolov8-n-coco-base_quantized.onnx")
# model = YOLO("yolo-Weights/yolov8-n-voc_coco-pruned48_quantized.onnx")

def capture_and_set(width, height):
    cap = cv2.VideoCapture(0)
    cap.set(3, width)
    cap.set(4, height)
    return cap

def get_object_midpoints(x1, y1, x2, y2):
    return (x1 + x2) // 2, (y1 + y2) // 2

cap = capture_and_set(IMAGE_WIDTH, IMAGE_HEIGHT)

step_controller = StepController()
motor_thread = threading.Thread(target=step_controller.move)
motor_thread.start()

while True:
    try:
        start = time.time()
        success, img = cap.read()
        if img is None:
            cap = capture_and_set(IMAGE_WIDTH, IMAGE_HEIGHT)

        results = model.predict(img, stream=True, save=False, classes=CLASS_NAMES,imgsz = (YOLO_IMAGE_WIDTH, YOLO_IMAGE_HEIGHT), verbose=False)

        # coordinates
        for r in results:
            boxes = r.boxes
            if len(boxes) != 1:
                step_controller.set_directions(IDLE, IDLE)
                continue
            box = boxes[0]
            # bounding box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) # convert to int values

            ## yolo origin points (0,0) is top-letf of the image
            mid_x, mid_y = get_object_midpoints(x1, y1, x2, y2)
            direction_x, direction_y = StepController.get_stepper_next_directions(mid_x, mid_y)
            step_controller.set_directions(direction_x, direction_y)

            # put box in cam
            cv2.rectangle(img, (x1, y1), (x2, y2), BB_COLOR, 3)

        end = time.time()
        fps = int(1/(end-start))
        if fps < 5:
            step_controller.set_directions(IDLE, IDLE)
        cv2.putText(img, str(fps), (7, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (100, 255, 0), 3, cv2.LINE_AA)

        cv2.imshow('Webcam', img)
        if cv2.waitKey(1) == ord('q'):
            step_controller.set_run_flag(False)
            step_controller.release()
            cap.release()
            cv2.destroyAllWindows()
            motor_thread.join()
            break
    except Exception as e:
        print(e)
