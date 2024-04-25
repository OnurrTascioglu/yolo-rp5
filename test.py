import cv2
import time

cap = cv2.VideoCapture(0)


while cap.isOpened():
    start = time.time()
    flags, frame = cap.read()
    cv2.imshow('img', frame)

    end = time.time()
    fps = 1/(end-start)
    fps = str(int(fps))
    cv2.putText(frame, fps, (7, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (100, 255, 0), 3, cv2.LINE_AA)

    cv2.imshow('img', frame)
    if cv2.waitKey(1) == ord('q'):
                cap.release()
                cv2.destroyAllWindows()
                break

cap.release()
cv2.destroyAllWindows()
