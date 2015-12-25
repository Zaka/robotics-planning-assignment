import unittest
import pdb
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

        self.testDistanceMatrix = [[None, None,         None,         None, None, None],
                                   [None, None,         None,         None, None, None],
                                   [None, float('inf'), float('inf'), None, None, None],
                                   [None, None,         float('inf'), None, None, None],
                                   [None, float('inf'), float('inf'), None, None, None],
                                   [None, None,         None,         None, None, None],
                                   [None, None,         None,         None, None, None]]

    def test__init__(self):
        from PIL import Image 
        im = Image.open('../maze-images/maze-01.png')
        maze = Maze(im.getdata())

        for row in maze.data:
            self.assertIn(row, self.expectedMazeData)

    def testGetPoint(self):
        maze = Maze()
        maze.data = self.testDistanceMatrix
        maze.setStart((5, 6))
        maze.setGoal((1,3))

        
        nonePoints = [(0,0), (1,0), (5, 0), (0, 6)]
        for p in nonePoints:
            self.assertIsNone(maze.getPoint(p))

        obstaclePoints = [(1, 2), (1, 4), (2, 2), (2, 3), (2, 4)]
        for p in obstaclePoints:
            self.assertEqual(float('inf'),
                             maze.getPoint(p))
            
        self.assertEqual('G',
                         maze.getPoint((1, 3)))

        self.assertEqual('S',
                         maze.getPoint((5, 6)))
            
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
        """Test computation of distance surrounding a goal.
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
        maze.setGoal((1, 3))

        for elem in testList:
            self.assertAlmostEqual( elem['expectedDistance'],
                                    maze.computeDistanceToNeighbours(elem['point']),
                                    places = 14,
                                    msg = "Error computing distance for point " +  str(elem['point']))


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
        """Test the computation of  a distance surrounding a start.
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

    def testExists(self):
        maze = Maze()
        maze.data = self.testDistanceMatrix
        
        nonExistentPoints = [(-1,0), (0,-1), (6, 0), (0, 7), (6, 7)]
        existingPoints = [(0,0),(0, 6), (5, 0), (5, 6)]

        for p in nonExistentPoints:
            self.assertFalse(maze.exists(p), "Error with non-existent point: " + str(p))

        for p in existingPoints:
            self.assertTrue(maze.exists(p), "Error with existent point: " + str(p))

            
    # @unittest.skip("")
    def testIsEmpty(self):
        # TODO: We need to test for positions that have a distance
        # already
        
        maze = Maze([])
        maze.data = self.testDistanceMatrix
        maze.setStart((5, 6))
        maze.setGoal((1,3))

        maze.setPoint((3, 3), 1.22)

        emptyPoints = [(0,0), (5, 0), (0, 6)]
        notEmptyPoints = [(1, 2), (1, 3), (1, 4), (5, 6), (3, 3)]

        for p in emptyPoints:
            self.assertTrue(maze.isEmpty(p), "Error with empty point: " + str(p))

        for p in notEmptyPoints:
            self.assertFalse(maze.isEmpty(p), "Error with non-empty point: " + str(p))
            
    # @unittest.skip("")
    def testSelectNeighbours(self):
        maze = Maze([])
        maze.data = self.testDistanceMatrix
        maze.setStart((5, 6))
        maze.setGoal((1,3))

        expectedNeighbours = [(0,3), (0,4), (0, 2)]
        self.assertEqual(expectedNeighbours,
                         maze.selectNeighbours(maze.goal))
        
    # @unittest.skip("")
    def testSelectNeighbours01(self):
        """Test when selecting already valued neighbours
        """
        testMatrix = [[None, None,         None,              None,              None, None], 
                      [None, None,         None,              None,              None, None], 
                      [None, float('inf'), float('inf'),      5.24264068712,     None, None], 
                      [None, None,         float('inf'),      6.24264068712,     None, None], 
                      [None, float('inf'), float('inf'),      7.24264068712,     None, None], 
                      [None, None,         3.82842712474,     4.82842712474,     None, None], 
                      [None, None,         4.242640687110001, 5.242640687110001, None, None]]

        maze = Maze([])
        maze.data = testMatrix
        maze.setStart((5, 6))
        maze.setGoal((1,3))
        currentPos = (3,5)

        expectedNeighbours = [(3,4), (4,5), (4, 6), (4,4)]
        self.assertEqual(expectedNeighbours,
                         maze.selectNeighbours(currentPos))
        
    def assertListAlmostEqual(self, lst1, lst2, places=7, msg=None, delta=None):
        len1 = len(lst1)
        len2 = len(lst2)

        if len1 != len2:
            msg = self._formatMessage(msg, 'Length of lists is different')
            raise self.failureException(msg)

        for i in xrange(len1):
            item1 = lst1[i]
            item2 = lst2[i]

            if ( type(item1) == list and
                 type(item2) == list ):
                self.assertListAlmostEqual( item1, item2, places, msg=msg,
                                            delta=delta )
            else:
                self.assertAlmostEqual( item1, item2, places=places,
                                        msg=msg, delta=delta )
                
    # @unittest.skip("")
    def testComputeDistanceMatrix(self):
        """Test the computation of a maze with a concave hurdle.
        """
        expectedDistanceMatrix = [[3.414213562373095,  3.8284271247461903, 4.242640687119286,  5.242640687119286, 6.242640687119286, 7.242640687119286], 
                                  [2.414213562373095,  2.8284271247461903, 3.8284271247461903, 4.82842712474619,  5.82842712474619,  6.82842712474619],  
                                  [1.4142135623730951, float('inf'),       float('inf'),       5.242640687119286, 6.242640687119286, 7.242640687119286], 
                                  [1,                  'G',                float('inf'),       6.242640687119286, 6.656854249492381, 7.656854249492381], 
                                  [1.4142135623730951, float('inf'),       float('inf'),       5.242640687119286, 6.242640687119286, 7.242640687119286], 
                                  [2.414213562373095,  2.8284271247461903, 3.8284271247461903, 4.82842712474619,  5.82842712474619,  6.82842712474619],  
                                  [3.414213562373095,  3.8284271247461903, 4.242640687119286,  5.242640687119286, 6.242640687119286, 'S' ]]

        maze = Maze([])
        maze.data = self.testDistanceMatrix
        maze.setGoal((1,3))
        maze.setStart((5, 6))
        maze.computeDistanceMatrix()

        self.assertListAlmostEqual(expectedDistanceMatrix,
                                   maze.data)

        

    @unittest.skip("")
    def testComputeDistanceMatrix(self):
        """Test the computation of a maze with a concave hurdle.
        """
        maze = Maze([])
        maze.data = self.expectedMazeData
        maze.setGoal((15, 12))
        maze.setStart((5, 9))
        maze.computeDistanceMatrix()

        pdb.set_trace()

        self.assertListAlmostEqual(expectedDistanceMatrix,
                                   maze.data)
        
    # @unittest.skip("")
    def testGetShortestPath(self):
        """Test the computation of a maze with a concave hurdle.
        """
        data = [[3.414213562373095,  3.8284271247461903, 4.242640687119286,  5.242640687119286, 6.242640687119286, 7.242640687119286], 
                [2.414213562373095,  2.8284271247461903, 3.8284271247461903, 4.82842712474619,  5.82842712474619,  6.82842712474619],  
                [1.4142135623730951, float('inf'),       float('inf'),       5.242640687119286, 6.242640687119286, 7.242640687119286], 
                [1,                  None,               float('inf'),       6.242640687119286, 6.656854249492381, 7.656854249492381], 
                [1.4142135623730951, float('inf'),       float('inf'),       5.242640687119286, 6.242640687119286, 7.242640687119286], 
                [2.414213562373095,  2.8284271247461903, 3.8284271247461903, 4.82842712474619,  5.82842712474619,  6.82842712474619],  
                [3.414213562373095,  3.8284271247461903, 4.242640687119286,  5.242640687119286, 6.242640687119286, None ]]

        expectedPath = [(4, 5), (3, 5), (2, 5), (1, 5), (0, 4)]
        
        maze = Maze([])
        maze.data = data
        maze.setGoal((1,3))
        maze.setStart((5, 6))

        self.assertEqual(expectedPath,
                         maze.getShortestPath())
        
#if __name__ == '__main__':
unittest.main()
