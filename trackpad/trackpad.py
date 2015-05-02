#!/usr/bin/env python

import subprocess 

# * some settings *"
touchpad_device_id = 11 		# you can detect id via 'xinput list'
trackpoint_device_id = 12 		
icon_path = "/path/to/icons/icon.png" # you have to use absolute path

def get_props(device_id):
	cmd = "xinput list-props " + str(device_id) + " | grep \"Device Enabled\" | awk '{print $4}'"
	is_enabled = subprocess.check_output(cmd, shell=True)
	return int(is_enabled)


def send_notify(touchpad_state, trackpoint_state):
	device_status = "Touchpad:" + "\t" + touchpad_state + "\n" + "Trackpoint:" + "\t" + trackpoint_state
	icon_arg = "--icon=" + icon_path
	subprocess.call(["notify-send", "--urgency=low", "--expire-time=2000", icon_arg, "TrackPad Notify", device_status])

def change_device_state(device_id, enable = True):
	subprocess.call(["xinput", "set-prop", str(device_id), "Device Enabled", str(int(enable))])


if __name__ == "__main__":
	touchpad_is_enabled = get_props(touchpad_device_id)
	trackpoint_is_enabled = get_props(trackpoint_device_id)

	if touchpad_is_enabled and trackpoint_is_enabled:
		change_device_state(touchpad_device_id, False)
		send_notify("disabled", "enabled")
	elif touchpad_is_enabled == False and trackpoint_is_enabled:
		change_device_state(trackpoint_device_id, False)
		send_notify("disabled", "disabled")
	elif touchpad_is_enabled and trackpoint_is_enabled == False:
		change_device_state(trackpoint_device_id)
		send_notify("enabled", "enabled")
	else:
		change_device_state(touchpad_device_id)
		send_notify("enabled", "disabled")	

