#!/usr/bin/python3

import libmicon
import os

micon_api = libmicon.micon_api("/dev/ttyS1")



##set custom lcd message
micon_api.set_lcd_buffer(libmicon.lcd_set_buffer0, os.environ['message_line_1'] ,os.environ['message_line_2'])
micon_api.cmd_force_lcd_disp(libmicon.lcd_disp_buffer0)

##enable just the messages that we've configured so far.
micon_api.send_write_cmd(1,libmicon.lcd_set_dispitem,0x3F)
micon_api.send_write_cmd(1,libmicon.lcd_set_dispitem_ex,0x00)

if (os.environ['status']=="error"):
    micon_api.set_lcd_color(libmicon.LCD_COLOR_ORANGE)
    micon_api.cmd_set_led(libmicon.LED_ON, libmicon.ERROR_LED)
    #try every possible sound setting.
    micon_api.cmd_sound(libmicon.BZ_MUSIC2)
elif (os.environ['status']=="busy"):
    micon_api.set_lcd_color(libmicon.LCD_COLOR_GREEN)
    micon_api.cmd_set_led(libmicon.LED_OFF, libmicon.ERROR_LED)
elif (os.environ['status']=="done"):
    micon_api.set_lcd_color(libmicon.LCD_COLOR_AQUA)
    micon_api.cmd_set_led(libmicon.LED_OFF, libmicon.ERROR_LED)
else:
    micon_api.set_lcd_color(libmicon.LCD_COLOR_AQUA)
    micon_api.cmd_set_led(libmicon.LED_OFF, libmicon.ERROR_LED)



micon_api.port.close()
quit()
