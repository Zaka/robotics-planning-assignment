#!/usr/bin/env python

import pdb
import Tkinter as tk
import matplotlib.image as mpimg
import numpy as np
from PIL import Image, ImageTk

# Read image
class MainWindow():
    def __init__(self):
        self.root = tk.Tk()
        
        self.im = Image.open('../maze-images/maze-01.png')

        self.photo = ImageTk.PhotoImage(image = self.im)
        
        self.imgSize = { 'width' : self.photo.width(),
                         'height' : self.photo.height() }
        
        self.windowSize = dict(self.imgSize)
        
        self.maze = self.getMap(self.im.getdata())

        initSize = { 'w' : 400, 'h' : 400 }
        
        self.frame = tk.Frame(self.root,
                              width = initSize['w'],
                              height = initSize['h'])
        self.frame.columnconfigure(0, weight = 1)
        self.frame.rowconfigure(0, weight = 1)
        self.frame.pack(fill = BOTH, expand = 1)
        self.canvas = tk.Canvas(self.frame,
                                bd = 0,
                                highlightthickness = 0,
                                width=initSize['w'],
                                height=initSize['h'])
        self.canvas.grid(row = 0, sticky = W+E+N+S)
        self.canvas.place(x=0,y=0)

        # Mouse event handling
        self.root.bind('<Button-1>', self.onLeftButton)
        self.root.bind('<Button-3>', self.onRightButton)
        # Resize event handling
        self.frame.bind('<Configure>', self.onResize)

        self.imageOnCanvas = self.canvas.create_image(0,0,
                                 image = self.photo,
                                 anchor=tk.NW)
    
        self.root.mainloop()
                
    def onLeftButton(self, event):
        # TODO: Mark as start of the path
        
        x = self.imgSize['width']*event.x / self.windowSize['width']
        y = self.imgSize['height']*event.y / self.windowSize['height']

        self.im.putpixel((x,y), 230)

        resized = self.im.resize((self.windowSize['width'],
                                  self.windowSize['height']),
                                 Image.ANTIALIAS)
        
        self.photo = ImageTk.PhotoImage(image = resized)
        
        self.canvas.config(width = self.windowSize['width'],
                           height = self.windowSize['height'])
        self.canvas.itemconfig(self.imageOnCanvas,
                               image = self.photo)
        self.root.update()
        # TODO: Fire the createPath method only if start and end are
        # defined

    def onRightButton(self, event):
        # TODO: Mark as the end of the path
        x = self.imgSize['width']*event.x / self.windowSize['width']
        y = self.imgSize['height']*event.y / self.windowSize['height']

        self.im.putpixel((x,y), 150)

        resized = self.im.resize((self.windowSize['width'],
                                  self.windowSize['height']),
                                 Image.ANTIALIAS)
        
        self.photo = ImageTk.PhotoImage(image = resized)
        
        self.canvas.config(width = self.windowSize['width'],
                           height = self.windowSize['height'])
        self.canvas.itemconfig(self.imageOnCanvas,
                               image = self.photo)
        self.root.update()
        
        # TODO: Fire the createPath method only if start and end are
        # defined

    def onResize(self, event):
        size = (event.width, event.height)
        
        self.windowSize['width'] = event.width
        self.windowSize['height'] = event.height
        
        resized = self.im.resize(size,Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(resized)
        self.canvas.config(width = event.width,
                           height = event.height)
        self.canvas.delete("IMG")
        self.canvas.create_image(0, 0, image=self.photo,
                                  anchor=tk.NW, tags="IMG")
        self.root.update()

    def getMap(self, data):
        maze = np.full(shape = data.size,
                       fill_value = float('inf'))

        for i in np.ndindex(data.size):
            if data.getpixel(i) == 255:
                maze[index] = 0

        return maze
                    
            

        
# TODO: Uncomment and indent        
# if __name__ == '__main__':
x=MainWindow()

# TODO: Select start and goal

# TODO: Plan the path

# TODO: Draw the path over the image

