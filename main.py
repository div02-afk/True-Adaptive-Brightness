from PIL import ImageGrab
import numpy as np
import wmi
import time
import win32gui
import win32con
import win32process
# Connect to WMI
c = wmi.WMI(namespace='wmi')

# Get brightness
def get_brightness():
    brightness = c.WmiMonitorBrightness()[0].CurrentBrightness
    return brightness
def set_brightness(brightness):
    brightness = min(max(brightness, 0), 100)  # Ensure brightness is within valid range (0-100)
    c.WmiMonitorBrightnessMethods()[0].WmiSetBrightness(brightness, 0)  # Second parameter 0 is for the brightness level source

# Function to calculate average light level
def average_light_level():
    # Capture screen image
    screen_image = ImageGrab.grab()

    # Convert image to grayscale
    gray_image = screen_image.convert('L')

    # Convert image to numpy array for faster processing
    image_array = np.array(gray_image)

    # Calculate average pixel value
    average_brightness = np.mean(image_array)

    return average_brightness

def check():
    average_brightness = average_light_level()
    
    if(average_brightness > 100):
    	current_brightness = get_brightness()
    	if(current_brightness > 50):
	    	set_brightness(30)
    elif(average_brightness < 50):
    	current_brightness = get_brightness()
    	if(current_brightness < 50):
        	set_brightness(80)
    
    print("Average light level:", average_brightness)
while True:
    check()
    time.sleep(3)
