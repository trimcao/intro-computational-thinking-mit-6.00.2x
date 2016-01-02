# 6.00.2x Problem Set 5
# Graph optimization
#
# A set of data structures to represent graphs
#

class Node(object):
    def __init__(self, name):
        self.name = str(name)
    def getName(self):
        return self.name
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name
    def __eq__(self, other):
        return self.name == other.name
    def __ne__(self, other):
        return not self.__eq__(other)
    def __hash__(self):
        # Override the default hash method
        # Think: Why would we want to do this?
        return self.name.__hash__()

class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return '{0}->{1}'.format(self.src, self.dest)

class Digraph(object):
    """
    A directed graph
    """
    def __init__(self):
        # A Python Set is basically a list that doesn't allow duplicates.
        # Entries into a set must be hashable (where have we seen this before?)
        # Because it is backed by a hashtable, lookups are O(1) as opposed to the O(n) of a list (nifty!)
        # See http://docs.python.org/2/library/stdtypes.html#set-types-set-frozenset
        self.nodes = set([])
        self.edges = {}
    def addNode(self, node):
        if node in self.nodes:
            # Even though self.nodes is a Set, we want to do this to make sure we
            # don't add a duplicate entry for the same node in the self.edges list.
            raise ValueError('Duplicate node')
        else:
            self.nodes.add(node)
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    def childrenOf(self, node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.nodes
    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[str(k)]:
                res = '{0}{1}->{2}\n'.format(res, k, d)
        return res[:-1]

class WeightedEdge(Edge):
    """
    Subclass WeightedEdge from Edge
    """
    def __init__(self, src, dest, weight1, weight2):
        Edge.__init__(self, src, dest)
        self.weight1 = weight1
        self.weight2 = weight2
    def __str__(self):
        return str(self.src) + "->" + str(self.dest) + " (" + str(self.weight1) \
                    + ", " + str(self.weight2) + ")"
    def getTotalDistance(self):
        return self.weight1
    def getOutdoorDistance(self):
        return self.weight2

class WeightedDigraph(Digraph):
    """
    Weighted version of Digraph class
    """
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(edge)

    def childrenOf(self, node):
        children = []
        for edge in self.edges[node]:
            children.append(edge.getDestination())
        return children
    
    def getEdge(self, src, dest):
        for edge in self.edges[src]:
            if (edge.getDestination() == dest):
                return edge
        raise ValueError('Edge not in graph')

    def __str__(self):
        s = ""
        for node in self.nodes:
            for edge in self.edges[node]:
                edgeInfo =  str(edge.getSource()) + "->" + str(edge.getDestination()) + " (" + \
                    str(float(edge.getTotalDistance())) + ", " + str(float(edge.getOutdoorDistance())) + ")"
                s += edgeInfo
                s += '\n'
        return s


### TEST Weighted Digraph
#g = WeightedDigraph()
#na = Node('a')
#nb = Node('b')
#nc = Node('c')
#g.addNode(na)
#g.addNode(nb)
#g.addNode(nc)
#e1 = WeightedEdge(na, nb, 15, 10)
#print e1
#e2 = WeightedEdge(na, nc, 14, 6)
#e3 = WeightedEdge(nb, nc, 3, 1)
#print e2
#print e3
#g.addEdge(e1)
#g.addEdge(e2)
#g.addEdge(e3)
#print g

#nx = Node('x')
#ny = Node('y')
#nz = Node('z')
#e1 = WeightedEdge(nx, ny, 18, 8)
#e2 = WeightedEdge(ny, nz, 20, 1)
#e3 = WeightedEdge(nz, nx, 7, 6)
#g = WeightedDigraph()
#g.addNode(nx)
#g.addNode(ny)
#g.addNode(nz)
#g.addEdge(e1)
#g.addEdge(e2)
#g.addEdge(e3)
#print g

#nj = Node('j')
#nk = Node('k')
#nm = Node('m')
#ng = Node('g')
#g = WeightedDigraph()
#g.addNode(nj)
#g.addNode(nk)
#g.addNode(nm)
#g.addNode(ng)
#randomEdge = WeightedEdge(nj, ng, 76, 24)
#g.addEdge(randomEdge)
#randomEdge = WeightedEdge(nj, ng, 46, 30)
#g.addEdge(randomEdge)
#randomEdge = WeightedEdge(nm, nk, 83, 22)
#g.addEdge(randomEdge)
#randomEdge = WeightedEdge(ng, nj, 37, 32)
#g.addEdge(randomEdge)
#randomEdge = WeightedEdge(nm, nj, 89, 58)
#g.addEdge(randomEdge)
#randomEdge = WeightedEdge(ng, nj, 18, 14)
#g.addEdge(randomEdge)
#randomEdge = WeightedEdge(nj, ng, 71, 48)
#g.addEdge(randomEdge)
#randomEdge = WeightedEdge(nj, nm, 91, 45)
#g.addEdge(randomEdge)
#print g
