import platform
import time
from windows import checkWindows
# from linux import checkLinux
from macOS import checkMacOS
   
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

# Example usage
os_name = detect_os()
print("Operating System:", os_name)

if(os_name == "Windows"):
    while True:
        checkWindows()
        time.sleep(3)
elif( os_name == "Linux"):
    print("Linux is not supported yet.")
elif( os_name == "macOS"):
    while True:
        checkMacOS()
        time.sleep(3)