TARGET_LOCK_THRESHOLD_PIXELS_HORIZONTAL = 75
TARGET_LOCK_THRESHOLD_PIXELS_VERTICAL = 40
IMAGE_WIDTH = 1024      ## default == 1024x768, yolo == 256x192
IMAGE_HEIGHT =768       ## 640x480
YOLO_IMAGE_WIDTH = 512  ## 512x384
YOLO_IMAGE_HEIGHT =384
CENTER_X, CENTER_Y = IMAGE_WIDTH // 2, IMAGE_HEIGHT // 2
BB_COLOR = (255, 0, 255)
CLASS_NAMES = [0] ## Yolo detect, person only

## Step motor movement constants
LEFT = 0
RIGHT = 1
UP = 0
DOWN = 1
IDLE = None
BACKWARD = 0
FORWARD = 1

## GPIO pins
TRIGGER_PIN = 14
ECHO_PIN = 15
DIR_PIN_HOR = 20
DIR_PIN_VER = 5
STEP_PIN_HOR = 21
STEP_PIN_VER = 6

## Pin Timers
TRIGGER_TIME = 0.00001
LIDAR_SCANNER_DURATION = 0.0055

## Constants 
LIDAR_MAX_HZ = 1000
LIDAR_SCAN_ANGLE = 90

MOTOR_HAT_ANGLES={
	"1": 1.8,
	"2": 0.9,
	"4": 0.45,
	"8": 0.225,
	"16": 0.1125,
	"32": 0.05625,
	"64": 0.028125,
	"128": 0.0140625,
}
