from gpiozero import MotionSensor
from picamera import PiCamera

pir = MotionSensor(4)
camera = PiCamera()
filename = "intruder.h264"

while True:
    pir.wait_for_motion()
    print("Motion detected!")
    camera.start_preview()
    pir.wait_for_motion()
    camera.stop_preview()