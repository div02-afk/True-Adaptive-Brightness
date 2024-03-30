from common import average_light_level
import subprocess

def set_brightness(brightness):
    try:
        gamma = brightness / 100.0
        xrandr_output = subprocess.check_output(['xrandr']).decode('utf-8')
        connected_displays = [line.split()[0] for line in xrandr_output.splitlines() if ' connected' in line]

        for display in connected_displays:
            subprocess.run(['xrandr', '--output', display, '--brightness', str(gamma)])
            
    except Exception as e:
        print("Error:", e)

def check_linux():
    average_brightness = average_light_level()
    if(average_brightness > 100):
        set_brightness(30)
    elif(average_brightness < 50):
        set_brightness(80)
    
    print("Average light level:", average_brightness)