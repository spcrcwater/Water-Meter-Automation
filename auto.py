from time import sleep
from datetime import datetime, timedelta
import os
import subprocess

while True:
    filename = subprocess.getoutput('ls /home/pi/Desktop/images | head -1')
    if (filename != ""):
        cmd1 = "rclone copy /home/pi/Desktop/images/" + filename + " remote:test"
        os.system(cmd1)
        print("Image uploaded")
        cmd2 = "rm /home/pi/Desktop/images/" + filename
        sleep(20)
        os.system(cmd2)
        print("Task completed")

    else:
        print("Folder is empty")
        sleep(20)
        continue

