sys.setrecursionlimit(10000)

# Data structure for representing a graph
class Graph():
    # initalize a graph with n vertices and no edges
    def __init__(self, n):
        self.n = n # number of nodes in the graph
        self.A = [[] for i in range(n)]
        # For u in [0..n), A[u] is the adjacency list for u

    # add an edge u -> v to the graph
    def add_edge(self, u, v):
        self.A[u].append(v)

# Data structure holding data computed by DFS
class DFSInfo():
    def __init__(self, graph):
        n = graph.n
        self.k = 0                      # number of trees in DFS forest
        self.T = [0 for i in range(n)]  # For u in [0..n), T[u] is initally 0, but when DFS discovers
                                        # u, T[u] is set to the index (which is in [1..k]) of the tree
                                        # in DFS forest in which u belongs.
                                             
        self.L = [-1 for i in range(n)] # List of nodes in order of decreasing finish time
                                             
        self.count = n                  # initially set to n, and is decremented every time
                                        # DFS finishes with a node and is recorded in L

# performs a recursive DFS, starting at u
def rec_DFS(u, graph, dfs_info):
    k+=1
    self.T[u] = k
    while u != None:
        if dfs_infoT[u-1] == 0:
            rec_DFS(u-1,graph,dfs_info)
        curSucc = graphA[u][0]
    
    
    

# performs a "full" DFS on given graph, processing
# nodes in the order specified (i.e., order[0], order[1], ...)
# in the main loop.
# returns DFSInfo object.
def DFS(order, graph):
    graphinfo = DFSInfo(graph)
    for a in range(len(self.A)):
        if DFSInfo.T[a] == 0:
            rec_DFS(a,graph,graphinfo)

    return graphinfo

# returns a boolean array indicating which nodes
# are safe nodes. The dfs_info is that computed from the
# second DFS.
def compute_safe_nodes(graph, dfs_info):

    return None

# returns the reverse of the given graph
def reverse(graph):
    revgraph = Graph(graph.n)
    for a in range(len(graph.A)):
        for b in range(len(a)):
            revgraph.add_edge(b,a)
    return revgraph

if __name__ == "__main__":
    mapinfo = input()
    infolist = mapinfo.split(" ")
    maps = Graph(int(infolist[0]))
    for a in range(int(infolist[1])):
        addop = input()
        addlist = addop.split(" ")
        maps.add_edge(int(addlist[0]),int(addlist[1]))
    mapsinfo = DFSInfo(maps)
    safe = computer_safe_nodes(maps,mapsinfo)
    for a in range(len(safe)):
        if safe(a) == True:
            print(a,end = " ")
    
    
