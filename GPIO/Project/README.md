How the code works
First you import the necessary libraries; as we’ve said, the program uses the picamera library to control the camera. The gpiozero library contains classes to control the pushbutton and the motion sensor: Button and MotionSensor. The sleep method allows us to deal with delays, and the pause method is used to handle interrupts.

from gpiozero import Button, MotionSensor
from picamera import PiCamera
from time import sleep
from signal import pause
Then, you create objects to refer to the pushbutton, the PIR motion sensor, and the camera. The pushbutton is on GPIO 2 and the motion sensor on GPIO 4.

button = Button(2)
pir = MotionSensor(4)
camera = PiCamera()
Then, initialize the camera with camera.start_preview().

camera.start_preview()
Depending on how your camera is oriented, you might also need to rotate it 180 degrees so that it doesn’t take the photos upside down.

camera.rotation = 180
Next, you initialize an i variable that starts at 0.

i = 0
Then, we create the stop_camera() and the take_photo() functions that will be called later in the code.

The take_photo() function, will use the i variable to count and number the images, incrementing the number in the filename by one with each picture taken.

def take_photo():
  global i
  i = i + 1
  camera.capture('/home/pi/Desktop/image_%s.jpg' % i)
  print('A photo has been taken')
  sleep(10)
To take and save a photo you use the camera.capture() method, specifying the directory you want to save the image to inside the parentheses. In this case, we’re saving the images in the Desktop folder and naming the images image_%s.jpg, where %s is replaced with the number we incremented earlier in i.

If you want to save your files to a different folder, replace this directory with the path to your chosen folder. You then impose a 10-second delay, meaning the camera takes photos at 10-second intervals for as long as the PIR sensor detects movement. Feel free to increase or decrease the delay time, but be careful to not overload the Pi with tons of images by making the delay time too small.

The stop_camera() function stops the camera with the camera.stop_preview() method.

def stop_camera():
  camera.stop_preview()
  #exit the program
  exit()
This function stops the camera preview and exits the program. The exit() function pops up a window asking if you want to close the program; to close it, just click OK.

Finally, you define that when the pushbutton is pressed, the cameras stops.

button.when_pressed = stop_camera
Finally, you tell the camera to take a photo by triggering the take_photo() function when motion is detected.

pir.when_motion = take_photo
The pause() at the end of the code keeps your program running so that interrupts can be detected.

Demonstration
If your’re using Python IDLE to write your code, press F5 or go to Run > Run Module to run the script. While the script is running, you should see a preview of what the camera sees on your screen. To shut down the camera preview, press the pushbutton and click OK in the window that pops up.

Alternatively, in the Terminal window you can type:

pi@raspberrypi:~ $ python3 burglar_detector.py
Congratulations, you project is ready to detect motion and take some photos. You can place this project in a strategic place and come back later to check any saved photos. The following figure shows a photo taken by this project.