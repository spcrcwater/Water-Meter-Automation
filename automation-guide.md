# Installing rclone

- Run `sudo apt install rclone`
- Run the command `rclone config` and follow the intructions on https://rclone.org/drive/ to setup rclone
- Make sure to name the remote you create as `remote` only otherwise the code will not work

# Adding the code files

- We need 2 files to automate the process, both of which are provided. One is auto.py and another one is myauto.service
- For the auto.py file, just create a new file on the Desktop using the command `nano auto.py` and pasting the contents of the provided file in there (Make sure it is on the desktop only)
- For the .service file, make a new file using the command `sudo nano /etc/systemd/system/myauto.service` and paste the contents of the provided file in there (Make sure it is in the same directory as the command)

# Enabling the service file

- Run `sudo systemctl enable myauto.service` to enable the .service file
- Run the command `cd /home/pi/.config/rclone`, there you will find a file called `rclone.conf`
- Use the command `sudo cp rclone.conf /root/.config/rclone/` to copy the file to another location
- Use the command `sudo systemctl start myauto.service` to start the service file

## You are done, the automation should be successfully completed

# Checking the status of the service

- Use the command `sudo systemctl status myauto.service` to see the status of the .service file
- You can also use the `sudo systemctl stop myauto.service` and `sudo systemctl restart myauto.service` to stop and restart the service respectively