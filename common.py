from PIL import ImageGrab
import numpy as np
import platform
def average_light_level():
    screen_image = ImageGrab.grab()
    gray_image = screen_image.convert('L')
    image_array = np.array(gray_image)
    average_brightness = np.mean(image_array)
    return average_brightness
def detect_os():
    system = platform.system()
    if system == "Windows":
        return "Windows"
    elif system == "Linux":
        return "Linux"
    elif system == "Darwin":
        return "macOS"
    else:
        return "Unknown"
