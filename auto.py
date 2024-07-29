from time import sleep
from datetime import datetime, timedelta
import os
import subprocess

while True:
    filename = subprocess.getoutput('ls /home/pi/Desktop/images | head -1')
    if filename != "":
        cmd1 = ["rclone", "copy",
                f"/home/pi/Desktop/images/{filename}", "remote:test"]
        result = subprocess.run(cmd1, capture_output=True, text=True)

        if result.returncode == 0:
            print(f"Image uploaded successfully: {result.returncode}")
            cmd2 = "rm /home/pi/Desktop/images/" + filename
            sleep(20)
            os.system(cmd2)
            print("Task completed")
        else:
            print(
                f"Error occurred while uploading image. Return code: {result.returncode}")
            print(f"stderr: {result.stderr}")
            if "config" in result.stderr:
                print("Trying by copying the backup config file")
                cmd3 = ["cp", "/home/pi/.config/rclone/rclone.conf",
                        "/root/.config/rclone/"]
                subprocess.run(cmd3)
            sleep(20)
    else:
        print("Folder is empty")
        sleep(20)
        continue
