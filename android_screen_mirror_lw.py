#!/usr/bin/env python

# A simple program that continuously polls an Android device
# and screen-grabs screen in PNG format.
# Adjusted for Gtk 3.0 by Luca Waldmann

# Requires: Gtk 3.0, `adb` in $PATH

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf

import threading, time

from subprocess import Popen, PIPE, STDOUT, check_output


class MainWindow(Gtk.Window):

    def __init__(self):
        super(MainWindow,self).__init__()
        self.img=Gtk.Image()
        self.add(self.img)
        self.con = True

        self.stopthread = threading.Event()
        threading.Thread(target=self.pull_data).start()

    ## Thread continously pulls image data over adb from the device.
    def pull_data(self):
        self.last_time=time.time()
        while not self.stopthread.isSet():
            try:
		# todo: adjust address here!
                png = check_output("adb -s 127.0.0.1:4444 exec-out screencap -p", timeout=5)
                # Load the PNG image into gdk and obtain a decompressed pixbuf
                loader = GdkPixbuf.PixbufLoader()
                loader.write(png)
                loader.close()
                pic = loader.get_pixbuf()
                self.img.set_from_pixbuf(pic)
                
                self.con = True
            except:
                if self.con:
                    print ("No connection!")
                    self.img.set_from_file("no_connect.png")
                    self.con = False
                time.sleep(1)
            # Some helpful framerate statistics
            self.current_time=time.time()
            print ("{:10.2f} fps\r".format(1.0/(self.current_time - self.last_time))),
            self.last_time = self.current_time

            # Displays windows if they're not already showing
            self.show_all()

    def stop(self):
        self.stopthread.set()


def main_quit(obj):
    global win
    win.stop()
    Gtk.main_quit()

def main():
    global win
    win = MainWindow()
    win.connect("destroy", main_quit)
    win.show_all()
    Gtk.main()

# Run our main function if we're in the default scope
if __name__ == "__main__":
    main()
