#!/usr/bin/env python

import Tkinter
import matplotlib.image as mpimg
import numpy as np
from PIL import Image, ImageTk

# Read image
class mainWindow():
        # times=1
        # timestart=time.clock()

        data = mpimg.imread('../maze-images/laberinto-01.png')

        data = (data * 255).round().astype(np.uint8)

        width = data.shape[1]
        height = data.shape[0]


        # data=np.array(np.random.random((400,500))*100,
        #                  dtype=int)
        
        def __init__(self):
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
            self.root.after(0,self.start) # INCREASE THE 0 TO SLOW IT
                                          # DOWN

            print "width", self.width
            print "height", self.height

            self.root.mainloop()
                
        def start(self):
            global data
            self.im=Image.fromstring('L', (self.data.shape[1],\
                                           self.data.shape[0]),
                                     self.data.astype('b').tostring())
            self.photo = ImageTk.PhotoImage(image=self.im)
            self.canvas.create_image(0,0,
                                     image=self.photo,
                                     anchor=Tkinter.NW)
            self.root.update()
            # self.times+=1
            # if self.times%33==0:
            #     print "%.02f FPS"%(self.times/(time.clock()-self.timestart))
            # self.root.after(10,self.start)
            # self.data=np.roll(self.data,-1,1)

if __name__ == '__main__':
    x=mainWindow()

# TODO: Show image in a interactive window

# TODO: Select start and goal

# TODO: Plan the path

# TODO: Draw the path over the image

