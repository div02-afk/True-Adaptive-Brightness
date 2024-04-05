import subprocess
import sys
import pystray
from pystray import MenuItem as item
from PIL import Image
from common import detect_os
process = None

def run_command():
    global process
    if(detect_os() == "Windows"):
        process = subprocess.Popen(["python", "main.py"])
    elif(detect_os() == "Linux" or detect_os() == "macOS"):
        process = subprocess.Popen(["python3", "main.py"])
    else:
        print("Unsupported operating system")
        sys.exit()

def stop_command():
    global process
    process.terminate()

def on_quit_callback(icon, item):
    icon.stop()
    sys.exit()


icon = pystray.Icon("my_app", title="Adaptive Brightness")
icon.icon = Image.open(".//assets//Adaptive_Brightness.png")
icon.menu = (item('Start', run_command),item("Stop", stop_command), item('Quit', on_quit_callback))
icon.run()
