#!/usr/bin/env python

import pdb
import Tkinter as tk
import matplotlib.image as mpimg
import numpy as np
from PIL import Image, ImageTk

# Read image
class MainWindow():
    def __init__(self):
        self.startPoint = None
        self.goalPoint = None
        
        self.root = tk.Tk()
        
        self.im = Image.open('../maze-images/maze-01-color.png')

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
        self.frame.pack(fill = tk.BOTH, expand = 1)
        self.canvas = tk.Canvas(self.frame,
                                bd = 0,
                                highlightthickness = 0,
                                width=initSize['w'],
                                height=initSize['h'])
        self.canvas.grid(row = 0, sticky = tk.W + tk.E + tk.N + tk.S)
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
        x = self.imgSize['width']*event.x / self.windowSize['width']
        y = self.imgSize['height']*event.y / self.windowSize['height']

        if self.maze[y][x] == float('inf'):
            return
        
        # Mark as the end of the path
        self.maze[y][x] = 'S'
        self.startPoint = (x,y)
        
        beautifulRed = (168, 96, 113)
        self.im.putpixel((x,y), beautifulRed)

        resized = self.im.resize((self.windowSize['width'],
                                  self.windowSize['height']))
        
        self.photo = ImageTk.PhotoImage(image = resized)
        
        self.canvas.config(width = self.windowSize['width'],
                           height = self.windowSize['height'])
        self.canvas.itemconfig(self.imageOnCanvas,
                               image = self.photo)
        self.root.update()

        if self.startPoint and self.goalPoint:
            self.createPath()

    def onRightButton(self, event):
        # Get point in image dimensions (instead of window dimension)
        x = self.imgSize['width']*event.x / self.windowSize['width']
        y = self.imgSize['height']*event.y / self.windowSize['height']

        if self.maze[y][x] == float('inf'):
            return
        
        print "Mouse pressed at:", event.x, event.y
        print "img coord:", x, y

        # Mark as the end of the path
        self.maze[y][x] = 'G'
        self.goalPoint = (x,y)
        
        beautifulBlue = (113, 150, 176)
        self.im.putpixel((x,y), beautifulBlue)

        resized = self.im.resize((self.windowSize['width'],
                                  self.windowSize['height']))
        
        self.photo = ImageTk.PhotoImage(image = resized)
        
        self.canvas.config(width = self.windowSize['width'],
                           height = self.windowSize['height'])
        self.canvas.itemconfig(self.imageOnCanvas,
                               image = self.photo)
        self.root.update()

        if self.startMarked and self.goalMarked:
            self.createPath()

    def onResize(self, event):
        size = (event.width, event.height)
        
        self.windowSize['width'] = event.width
        self.windowSize['height'] = event.height
        
        resized = self.im.resize(size)
        self.photo = ImageTk.PhotoImage(resized)
        self.canvas.config(width = event.width,
                           height = event.height)
        self.canvas.delete("IMG")
        self.canvas.create_image(0, 0, image=self.photo,
                                  anchor=tk.NW, tags="IMG")
        self.root.update()

    def getMap(self, data):
        maze = [[float('inf') for i in range(data.size[0])] for j in range(data.size[1])]

        for h in range(len(maze)):
            for w in range(len(maze[0])):
                print data.getpixel((w,h))
                if data.getpixel((w,h)) == (255, 255, 255):
                    maze[h][w] = 0

        return maze

    def printMaze(self, maze):
        for l in maze:
            for v in l:
                print v,
            print ''
    
    def createPath(self):
        pass

        
# TODO: Uncomment and indent        
# if __name__ == '__main__':
x=MainWindow()

# TODO: Plan the path

# TODO: Draw the path over the image

# TODO: Ensure that the map has only one start point and only one goal
# point.
