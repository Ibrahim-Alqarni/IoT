### To convert video.mp4 to video.gif:
```sh
pi@raspberrypi:~ $ sudo apt install ffmpeg
```
```sh
pi@raspberrypi:~ $ ffmpeg -i the_video.mp4 the_video.gif
```
![](Camera/video.gif)

### For sending the Video .mp4 to the email you have to do two steps:

#### To send the video through the email: 
First, you need to access to a Gmail address. 

##### To do that in motion_video_alert.py: 
In line 51: first parameter "" should be the Gamai Address, and the second parameter "" should be the Google App Password.
```sh
51    server.login("....@gmail.com","....")
``` 
In line 52: first parameter "" should be Sender Gmail Address, and the second parameter "" should be Receiver Gmail Address
```sh
52    server.sendmail("....@gmail.com", "....@gmail.com", msg.as_string())
``` 
