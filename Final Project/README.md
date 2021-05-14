## In motion_video_alert.py
### From line 1 to 12 cover required imports to make the script work:
```sh
1   from gpiozero import MotionSensor
2   from picamera import PiCamera
3   from datetime import datetime
4   from email.mime.multipart import MIMEMultipart
5   from email.mime.base import MIMEBase
6   from email.mime.text import MIMEText
7   import email.encoders
8   import smtplib
9   import os
10  import email
11  import sys
12  import time
``` 
### From line 14 to 18 establish important variables needed to make the camera and PIR sensor work properly:
```sh
14   camera = PiCamera()
15   pir = MotionSensor(4)
16   camera.rotation = 180 # delete or adjust to 90, 180, or 270 accordingly
17   h264_video = ".h264" 
18   mp4_video = ".mp4"
``` 
### Line 20 introduces some basic logic by creating a while loop:
```sh
20   while True:
``` 
### From line 23 to 30 represent the sensor detecting motion. Once motion is detected, the camera will begin recording video. Once the sensor registers the absence of motion, the camera will stop recording, leaving us with an h264 video file that is conveniently named with a month-day-year-hour-minute-second format:
```sh
23      pir.wait_for_motion()
24      video_name = datetime.now().strftime("%m-%d-%Y_%H.%M.%S")
25      camera.start_recording(video_name + h264_video)
26      pir.wait_for_no_motion()
27      camera.stop_recording()
28      os.system("MP4Box -add " + video_name + h264_video + " " + video_name + mp4_video)
29      os.system("rm " + video_name + h264_video) # delete h264 file
30      footage = video_name + mp4_video
``` 
### From line 33 to 39 are preparing the email we’re about to send:
```sh
33      f_time = datetime.now().strftime("%A %B %d %Y @ %H:%M:%S")
34      msg = MIMEMultipart()
35      msg["Subject"] = f_time
36      msg["From"] = "...@gmail.com"
37      msg["To"] = "...@gmail.com"
38      text = MIMEText("WARNING! Motion Detected!")
39      msg.attach(text)
``` 

### For sending the Video .mp4 to the email you have to do two steps in motion_video_alert.py:

#### First step, you need to prepare the Email.
##### To do that: 
In line 36: 
The first email is the sender email 
```sh
36    msg["From"] = "...@gmail.com"
``` 
In line 37: 
The second email is the receiver email
```sh
37    msg["To"] = "...@gmail.com"
``` 
### From line 49 to 53 describe how to access a Gmail account and email everything:
```sh
49     server = smtplib.SMTP("smtp.gmail.com:587")
50     server.starttls()
51     server.login("your_gmail_login","your_gmail_password")
52     server.sendmail("your_address@gmail.com", "to_address@gmail.com", msg.as_string())
53     server.quit()
``` 
Second step, you need to access to a Gmail Address Account to send the video. 
##### To do that: 
In line 51: first parameter "" should be the Gamai Address, and the second parameter "" should be the Google App Password.
```sh
51    server.login("....@gmail.com","....")
``` 
In line 52: first parameter "" should be Sender Gmail Address, and the second parameter "" should be Receiver Gmail Address
```sh
52    server.sendmail("....@gmail.com", "....@gmail.com", msg.as_string())
``` 
### From line 42 to 46 attach the mp4 video:
```sh
42     part = MIMEBase("application", "octet-stream")
43     part.set_payload(open(footage, "rb").read())
44     email.encoders.encode_base64(part)
45     part.add_header("Content-Disposition", "attachment; filename= %s" % os.path.basename(footage))
46     msg.attach(part)
``` 
### Line 56 describes a simple Linux commands that deletes the mp4 (we already deleted the original h264 in line 29):
```sh
56    os.system("rm " + footage)
``` 
### To convert video.mp4 to video.gif:
```sh
pi@raspberrypi:~ $ sudo apt install ffmpeg
```
```sh
pi@raspberrypi:~ $ ffmpeg -i the_video.mp4 the_video.gif
```
![](Camera/video.gif)
