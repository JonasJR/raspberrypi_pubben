#!/usr/bin/python

import time, glob, os, shutil

class Example():
    def __init__(self):
        self._configfile = "tv.conf"
        self._mount = "/mnt/tv/"
        self._settings = {"on": True, "source": True, "off": True, "type": "samba", "source": "", "user": "", "pass": "", "time": 30, "default": True, "noDefaultTvCtrl": True, "maxTime": 60}
        self._readConf()
        self._tty = 1
        # Mount
        if self._settings["type"] == "samba":
            c = "mount -t cifs -o username=" + self._settings["user"] + ",password=" + self._settings["pass"] + ",noserverino" + " " + self._settings["source"] + " " + self._mount
            os.system(c)
            while not os.path.ismount(self._mount):
                self._logger.error("Could not mount, retries")
                c = "mount -t cifs -o username=" + self._settings["user"] + ",password=" + self._settings["pass"] + ",noserverino" + " " + self._settings["source"] + " " + self._mount
                os.system(c)
                time.sleep(self._mountSleep)
        else:
            self._logger.error("Unknown mount_type")
        # Change this to be the location of the folder for the specific TV
        os.chdir("/mnt/tv/")

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

    def _readConf(self):
        # Check if path and configfile exists
        if os.path.exists(self._configfile) == False:
            return "Cannot find the file " + self._configfile

        inFile = open(self._configfile,'r')

        for line in inFile:
            line = line.strip()
            if line != "" and line[0] != '#':
                split = line.split('=')
                option = split[0].strip().lower()
                value = split[1].strip().lower()
                ## Settings
                if option == "mount_source":
                    self._settings["source"] = value
                elif option == "mount_username":
                    self._settings["user"] = split[1].strip()
                elif option == "mount_password":
                    self._settings["pass"] = split[1].strip()

        inFile.close()
        return None

def main():
    app = Example()

if __name__ == '__main__':
    main()
