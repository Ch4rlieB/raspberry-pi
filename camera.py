import picamera
import time
import os

# get instance of PiCamera
camera = picamera.PiCamera()

# camera settings for resolution, horizontal flip, vertical flip
camera.resolution = '1080p'
camera.hflip = True
camera.vflip = True

time.sleep(1*60)

# infinite loop
while True:

  # picture path settings
  capture_time = time.strftime("%Y-%m-%d-%H%M%S")
  picture_path = '/var/www/html/pics/image' + capture_time + '.jpg'

  # capturing picture
  camera.capture(picture_path)

  # sleep 10 minutes before capturing next picture
  time.sleep(10*60)
