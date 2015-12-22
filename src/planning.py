#!/usr/bin/env python

import Tkinter
import matplotlib.image as mpimg
import numpy as np
from PIL import Image, ImageTk

# Read image
class MainWindow():
    def __init__(self):
        self.data = mpimg.imread('../maze-images/maze-01.png')
        self.data = (self.data * 255).round().astype(np.uint8)

        # TODO: Transform the data to a 0, inf matrix. Where inf is
        # obstacle.
        self.maze = self.getMap(self.data)
        
        self.width = self.data.shape[1]
        self.height = self.data.shape[0]

        self.root = Tkinter.Tk()
        self.frame = Tkinter.Frame(self.root,
                                   width=self.width,
                                   height=self.height)
        self.frame.pack()
        self.canvas = Tkinter.Canvas(self.frame,
                                     width=self.width,
                                     height=self.width)
        # self.canvas.place(x=-2,y=-2)
        self.canvas.place(x=0,y=0)

        # Mouse event handling
        self.root.bind('<Button-1>', self.onLeftButton)
        self.root.bind('<Button-3>', self.onRightButton)
        
        self.root.after(0,self.start)
        self.root.mainloop()
                
    def start(self):
        self.im=Image.fromstring('L', (self.data.shape[1],\
                                       self.data.shape[0]),
                                 self.data.astype('b').tostring())
        self.photo = ImageTk.PhotoImage(image=self.im)
        self.canvas.create_image(0,0,
                                 image=self.photo,
                                 anchor=Tkinter.NW)
        self.root.update()

    def onLeftButton(self, event):
        # TODO: Mark as start of the path
        self.canvas.create_line(event.x, event.y,
                                event.x + 1, event.y,
                                fill='red')
        print "Left button on", event.x, event.y
        # TODO: Fire the createPath method only if start and end are
        # defined

    def onRightButton(self, event):
        # TODO: Mark as the end of the path
        self.canvas.create_line(event.x, event.y,
                                event.x + 1, event.y,
                                fill='green')
        print "Right button on", event.x, event.y
        # TODO: Fire the createPath method only if start and end are
        # defined

    def getMap(self, data):
        maze = np.full(shape = data.shape,
                       fill_value = float('inf'))

        for index, value in np.ndenumerate(self.data):
            if value == 255:
                maze[index] = 0

        return maze
                    
            

        
# TODO: Uncomment and indent        
# if __name__ == '__main__':
x=MainWindow()

# TODO: Select start and goal

# TODO: Plan the path

# TODO: Draw the path over the image

