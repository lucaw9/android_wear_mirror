# android_wear_mirror

1. Place the python file into path:

/c/Users/NAME/AppData/local/android/sdk/platform-tools

This location should contain adb.exe

2. Open it and adjust the adress in line 35:
Find address of your device by running cmd at this location and executing:

adb devices

3. Execute it (for example via MinGW64):

cd /c/Users/NAME/AppData/local/android/sdk/platform-tools
python android_screen_mirror_lw.py



Credits:

This application was originally developed by @baitisj here: https://github.com/baitisj/android_screen_mirror
Check the original repo for more info on how to use this.

I merely adjusted some things to make it work with GTK 3.0


