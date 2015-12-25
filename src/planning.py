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
        maze = [[float('inf') for i in range(data.size[0])]
                for j in range(data.size[1])]

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

class Maze():
    DIR = [(0,1), (0,-1), (1,0), (1,1),
           (1,-1), (-1,0), (-1,1), (-1, -1)]

    DIRCOST = {(0,1) : 1, (0,-1) : 1, (1,0) : 1,
               (1,1) : 1.4142135623730951,
               (1,-1) : 1.4142135623730951, (-1,0) : 1,
               (-1,1) : 1.4142135623730951,
               (-1, -1) : 1.4142135623730951}

    def __init__(self, imgData = []):
        self.start = None
        self.goal = None
        
        if imgData:
            self.data = [[float('inf') for i in range(imgData.size[0])]
                         for j in range(imgData.size[1])]

            for h in range(len(self.data)):
                for w in range(len(self.data[0])):
                    if imgData.getpixel((w,h)) == (255, 255, 255):
                        self.data[h][w] = None
        else:
            self.data = []

    def setStart(self, start):
        if self.isEmpty(start):
            self.start = start
            self.setPoint(self.start, 'S')

    def setGoal(self, goal):
        if self.isEmpty(goal):
            self.goal = goal
            self.setPoint(self.goal, 'G')

    def isEmpty(self, point):
        """Point exists and is not an obstacle.
        """
        return ( self.exists(point) and
                 self.getPoint(point) == None )
    
    def exists(self, point):
        return not ( point[0] < 0 or
                     point[1] < 0 or
                     point[0] >= len(self.data[0]) or
                     point[1] >= len(self.data) )

    def setPoint(self, t, v):
        self.data[t[1]][t[0]] = v
        
    def getPoint(self, t):
        return self.data[t[1]][t[0]]
    
    def computeDistanceToNeighbours(self, refPoint):
        """Compute the minimum distance to neighbours and store it in the
        maze. If the point is surrounded by Non-Distances(None, inf or
        'S'), then the value is None. :param: refPoint Tuple representing the
        point
        """
        minDistance = float('inf')
                            
        for d in Maze.DIR:
            nextPoint = tuple(map(sum, zip(d, refPoint)))

            if self.exists(nextPoint):
                neighbourValue = self.getPoint(nextPoint)
            
                if ( neighbourValue != None and
                     neighbourValue != 'S' ):
                    if neighbourValue == 'G':
                        distanceToNeighbour = Maze.DIRCOST[d]
                    else:
                        distanceToNeighbour = (self.getPoint(nextPoint) + 
                                               Maze.DIRCOST[d])

                    if (distanceToNeighbour != float('inf') and
                        distanceToNeighbour < minDistance):
                        minDistance = distanceToNeighbour

        if minDistance == float('inf'):
            return None
        else:
            return minDistance

    def selectNeighbours(self, p):
        """Select neighbours of p Neighbours are empty spots or neighbours
        that have a value greater than p value + direction cost.
        """
        neighbours = []
        currentPointValue = self.getPoint(p)

        if currentPointValue == 'G':
            currentPointValue = 0
        elif currentPointValue == 'S':
            currentPointValue = float('inf')
            
        for d in Maze.DIR:
            candidate = tuple(map(sum, zip(d, p)))

            if self.exists(candidate):
                candidateValue = self.getPoint(candidate)

                if self.isEmpty(candidate):
                    neighbours.append(candidate)
                elif (candidateValue != 'G' and
                      candidateValue != 'S' and
                      self.getPoint(candidate) != float('inf') and
                      candidateValue > currentPointValue + Maze.DIRCOST[d]):
                    neighbours.append(candidate)

        return neighbours
        
    def computeDistanceMatrix(self):
        if ( self.start == None or
             self.goal == None ):
            return

        neighbours = set([])
        neighbours |= set(self.selectNeighbours(self.goal))

        while neighbours:
            nextNeighbour = neighbours.pop()

            self.setPoint(nextNeighbour,
                          self.computeDistanceToNeighbours(nextNeighbour))
            
            neighbours |= set(self.selectNeighbours(nextNeighbour))

    def getShortestPath(self):
        if ( self.start == None or
             self.goal == None ):
            return

        path = []
        currentPoint = self.start
        bestCandidate = []
        while True:
            if bestCandidate != []:
                currentPoint = bestCandidate
                path.append(bestCandidate)                

            bestCandidate = []
            bestCandidateValue = float('inf')
            
            for d in Maze.DIR:
                candidate = tuple(map(sum, zip(d, currentPoint)))

                # if candidate == (4, 5):
                #     pdb.set_trace()
                
                if self.exists(candidate):
                    candidateValue = self.getPoint(candidate)

                    if candidateValue == 'G':
                        return path

                    if ( candidateValue != 'S' and
                         candidateValue < bestCandidateValue ):
                        bestCandidateValue = candidateValue
                        bestCandidate = candidate

        return path
        
    def printMaze(self):
        for l in self.data:
            for v in l:
                print v,
            print

if __name__ == '__main__':
    x = MainWindow()

# TODO: Plan the path

# TODO: Draw the path over the image

# TODO: Ensure that the map has only one start point and only one goal
# point.
