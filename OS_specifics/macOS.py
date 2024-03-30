from common import average_light_level
import subprocess

def set_brightness(brightness):
    set_brightness = f'brightness {brightness/100}'
    subprocess.run(set_brightness, shell=True)

def check_macOS():
    average_brightness = average_light_level()
    if(average_brightness > 100):
        set_brightness(30)
    elif(average_brightness < 50):
        set_brightness(80)
    
    print("Average light level:", average_brightness)