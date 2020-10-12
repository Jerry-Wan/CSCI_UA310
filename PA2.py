import io
import sys

class Node(object):
    def __init__(self):
        self.guide = None
        self.value = 0
        # guide points to max key in subtree rooted at node


class InternalNode(Node):
    def __init__(self):
        Node.__init__(self)
        self.child0 = None
        self.child1 = None
        self.child2 = None
        # child0 and child1 are always non-none
        # child2 is none iff node has only 2 children


class LeafNode(Node):
    def __init__(self):
        Node.__init__(self)
        # guide points to the key


class TwoThreeTree:
    def __init__(self):
        self.root = None
        self.height = -1


class WorkSpace:
    def __init__(self):
        self.newNode = None
        self.offset = None
        self.guideChanged = None
        self.scratch = [None] * 4


def insert(key, value, tree):
    # insert a key value pair into tree (overwrite existsing value
    # if key is already present)

    h = tree.height

    if h == -1:
        newLeaf = LeafNode()
        newLeaf.guide = key
        newLeaf.value = value
        tree.root = newLeaf
        tree.height = 0

    else:
        ws = doInsert(key, value, tree.root, h)

        if ws != None and ws.newNode != None:
            # create a new root

            newRoot = InternalNode()
            if ws.offset == 0:
                newRoot.child0 = ws.newNode
                newRoot.child1 = tree.root

            else:
                newRoot.child0 = tree.root
                newRoot.child1 = ws.newNode

            resetGuide(newRoot)
            tree.root = newRoot
            tree.height = h + 1

def doInsert(key, value, p, h):
    # auxiliary recursive routine for insert

    if h == 0:
        # we're at the leaf level, so compare and
        # either update value or insert new leaf

        leaf = p  #downcast (unnecessary in python)
        cmp = 0
        if key < leaf.guide:
            cmp = -1
        elif key > leaf.guide:
            cmp = 1

        if cmp == 0:
            leaf.value = value
            return None

        # create new leaf node and insert into tree
        newLeaf = LeafNode()
        newLeaf.guide = key
        newLeaf.value = value

        offset = 1
        if cmp < 0:
            offset = 0
        # offset == 0 => newLeaf inserted as left sibling
        # offset == 1 => newLeaf inserted as right sibling

        ws = WorkSpace()
        ws.newNode = newLeaf
        ws.offset = offset
        ws.scratch = [None] * 4

        return ws

    else:
        q = p  # downcast (unnecessary in python)
        pos = 2
        ws = None
        q.child0.value += q.value
        q.child1.value += q.value
        if q.child2 != None:
            q.child2.value += q.value
        q.value=0

        if key <= q.child0.guide:
            pos = 0
            ws = doInsert(key, value, q.child0, h - 1)

        elif key <= q.child1.guide or q.child2 is None:
            pos = 1
            ws = doInsert(key, value, q.child1, h - 1)

        else:
            pos = 2
            ws = doInsert(key, value, q.child2, h - 1)
        if ws != None:
            if ws.newNode != None:
                # make ws.newNode child # pos + ws.offset of q
                sz = copyOutChildren(q, ws.scratch)

                ws.scratch.insert(pos + ws.offset, ws.newNode)

                if sz == 2:
                    ws.newNode = None
                    ws.guideChanged = resetChildren(q, ws.scratch, 0, 3)
                else:
                    ws.newNode = InternalNode()
                    ws.offset = 1
                    resetChildren(q, ws.scratch, 0, 2)
                    resetChildren(ws.newNode, ws.scratch, 2, 2)

            elif ws.guideChanged:
                ws.guideChanged = resetGuide(q)

        return ws


def copyOutChildren(q, x):
    # copy children of q into x, and return # of children

    sz = 2
    x[0] = q.child0
    x[1] = q.child1
    if q.child2 != None:
        x[2] = q.child2
        sz = 3

    return sz


def resetGuide(q):
    # reset q.guide, and return true if it changes.

    oldGuide = q.guide
    if q.child2 != None:
        q.guide = q.child2.guide
    else:
        q.guide = q.child1.guide

    return q.guide != oldGuide


def resetChildren(q, x, pos, sz):
    # reset q's children to x[pos..pos+sz), where sz is 2 or 3.
    # also resets guide, and returns the result of that

    q.child0 = x[pos]
    q.child1 = x[pos + 1]

    if sz == 3:
        q.child2 = x[pos + 2]
    else:
        q.child2 = None
    return resetGuide(q)

def AddAll(node, amount):
    node.value += amount

def Search(guide,tree,height,nodeList):
    place = tree.root
    nodeList.append(place)
    for a in range(height):
        if guide <= place.child0.guide:
            place = place.child0
            nodeList.append(place)
        elif place.child2 == None or guide <= place.child1.guide:
            place = place.child1
            nodeList.append(place)
        else:
            place = place.child2
            nodeList.append(place)
    return place
            

def AddRange(start,end,tree,amount):
    if start > end:
        a = start
        start = end
        end = a
       
    if tree.height == 0 and start <= tree.root.guide and end >= tree.root.guide:
        AddAll(tree.root,amount)
        return
    
    if tree.height == -1 and tree.root == None:
        print("Error!")
        return 
    
    xList = []
    leafX = Search(start,tree,tree.height,xList)
    
    yList = []
    leafY = Search(end,tree,tree.height,yList)
    #print("The value of last node is",yList[tree.height].guide)
    
    divPoint = 0
    if xList[tree.height].guide != yList[tree.height].guide:
        while xList[divPoint].guide == yList[divPoint].guide:
            divPoint += 1
        divPoint -= 1
    else:
        Leaf = xList[tree.height]
        if Leaf.guide >= start and Leaf.guide <= end:
            AddAll(Leaf,amount)
            return
        return
    
    if xList[tree.height].guide >= start:
        Leafx = xList[tree.height]
        AddAll(Leafx,amount)
        
    p = tree.height-1
    while(p > divPoint):
        node1 = xList[p]
        if xList[p+1].guide == node1.child0.guide:
            AddAll(node1.child1,amount)
            if(node1.child2 != None):
                AddAll(node1.child2,amount)
        elif xList[p+1].guide == node1.child1.guide and node1.child2 != None:
            AddAll(node1.child2,amount)
        p-=1
    
    inter = xList[divPoint]
    if inter.child2!= None:
        if xList[divPoint+1].guide == inter.child0.guide and yList[divPoint+1].guide == inter.child2.guide:
            AddAll(inter.child1,amount)
    
    p = divPoint +1
    while (p<tree.height):
        node2 = yList[p]
        if node2.child2 != None:
            if yList[p+1].guide == node2.child2.guide:
                AddAll(node2.child0,amount)
                AddAll(node2.child1,amount)
            if yList[p+1].guide == node2.child1.guide:
                AddAll(node2.child0,amount)
        else:
            if yList[p+1].guide == node2.child1.guide:
                AddAll(node2.child0,amount)
        p+=1
    
    if yList[tree.height].guide <= end:
        Lefy = yList[tree.height]
        AddAll(Lefy,amount)
        #print("Lefy is", Lefy.guide,Lefy.value)
        #print("successfully add y",start,end)

def FindValue(key,tree):
    place = tree.root
    sums = tree.root.value
    #print("the place guide is now", place.guide)
    #print("the choice of place is:",place.child0.guide,place.child1.guide,place.child2.guide)
    for a in range(tree.height):
        if key <= place.child0.guide:
            place = place.child0
            sums+=place.value
            #print("the place guide is now",place.guide)
            #if type(place) is InternalNode:
                #print("the choice of place is", place.child0.guide,place.child1.guide,place.child2.guide)
        elif place.child2 == None or key <= place.child1.guide:
            place = place.child1
            sums += place.value
            #print("the place guide is now" ,place.guide)
            #if type(place) is InternalNode:
                #print("the choice of place is", place.child0.guide,place.child1.guide,place.child2.guide)
        else:
            place = place.child2
            sums += place.value
            #print("the place guide is now", place.guide)
            #if type(place) is InternalNode:
                #print("the choice of place2 is:",place.child0.guide,place.child1.guide,place.child2.guide)
    if key == place.guide:
        #print("the final guide for place is ", place.guide)
        return sums
    else:
        return -1

def main():
    size = input()
    result = TwoThreeTree()
    for a in range(int(size)):
        operation = input()
        operationList = operation.split(" ")
        #print(operationList)
        if operationList[0] == "1":
            insert(operationList[1],int(operationList[2]),result)
        elif operationList[0] == "2":
            AddRange(operationList[1],operationList[2],result,int(operationList[3]))
        else:
            #print(operationList)
            print(FindValue(operationList[1],result))
            
    
    
main()
