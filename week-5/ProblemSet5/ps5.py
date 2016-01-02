# 6.00.2x Problem Set 5
# Graph optimization
# Finding shortest paths through MIT buildings
#

import string
# This imports everything from `graph.py` as if it was defined in this file!
from graph import * 

#
# Problem 2: Building up the Campus Map
#
# Before you write any code, write a couple of sentences here 
# describing how you will model this problem as a graph. 

# This is a helpful exercise to help you organize your
# thoughts before you tackle a big design problem!
#

def load_map(mapFilename):
    """ 
    Parses the map file and constructs a directed graph

    Parameters: 
        mapFilename : name of the map file

    Assumes:
        Each entry in the map file consists of the following four positive 
        integers, separated by a blank space:
            From To TotalDistance DistanceOutdoors
        e.g.
            32 76 54 23
        This entry would become an edge from 32 to 76.

    Returns:
        a directed graph representing the map
    """
    # TODO
    print "Loading map from file..."
    f = open(mapFilename, 'r')
    graph = WeightedDigraph()
    # read each line
    for line in f:
        data = line.split()
        nodeSrc = Node(data[0])
        nodeDest = Node(data[1])
        weight1 = int(data[2])
        weight2 = int(data[3])
        # add the nodes to graph if the nodes not already in the graph
        if not (graph.hasNode(nodeSrc)):
            graph.addNode(nodeSrc)
        if not (graph.hasNode(nodeDest)):
            graph.addNode(nodeDest)
        # create a new edge
        edge = WeightedEdge(nodeSrc, nodeDest, weight1, weight2)
        graph.addEdge(edge)
    print "Loading map done!"
    return graph
        


        

#
# Problem 3: Finding the Shortest Path using Brute Force Search
#
# State the optimization problem as a function to minimize
# and what the constraints are
#

def bruteForceSearch(digraph, start, end, maxTotalDist, maxDistOutdoors):    
    """
    Finds the shortest path from start to end using brute-force approach.
    The total distance travelled on the path must not exceed maxTotalDist, and
    the distance spent outdoor on this path must not exceed maxDistOutdoors.

    Parameters: 
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by 
        a list of building numbers (in strings), [n_1, n_2, ..., n_k], 
        where there exists an edge from n_i to n_(i+1) in digraph, 
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    nodeStart = Node(start) 
    nodeEnd = Node(end)
    paths = bruteDFS(digraph, nodeStart, nodeEnd, ([], 0, 0))
    # find the paths that satisfy maxTotalDist
    # find the paths that satisfy maxDistOutdoors
    shortestDist = float('inf')
    shortestPath = []
    for eachPath in paths:
        if (eachPath[1] <= maxTotalDist) and (eachPath[2] <= maxDistOutdoors):
            if (eachPath[1] < shortestDist):
                shortestDist = eachPath[1]
                shortestPath = eachPath[0]
    # return value
    if (len(shortestPath) > 0):
        # format the shortest path
        pathPrint = []
        for eachNode in shortestPath:
            pathPrint.append(str(eachNode))
        return pathPrint
    else:
        raise ValueError('No solution available.')

#def computeWeight(digraph, path)

def bruteDFS(digraph, start, end, path):
    """ 
    DFS Search Method with no optimization 
    Input: a digraph, start node, end node, path
        path includes a tuple (list of nodes, totalWeight1, totalWeight2)
    Output: paths from start node to end node
    """
    newPath = list(path[0])
    newWeight1 = path[1]
    newWeight2 = path[2]
    if (len(newPath) > 0):
        lastNode = newPath[-1]
        currentEdge = digraph.getEdge(lastNode, start) 
        newWeight1 += int(currentEdge.getTotalDistance()) 
        newWeight2 += int(currentEdge.getOutdoorDistance())
    newPath.append(start)
    newInfo = (newPath, newWeight1, newWeight2)
    # base cases
    if (start == end):
        return [newInfo] 
    pathList = []
    # process each child of the start node
    for child in digraph.childrenOf(start):
        if not (child in path[0]):
            paths = bruteDFS(digraph, child, end, newInfo)
            pathList.extend(paths)
    return pathList

## TEST bruteDFS
#graph = WeightedDigraph()
#n0 = Node('0')
#n1 = Node('1')
#n2 = Node('2')
#n3 = Node('3')
#n4 = Node('4')
#n5 = Node('5')
#graph.addNode(n0)
#graph.addNode(n1)
#graph.addNode(n2)
#graph.addNode(n3)
#graph.addNode(n4)
#graph.addNode(n5)
#e1 = WeightedEdge(n0, n1, 2, 1)
#e2 = WeightedEdge(n0, n2, 2, 1)
#e3 = WeightedEdge(n1, n2, 2, 1)
#e4 = WeightedEdge(n2, n3, 2, 1)
#e5 = WeightedEdge(n1, n0, 2, 1)
#e6 = WeightedEdge(n3, n4, 2, 1)
#e7 = WeightedEdge(n3, n5, 2, 1)
#e8 = WeightedEdge(n3, n1, 2, 1)
#e9 = WeightedEdge(n2, n4, 2, 1)
#graph.addEdge(e1)
#
#graph.addEdge(e2)
#graph.addEdge(e3)
#graph.addEdge(e4)
#graph.addEdge(e5)
#graph.addEdge(e6)
#graph.addEdge(e7)
#graph.addEdge(e8)
#graph.addEdge(e9)

#print bruteDFS(graph, n0, n4, ([], 0, 0))

def optiDFS(digraph, start, end, path, maxWeight1, maxWeight2):
    """ 
    DFS Search Method with optimization 
    Input: a digraph, start node, end node, path
        path includes a tuple (list of nodes, totalWeight1, totalWeight2)
    Output: paths from start node to end node
    """
    newPath = list(path[0])
    newWeight1 = path[1]
    newWeight2 = path[2]
    if (len(newPath) > 0):
        lastNode = newPath[-1]
        currentEdge = digraph.getEdge(lastNode, start) 
        newWeight1 += int(currentEdge.getTotalDistance()) 
        newWeight2 += int(currentEdge.getOutdoorDistance())
    newPath.append(start)
    newInfo = (newPath, newWeight1, newWeight2)
    # base cases
    if (newWeight1 > maxWeight1) or (newWeight2 > maxWeight2):
        return []
    elif (start == end):
        return [newInfo] 
    # process each child of the start node
    pathList = []
    for child in digraph.childrenOf(start):
        if not (child in path[0]):
            paths = optiDFS(digraph, child, end, newInfo, maxWeight1, maxWeight2)
            pathList.extend(paths)
    return pathList

#print optiDFS(graph, n0, n4, ([], 0, 0), 5, 5)

#
# Problem 4: Finding the Shorest Path using Optimized Search Method
#
def directedDFS(digraph, start, end, maxTotalDist, maxDistOutdoors):
    """
    Finds the shortest path from start to end using directed depth-first.
    search approach. The total distance travelled on the path must not
    exceed maxTotalDist, and the distance spent outdoor on this path must
	not exceed maxDistOutdoors.

    Parameters: 
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by 
        a list of building numbers (in strings), [n_1, n_2, ..., n_k], 
        where there exists an edge from n_i to n_(i+1) in digraph, 
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    nodeStart = Node(start) 
    nodeEnd = Node(end)
    paths = optiDFS(digraph, nodeStart, nodeEnd, ([], 0, 0), maxTotalDist, maxDistOutdoors)
    # find the paths that satisfy maxTotalDist
    # find the paths that satisfy maxDistOutdoors
    shortestDist = float('inf')
    shortestPath = []
    for eachPath in paths:
        if (eachPath[1] < shortestDist):
            shortestDist = eachPath[1]
            shortestPath = eachPath[0]
    # return value
    if (len(shortestPath) > 0):
        # format the shortest path
        pathPrint = []
        for eachNode in shortestPath:
            pathPrint.append(str(eachNode))
        return pathPrint
    else:
        raise ValueError('No solution available.')

# Uncomment below when ready to test
#### NOTE! These tests may take a few minutes to run!! ####
if __name__ == '__main__':
    #    Test cases
    mitMap = load_map("mit_map.txt")
#    print isinstance(mitMap, Digraph)
#    print isinstance(mitMap, WeightedDigraph)
#    print 'nodes', mitMap.nodes
#    # create a dictionary of edges and follow the annoying format
#    edgeDict = {}
#    for eachNode in mitMap.edges:
#        edgeDict[eachNode] = []
#        for eachEdge in mitMap.edges[eachNode]:
#            dest = eachEdge.getDestination()
#            weight1 = eachEdge.getTotalDistance()
#            weight2 = eachEdge.getOutdoorDistance()
#            edgeDict[eachNode].append([dest, (weight1, weight2)])
#    print 'edges', edgeDict


    LARGE_DIST = 1000000

#     Test case 1
#    print "---------------"
#    print "Test case 1:"
#    print "Find the shortest-path from Building 32 to 56"
#    expectedPath1 = ['32', '56']
#    brutePath1 = bruteForceSearch(mitMap, '32', '56', LARGE_DIST, LARGE_DIST)
#    dfsPath1 = directedDFS(mitMap, '32', '56', LARGE_DIST, LARGE_DIST)
#    print "Expected: ", expectedPath1
#    print "Brute-force: ", brutePath1
#    print "DFS: ", dfsPath1
#    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath1 == brutePath1, expectedPath1 == dfsPath1)

#     Test case 2
#    print "---------------"
#    print "Test case 2:"
#    print "Find the shortest-path from Building 32 to 56 without going outdoors"
#    expectedPath2 = ['32', '36', '26', '16', '56']
#    brutePath2 = bruteForceSearch(mitMap, '32', '56', LARGE_DIST, 0)
#    dfsPath2 = directedDFS(mitMap, '32', '56', LARGE_DIST, 0)
#    print "Expected: ", expectedPath2
#    print "Brute-force: ", brutePath2
#    print "DFS: ", dfsPath2
#    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath2 == brutePath2, expectedPath2 == dfsPath2)

#     Test case 3
#    print "---------------"
#    print "Test case 3:"
#    print "Find the shortest-path from Building 2 to 9"
#    expectedPath3 = ['2', '3', '7', '9']
#    brutePath3 = bruteForceSearch(mitMap, '2', '9', LARGE_DIST, LARGE_DIST)
#    dfsPath3 = directedDFS(mitMap, '2', '9', LARGE_DIST, LARGE_DIST)
#    print "Expected: ", expectedPath3
#    print "Brute-force: ", brutePath3
#    print "DFS: ", dfsPath3
#    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath3 == brutePath3, expectedPath3 == dfsPath3)

#     Test case 4
#    print "---------------"
#    print "Test case 4:"
#    print "Find the shortest-path from Building 2 to 9 without going outdoors"
#    expectedPath4 = ['2', '4', '10', '13', '9']
#    brutePath4 = bruteForceSearch(mitMap, '2', '9', LARGE_DIST, 0)
#    dfsPath4 = directedDFS(mitMap, '2', '9', LARGE_DIST, 0)
#    print "Expected: ", expectedPath4
#    print "Brute-force: ", brutePath4
#    print "DFS: ", dfsPath4
#    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath4 == brutePath4, expectedPath4 == dfsPath4)

#     Test case 5
    print "---------------"
    print "Test case 5:"
    print "Find the shortest-path from Building 1 to 32"
    expectedPath5 = ['1', '4', '12', '32']
    brutePath5 = bruteForceSearch(mitMap, '1', '32', LARGE_DIST, LARGE_DIST)
    dfsPath5 = directedDFS(mitMap, '1', '32', LARGE_DIST, LARGE_DIST)
    print "Expected: ", expectedPath5
    print "Brute-force: ", brutePath5
    print "DFS: ", dfsPath5
    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath5 == brutePath5, expectedPath5 == dfsPath5)

#     Test case 6
    print "---------------"
    print "Test case 6:"
    print "Find the shortest-path from Building 1 to 32 without going outdoors"
    expectedPath6 = ['1', '3', '10', '4', '12', '24', '34', '36', '32']
    brutePath6 = bruteForceSearch(mitMap, '1', '32', LARGE_DIST, 0)
    dfsPath6 = directedDFS(mitMap, '1', '32', LARGE_DIST, 0)
    print "Expected: ", expectedPath6
    print "Brute-force: ", brutePath6
    print "DFS: ", dfsPath6
    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath6 == brutePath6, expectedPath6 == dfsPath6)

#     Test case 7
    print "---------------"
    print "Test case 7:"
    print "Find the shortest-path from Building 8 to 50 without going outdoors"
    bruteRaisedErr = 'No'
    dfsRaisedErr = 'No'
    try:
        bruteForceSearch(mitMap, '8', '50', LARGE_DIST, 0)
    except ValueError:
        bruteRaisedErr = 'Yes'
  
    try:
        directedDFS(mitMap, '8', '50', LARGE_DIST, 0)
    except ValueError:
        dfsRaisedErr = 'Yes'
  
    print "Expected: No such path! Should throw a value error."
    print "Did brute force search raise an error?", bruteRaisedErr
    print "Did DFS search raise an error?", dfsRaisedErr

#     Test case 8
    print "---------------"
    print "Test case 8:"
    print "Find the shortest-path from Building 10 to 32 without walking"
    print "more than 100 meters in total"
    bruteRaisedErr = 'No'
    dfsRaisedErr = 'No'
    try:
        bruteForceSearch(mitMap, '10', '32', 100, LARGE_DIST)
    except ValueError:
        bruteRaisedErr = 'Yes'
  
    try:
        directedDFS(mitMap, '10', '32', 100, LARGE_DIST)
    except ValueError:
        dfsRaisedErr = 'Yes'
  
    print "Expected: No such path! Should throw a value error."
    print "Did brute force search raise an error?", bruteRaisedErr
    print "Did DFS search raise an error?", dfsRaisedErr
