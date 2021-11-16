#!/usr/bin/python3

import libmicon
import socket
import platform
import time

test = libmicon.micon_api("/dev/ttyS1")

##to enable debug info change to
#test = libmicon.micon_api(1)

##update the date for the lcd display
test.set_lcd_date()
test.cmd_force_lcd_disp(libmicon.lcd_disp_date)
time.sleep(1)

##set the ip address for the lcd display
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('10.255.255.255', 1))
host_ip = s.getsockname()[0]
s.close()
host_name = socket.gethostname()
test.set_lcd_buffer_short(libmicon.lcd_set_ipaddress,host_ip)
test.set_lcd_buffer_short(libmicon.lcd_set_hostname,host_name)

test.cmd_force_lcd_disp(libmicon.lcd_disp_hostname)
time.sleep(1)

##set link speed (just to gbps)
test.send_write_cmd(1,libmicon.lcd_set_linkspeed,libmicon.LINK_1000M)
test.send_write_cmd(1,0x37,libmicon.LINK_1000M)
test.cmd_force_lcd_disp(libmicon.lcd_disp_linkspeed)
time.sleep(1)

##set custom lcd message
test.set_lcd_buffer(libmicon.lcd_set_buffer0,"Terastation x86", "Ubuntu")
test.cmd_force_lcd_disp(libmicon.lcd_disp_buffer0)

##enable just the messages that we've configured so far.
test.send_write_cmd(1,libmicon.lcd_set_dispitem,0x3F)
test.send_write_cmd(1,libmicon.lcd_set_dispitem_ex,0x00)

##configure to cycle through displays via the display button
test.send_write_cmd(0,libmicon.lcd_changemode_button)

##configure to cycle through displays every ~3 seconds
#test.send_write_cmd(0,libmicon.lcd_changemode_auto)

##turn off all sata leds 
test.cmd_set_sataled(libmicon.LED_OFF,libmicon.SATA_ALL_LED)


#cycle through all the backlight combinations
test.set_lcd_color(libmicon.LCD_COLOR_AQUA)

#set LCD backlight brightness
test.set_lcd_brightness(libmicon.LCD_BRIGHT_FULL)

#run some standalone commands
test.send_write_cmd(0,libmicon.lcd_disp_animation)

test.port.close()
quit()
