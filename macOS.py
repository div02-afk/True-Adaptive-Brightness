import subprocess
from common import average_light_level
# Function to set brightness using AppleScript
def set_brightness(brightness):
    applescript = f'tell application "System Events" to set brightness of every display to {brightness / 100}'
    subprocess.run(['osascript', '-e', applescript])

def checkMacOS():
    average_brightness = average_light_level()
    if(average_brightness > 100):
        set_brightness(30)
    elif(average_brightness < 50):
        set_brightness(80)
    
    print("Average light level:", average_brightness)