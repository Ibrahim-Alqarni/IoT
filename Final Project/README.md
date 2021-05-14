### To convert video.mp4 to video.gif:
```sh
pi@raspberrypi:~ $ sudo apt install ffmpeg
```
```sh
pi@raspberrypi:~ $ ffmpeg -i the_video.mp4 the_video.gif
```
![](Camera/video.gif)

### For sending the Video .mp4 to the email:

#### In line 51, to send the video through the email: 
In the first parameter " " should be the Gamai address and the second parameter " " should be the Google App Password.

```sh
51    server.login("..1..@gmail.com","..2..")
``` 
```sh
52    server.sendmail(".1.@gmail.com", ".2.@gmail.com", msg.as_string())
``` 
