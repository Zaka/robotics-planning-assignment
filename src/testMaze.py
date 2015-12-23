import unittest
from planning import Maze

class TestMaze(unittest.TestCase):
    def __init__(self, *args, **kargs):
        super(TestMaze, self).__init__(*args, **kargs)
        self.expectedMazeData = [[None, None, None, None, None, None, None, None, None, None,         None, None, None, None, None, None, None, None, None, None],
                                 [None, None, None, None, None, None, None, None, None, None,         None, None, None, None, None, None, None, None, None, None],
                                 [None, None, None, None, None, None, None, None, None, None,         None, None, None, None, None, None, None, None, None, None],
                                 [None, None, None, None, None, None, None, None, None, None,         None, None, None, None, None, None, None, None, None, None],
                                 [None, None, None, None, None, None, None, None, None, None,         None, None, None, None, None, None, None, None, None, None],
                                 [None, None, None, None, None, None, None, None, None, float('inf'), None, None, None, None, None, None, None, None, None, None],
                                 [None, None, None, None, None, None, None, None, None, float('inf'), None, None, None, None, None, None, None, None, None, None],
                                 [None, None, None, None, None, None, None, None, None, float('inf'), None, None, None, None, None, None, None, None, None, None],
                                 [None, None, None, None, None, None, None, None, None, float('inf'), None, None, None, None, None, None, None, None, None, None],
                                 [None, None, None, None, None, None, None, None, None, float('inf'), None, None, None, None, None, None, None, None, None, None],
                                 [None, None, None, None, None, None, None, None, None, float('inf'), None, None, None, None, None, None, None, None, None, None],
                                 [None, None, None, None, None, None, None, None, None, float('inf'), None, None, None, None, None, None, None, None, None, None],
                                 [None, None, None, None, None, None, None, None, None, float('inf'), None, None, None, None, None, None, None, None, None, None],
                                 [None, None, None, None, None, None, None, None, None, float('inf'), None, None, None, None, None, None, None, None, None, None],
                                 [None, None, None, None, None, None, None, None, None, float('inf'), None, None, None, None, None, None, None, None, None, None],
                                 [None, None, None, None, None, None, None, None, None, None,         None, None, None, None, None, None, None, None, None, None],
                                 [None, None, None, None, None, None, None, None, None, None,         None, None, None, None, None, None, None, None, None, None],
                                 [None, None, None, None, None, None, None, None, None, None,         None, None, None, None, None, None, None, None, None, None],
                                 [None, None, None, None, None, None, None, None, None, None,         None, None, None, None, None, None, None, None, None, None],
                                 [None, None, None, None, None, None, None, None, None, None,         None, None, None, None, None, None, None, None, None, None]]

        self.testDistance = [[None, None, None, None, None, None,              None, None,              None, None,         None, None, None, None, None, None, None, None, None, None],
                             [None, None, None, None, None, None,              None, None,              None, None,         None, None, None, None, None, None, None, None, None, None],
                             [None, None, None, None, None, None,              None, None,              None, None,         None, None, None, None, None, None, None, None, None, None],
                             [None, 'G',  None, None, None, None,              None, None,              None, None,         None, None, None, None, None, None, None, None, None, None],
                             [None, None, None, None, None, None,              None, None,              None, None,         None, None, None, None, None, None, None, None, None, None],
                             [None, None, None, None, None, None,              None, None,              None, float('inf'), None, None, None, None, None, None, None, None, None, None],
                             [None, None, None, None, None, None,              None, None,              None, float('inf'), None, None, None, None, None, None, None, None, None, None],
                             [None, None, None, None, None, 1.414213562373095, 1.0,  1.414213562373095, None, float('inf'), None, None, None, None, None, None, None, None, None, None],
                             [None, None, None, None, None, 1.0,               'G',  1.0,               None, float('inf'), None, None, None, None, None, None, None, None, None, None],
                             [None, None, None, None, None, 1.414213562373095, 1.0,  1.414213562373095, None, float('inf'), 32,   None, None, None, None, None, None, None, None, None],
                             [None, None, None, None, None, None,              None, None,              None, float('inf'), None, None, None, None, None, None, None, None, None, None],
                             [None, None, None, None, None, None,              None, None,              None, float('inf'), 'S',  None, None, None, None, None, None, None, None, None],
                             [None, None, None, None, None, None,              None, None,              None, float('inf'), None, None, None, None, None, None, None, None, None, None],
                             [None, None, None, None, None, None,              None, None,              None, float('inf'), None, None, None, None, None, None, None, None, None, None],
                             [None, None, None, None, None, None,              None, None,              None, float('inf'), None, None, None, None, None, None, None, None, None, None],
                             [None, None, None, None, None, None,              None, None,              None, None,         None, None, None, None, None, None, None, None, None, None],
                             [None, None, None, None, None, None,              None, None,              None, None,         None, None, None, None, None, None, None, None, None, None],
                             [None, None, None, None, None, None,              None, None,              None, None,         None, None, None, None, None, None, None, None, None, None],
                             [None, None, None, None, None, None,              None, None,              None, None,         None, None, None, None, None, None, None, None, None, None],
                             [None, None, None, None, None, None,              None, None,              None, None,         None, None, None, None, None, None, None, None, None, None]]
                            
    def test__init__(self):
        from PIL import Image 
        im = Image.open('../maze-images/maze-01.png')
        maze = Maze(im.getdata())

        for row in maze.data:
            self.assertIn(row, self.expectedMazeData)

    def testExists(self):
        from PIL import Image 
        im = Image.open('../maze-images/maze-01.png')
        maze = Maze(im.getdata())

        nonExistentPoints = [(-1,0), (0,-1), (len(maze.data), 0),
                             (0,len(maze.data[0]))]
        existingPoints = [(0,0),(1,1), (len(maze.data) - 1, 0),
                          (0,len(maze.data[0]) - 1)]

        for point in nonExistentPoints:
            self.assertFalse(maze.exists(point))

        for point in existingPoints:
            self.assertTrue(maze.exists(point))
            
    def testComputeDistanceToNeighbours01(self):
        """Compute a point in the middle of empty neighbours
        """
        point = (0,0)

        maze = Maze([])
        maze.data = self.testDistance

        self.assertIsNone(maze.computeDistanceToNeighbours(point))

    def testComputeDistanceToNeighbours02(self):
        """Compute a point near an obstacle
        """
        point = (9, 4)

        maze = Maze([])
        maze.data = self.testDistance

        self.assertIsNone(maze.computeDistanceToNeighbours(point))

    def testComputeDistanceToNeighbours03(self):
        """Compute a distance surrounding a goal.
        """
        testList = [ {'point':(0, 2), 'expectedDistance': 1.4142135623730951 },
                     {'point':(0, 3), 'expectedDistance': 1 },
                     {'point':(0, 4), 'expectedDistance': 1.4142135623730951 },
                     {'point':(1, 2), 'expectedDistance': 1 },
                     {'point':(1, 4), 'expectedDistance': 1 },
                     {'point':(2, 2), 'expectedDistance': 1.4142135623730951 },
                     {'point':(2, 3), 'expectedDistance': 1 },
                     {'point':(2, 4), 'expectedDistance': 1.4142135623730951 } ]
        
        maze = Maze([])
        maze.data = self.testDistance

        for elem in testList:
            self.assertAlmostEqual(elem['expectedDistance'],
                                   maze.computeDistanceToNeighbours(elem['point']),
                                   places = 14)


    def testComputeDistanceToNeighbours04(self):
        """Compute a distance in a general context. Surrounding other numbers,
        obstacles and empty entries.
        """
        testList = [ {'point':(4, 6),  'expectedDistance': 2.8284271247461903 },
                     {'point':(4, 7),  'expectedDistance': 2.414213562373095 },
                     {'point':(4, 8),  'expectedDistance': 2 },
                     {'point':(4, 9),  'expectedDistance': 2.414213562373095 },
                     {'point':(4, 10), 'expectedDistance': 2.8284271247461903 },

                     {'point':(8, 6),  'expectedDistance': 2.8284271247461903 },
                     {'point':(8, 7),  'expectedDistance': 2.414213562373095 }, 
                     {'point':(8, 8),  'expectedDistance': 2 },                 
                     {'point':(8, 9),  'expectedDistance': 2.414213562373095 }, 
                     {'point':(8, 10), 'expectedDistance': 2.8284271247461903 },

                     {'point':(5, 6), 'expectedDistance': 2.414213562373095 },
                     {'point':(6, 6), 'expectedDistance': 2 },
                     {'point':(7, 6), 'expectedDistance': 2.414213562373095 },

                     {'point':(5, 10), 'expectedDistance': 2.414213562373095 },
                     {'point':(6, 10), 'expectedDistance': 2 },                
                     {'point':(7, 10), 'expectedDistance': 2.414213562373095 } ]
        
        maze = Maze([])
        maze.data = self.testDistance

        for elem in testList:
            self.assertAlmostEqual(elem['expectedDistance'],
                                   maze.computeDistanceToNeighbours(elem['point']),
                                   places = 14)

    def testComputeDistanceToNeighbours05(self):
        """Compute a distance surrounding a start.
        """
        testList = [ {'point':(10, 10), 'expectedDistance': 33 },
                     {'point':(10, 11), 'expectedDistance': None },
                     {'point':(10, 12), 'expectedDistance': None } ]
        
        maze = Maze([])
        maze.data = self.testDistance

        for elem in testList:
            self.assertAlmostEqual(elem['expectedDistance'],
                                   maze.computeDistanceToNeighbours(elem['point']),
                                   places = 14)
            
if __name__ == '__main__':
    unittest.main()
