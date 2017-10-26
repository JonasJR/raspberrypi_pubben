#!/usr/bin/python

# use a Tkinter label as a panel/frame with a background image
# note that Tkinter only reads gif and ppm images
# use the Python Image Library (PIL) for other image formats
# free from [url]http://www.pythonware.com/products/pil/index.htm[/url]
# give Tkinter a namespace to avoid conflicts with PIL
# (they both have a class named Image)

import Tkinter as tk
from PIL import Image, ImageTk
from ttk import Frame, Button, Style
import time, glob, os

class Example():
    def __init__(self):
        self.root = tk.Tk()
        # Change this to be the location of the folder for the specific TV
        os.chdir("/home/jonas/Pictures/test")

        # pick an image file you have .bmp  .jpg  .gif.  .png
        # load the file and covert it to a Tkinter image object
        for file in glob.glob("*.jpg"):
            self.imageFile = file
        self.image = ImageTk.PhotoImage(Image.open(self.imageFile))

        # get the image size
        w = self.image.width()
        h = self.image.height()

        # position coordinates of root 'upper left corner'
        x = 0
        y = 0

        # make the root window the size of the image
        self.root.geometry("%dx%d+%d+%d" % (w, h, x, y))

        # root has no image argument, so use a label as a panel
        self.panel1 = tk.Label(self.root, image=self.image)
        self.display = self.image
        self.panel1.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES)
        print ("Display image")
        self.root.after(10000, self.update_image)
        self.root.mainloop()

    def update_image(self):
        for file in glob.glob("*.jpg"):
            newImageFile = file
        try:
            if newImageFile != self.imageFile:
                self.image = ImageTk.PhotoImage(Image.open(newImageFile))
                self.panel1.configure(image=self.image)
                print ("Display new image")
                self.display = self.image
                self.imageFile = newImageFile
            else:
                print ("No new image")
        except Exception:
            print ("NO IMAGE IN FOLDER")
        self.root.after(10000, self.update_image)       # Set to call again in 30 seconds

def main():
    app = Example()

if __name__ == '__main__':
    main()
