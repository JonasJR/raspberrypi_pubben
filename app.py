#!/usr/bin/python

import time, glob, os, shutil

class Example():
    def __init__(self):
        self._tty = 1
        # Change this to be the location of the folder for the specific TV
        os.chdir("/home/pi/test")

        # pick an image file you have .bmp  .jpg  .gif.  .png
        # load the file and covert it to a Tkinter image object
        for file in glob.glob("*.jpg"):
            self.imageFile = file
        command = "fbi -T " + str(self._tty) + " --noverbose -a "
        os.system(command + str(self.imageFile))
        time.sleep(10)
        self.update_image


    def update_image(self):
        for file in glob.glob("*.jpg"):
            newImageFile = file
        try:
            if newImageFile != self.imageFile:
                command = "fbi -T " + str(self._tty) + " --noverbose -a "
                os.system(command + str(self.imageFile))
        except Exception:
            print ("NO IMAGE IN FOLDER")
        time.sleep(10)
        self.update_image

def main():
    app = Example()

if __name__ == '__main__':
    main()
