Robotics planning assignment
============================


#Installation#

Python packages to install:

* TkInter
* PIL
* PIL - ImageTk

#Usage#

Press left mouse button to set the **starting point**, which is marked as
a red pixel.

Press right mouse button to set the **goal**, which is marked as a
blue pixel.

![Setting star & goal](https://github.com/Zaka/robotics-planning-assignment/blob/master/set-start-and-goal.png)

Press Space key to compute the path

![Computing the path](https://github.com/Zaka/robotics-planning-assignment/blob/master/solved-maze-02.png)

#Algorithm for path finding#

##Distance matrix computation ##

This solutions uses **dynamic programming** to find the shortest path
between start and goal.

The solution proposed here has a little tweak to improve the default
one. Instead of iterating until there are no changes, the algorithm
has a list of neighbours to be visited, where, per each point the
algoritm visites stores the next neighbours to be visited based on
weather this neghbours are empty places or has a value less than
current point's value plus the cost of the movement (that means that
the point that the algorithm is storing in the neighbours list has
been computed with a larger value from another possible path). Those,
we save time iterating over position that are already optimized.

##Path finding ##

The solution uses standard down-hill algorithm.

#Limitations #

* Doesn't support reseting of start and goal without close & open of
app.

* Very slow for mid to large mazes (maybe using another approach would
  improve the timing).
