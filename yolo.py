import cv2
import math
import time
from ultralytics import YOLO

classNames = [0]
model = YOLO("yolo-Weights/yolov8n.pt")


def capture_and_set(width, height):
    cap = cv2.VideoCapture(0)
    cap.set(3, width)
    cap.set(4, height)
    return cap

cap = capture_and_set(640,480)
while True:
    try:
        start = time.time()
        success, img = cap.read()
        if img is None:
            cap = capture_and_set(640,480)
        results = model.predict(img, stream=True, save=False, classes=classNames,imgsz = (256, 256))
        cv2.imshow('Webcam', img)

        # coordinates
        for r in results:
            boxes = r.boxes

            for box in boxes:
                # bounding box
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) # convert to int values

                # put box in cam
                cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

                confidence = math.ceil((box.conf[0]*100))/100

                cls = int(box.cls[0])

                # object details
                org = [x1, y1]
                font = cv2.FONT_HERSHEY_SIMPLEX
                fontScale = 1
                color = (255, 0, 0)
                thickness = 2

                try:
                    cv2.putText(img, classNames[cls], org, font, fontScale, color, thickness)
                except:
                    pass

        end = time.time()
        fps = 1/(end-start)
        fps = int(fps)
        fps = str(fps)
        cv2.putText(img, fps, (7, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (100, 255, 0), 3, cv2.LINE_AA)

        cv2.imshow('Webcam', img)
        if cv2.waitKey(1) == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            break
    except Exception as e:
        print(e)