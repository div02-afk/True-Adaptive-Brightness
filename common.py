from PIL import ImageGrab
import numpy as np

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
