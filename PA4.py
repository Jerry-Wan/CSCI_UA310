WHITE = 0
GRAY = 1
BLACK = 2

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
        self.color = [-1 for i in range(n)]  # variable storing the color
                                             # of each node during DFS
                                             # (WHITE, GRAY, or BLACK)
                                             
        self.parent = [-1 for i in range(n)] # variable storing the parent
                                             # of each node in the DFS forest
                                             
        self.d = [0 for i in range(n)]       # variable storing the discovery time
                                             # of each node in the DFS forest
                                             
        self.f = [0 for i in range(n)]       # variable storing the finish time
                                             # of each node in the DFS forest

# performs a recursive DFS, starting at u
def rec_DFS(u, graph, dfs_info):
    finished = False
    time = u
    #print(time)
    dfs_info.color[u] = 1
    dfs_info.d[u] = time
    cur = graph.A[u]
    #print(cur)
    while cur != None:
        curSucc = cur[0]
        print(curSucc)
        
        if dfs_info.color[curSucc-1] <= 0:
            dfs_info.parent[curSucc-1] = u
            rec_DFS(curSucc-1,graph,dfs_info)
            if finished == True:
                return
        if dfs_info.color[curSucc-1]==1:
            finished = True;
            break;
        cur = graph.A[u]
        print(dfs_info.color)
    dfs_info.color[u] = 2
           
        

# performs a "full" DFS on given graph.
# returns DFSInfo object
def DFS(graph):
    #finished = False
    graphinfo = DFSInfo(graph)
    for i in range(len(graph.A)):
        #print(graphinfo.color[i])
        if graphinfo.color[i] == -1:
            print("Y")
            rec_DFS(i,graph,graphinfo)
        else:
            return
    return graphinfo

# If graph contains a cycle x_1 -> ... x_k -> x_1,
# return the list containing the cycle; otherwise, return None.
# Note: if there is a cycle, you should just return one cycle ---
# it does not matter which one.

# To do this, scan through the edges of the graph,
# using info.f to locate a back edge.
# Once you find a back edge, use info.parent
# to build the list of nodes in the cycle
# in the correct order
def find_cycle(graph, dfs_info):
    result = []
    for a in range(graph.n):
        for b in range(len(graph.A[a])):
            if dfs_info.d[a]<dfs_info.d[b]<dfs_info.f[b]<dfs_info.f[a]:
                result.append(a)
                break
    if len(result) == 0:
        print("0")
        return
    while a != b :
        a = dfs_info.parent[a]
        if a != b:
            result.append(a)
    print("1")
    print(result.reverse)

if __name__ == "__main__":
    roomSet = input()
    roomSet = roomSet.split(" ")
    #print(roomSet)
    graphs = Graph(int(roomSet[0]))
    for a in range(int(roomSet[1])):
        operation = input()
        operationList = operation.split(" ")
        #print(operationList)
        graphs.add_edge(int(operationList[0])-1,int(operationList[1]))
    print(graphs.A)
    Graph_info = DFS(graphs)
    print(Graph_info.f)
    print(Graph_info.d)
    find_cycle(graphs,Graph_info)
