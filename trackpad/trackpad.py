#!/usr/bin/env python

import subprocess 

icon_path = "/path/to/icons/icon.png" # you have to use absolute path

def get_props():
	cmd = "synclient -l | grep TouchpadOff | awk '{print $3}'"
	is_enabled = subprocess.check_output(cmd, shell=True)
	return int(is_enabled)


def send_notify(touchpad_state):
	device_status = "\nTouchpad:" + "\t" + touchpad_state + "\n" 
	icon_arg = "--icon=" + icon_path
	subprocess.call(["notify-send", "--urgency=low", "--app-name=trackpad", "--expire-time=1500", icon_arg, "TrackPad Notify", device_status])

def change_device_state(enable = True):
	state = "TouchpadOff="+str(int(enable))
	subprocess.call(["synclient", state])


if __name__ == "__main__":
	touchpad_is_enabled = get_props()

	if touchpad_is_enabled:
		change_device_state(False)
		send_notify("enabled")
	else:
		change_device_state(True)
		send_notify("disabled")	

