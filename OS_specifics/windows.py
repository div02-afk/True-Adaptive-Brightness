from common import average_light_level
import wmi
import win32gui
import win32con
import win32process
import time


# Connect to WMI
c = wmi.WMI(namespace='wmi')

# Get brightness
def get_brightness():
    brightness = c.WmiMonitorBrightness()[0].CurrentBrightness
    return brightness
def set_brightness(brightness):
    brightness = min(max(brightness, 0), 100)
    c.WmiMonitorBrightnessMethods()[0].WmiSetBrightness(brightness, 0)  



def check_windows():
    try:
        average_brightness = average_light_level()
    except OSError as e:
        print(f"Error capturing screen: {e}. Retrying in 5 seconds...")
        time.sleep(5)
        check_windows()
        return
    
    
    if(average_brightness > 100):
        current_brightness = get_brightness()
        if(current_brightness > 50):
            set_brightness(30)
    elif(average_brightness < 50):
        current_brightness = get_brightness()
        if(current_brightness < 50):
            set_brightness(80)
    
    
    
    
    print("Average light level:", average_brightness)
    