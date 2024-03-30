from common import average_light_level
import subprocess
# Function to set brightness using AppleScript
def set_brightness(brightness):
    applescript = "\'tell application \"System Events\"\' -e \'key code 144\' -e \' end tell\'"
    subprocess.run(['osascript', '-e', applescript])
    repeatScript = "!!"
    for i in range(5):
        subprocess.run(['osascript', '-e', repeatScript])

def check_macOS():
    average_brightness = average_light_level()
    if(average_brightness > 100):
        set_brightness(30)
    elif(average_brightness < 50):
        set_brightness(80)
    
    print("Average light level:", average_brightness)