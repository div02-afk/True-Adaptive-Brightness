import platform
import time
from OS_specifics.windows import check_windows
from OS_specifics.linux import check_linux
from OS_specifics.macOS import check_macOS
   
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

time_delay = 1
os_name = detect_os()
print("Operating System:", os_name)

if(os_name == "Windows"):
    while True:
        check_windows()
        time.sleep(time_delay)
elif( os_name == "Linux"):
    while True:
        check_linux()
        time.sleep(time_delay)
elif( os_name == "macOS"):
    while True:
        check_macOS()
        time.sleep(time_delay)