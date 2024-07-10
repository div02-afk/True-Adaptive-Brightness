from PIL import ImageGrab
import numpy as np
import platform
def average_light_level():
    screen_image = ImageGrab.grab()
    
    image = screen_image.convert('L')
    width, height = image.size
    part_width = width // 4
    part_height = height // 4

    # Create a list to hold the parts
    parts = []
    final_brightness = 0
    count=0
    less = 0
    # Loop through and crop out each part
    for i in range(4):
        for j in range(4):
            left = j * part_width
            upper = i * part_height
            right = left + part_width
            lower = upper + part_height
            part = image.crop((left, upper, right, lower))
            
            image_array = np.array(part)
            average_brightness = np.mean(image_array)
            if(average_brightness > 100):
                count+=1
                final_brightness += average_brightness
            if(average_brightness < 50):
                less+=1
    print(count,less,final_brightness)
    if(count > 3):
        return (final_brightness/count)
    if(less>6):
        return 30
    if(count==0):
        return 80
    return (final_brightness/count)
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
