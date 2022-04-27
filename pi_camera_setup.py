#https://maker.pro/raspberry-pi/tutorial/how-to-interface-pi-noir-v2-camera-with-raspberry-pi

from time import sleep
from picamera import PiCamera
camera = PiCamera() #initialise PiCamera object
camera.resolution = (1024, 768) #set resolution of image: width, height
camera.start_preview() 

#camera warm-up time
sleep(2)
camera.capture( ‘image.jpg’ ) #capture image
