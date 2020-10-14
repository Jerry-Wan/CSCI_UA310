class fighter():
    def __init__(self,name,score,position):
        self.name = name
        self.score = score
        self.position = position
        
class Heap:
    def __init__(self,capacity):
        self._heap = []
        self._capacity = capacity
        self._size = 0
        
    def __len__(self):
        return len(self._heap)
       
    def isEmpty(self):
        return len(self) == 0
    
    def add(self,fighter):
        if self.getSize() == self.getCapacity():
            return
        self._size += 1
        #print(position)
        self._heap.append(fighter)
        self._upheap(len(self._heap)-1)
    
    def getSize(self):
        return self._size
    
    def getCapacity(self):
        return self._capacity
             
    def _getParent(self,position):
        return(position-1)//2
       
    def _getLeft(self,position):
        return 2*position +1
    
    def _getRight(self,position):
        return 2*position +2
    
    def _hasLeft(self,position):
        return self._getLeft(position) < len(self._heap)
    
    def _hasRight(self,position):
        return self._getRight(position) < len(self._heap)
   
    def _swap(self, i, j):
        t = self._heap[i].position
        self._heap[i].position = self._heap[j].position
        self._heap[j].position = t
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]
        
    def _upheap(self,position):
        parent = self._getParent(position)
        if position >0 and self._heap[position].score < self._heap[parent].score:
            self._swap(position,parent)
            self._upheap(parent)
        
    def _downheap(self,position):
        if self._hasLeft(position):
            left = self._getLeft(position)
            smallChild = left
            if self._hasRight(position):
                right = self._getRight(position)
                if self._heap[right].score < self._heap[left].score:
                    smallChild = right
            if self._heap[smallChild].score < self._heap[position].score:
                self._swap(position, smallChild)
                self._downheap(smallChild)    
                
    def getPosition(self,name):
        for a in self._heap:
            if a.name == name:
                return self._heap.index(a)
        
    def getMin(self):
        if self.isEmpty():
            raise Empty("Sorry, the heap is empty!")
        return self._heap[0]
    
    def getLast(self):
        if self.isEmpty():
            raise Empty("Sorry, the heap is empty!")
        return self._heap[size-1]
    
    def getScore(self,position):
        if self.isEmpty():
            raise Empty("Sorry, the heap is empty!")
        return self._heap[position].score
    
    def removeMin(self):
        if self.isEmpty():
            raise Empty("Sorry, the heap is empty!")
        self._swap(0,len(self._heap)-1)
        item = self._heap.pop()
        self._size -=1
        self._downheap(0)
        return(item)
    
    def addScore(self,position,amount):
        self._heap[position].score += amount
        self._downheap(position)
        
        
def main():
    fighterDict = {}
    
    capacity = input()
    fighterHeap = Heap(capacity)
    for a in range(int(capacity)):
        info = input()
        infoList = info.split(" ")
        fight = fighter(infoList[0],int(infoList[1]),len(fighterHeap))
        
        fighterHeap.add(fight)
        fighterDict[fight.name] = fight
        
    order = input()
    for a in range(int(order)):
        operation = input()
        operationList = operation.split(" ")
        #print(operationList)
        if int(operationList[0]) == 1:
            #print(fighterDict)
            position = fighterDict.get(operationList[1]).position
            fighterHeap.addScore(position,int(operationList[2]))
            #fighterDict[operationList[1]] = fighterHeap.getPosition(operationList[1])
        elif int(operationList[0]) == 2:
            standard = int(operationList[1])
            #print(standard)
            #for a in fighterHeap._heap:
                #print(a.name,a.score)
            #print(fighterHeap.getMin().score)
            while fighterHeap.getMin() != None and fighterHeap.getMin().score < standard:
                min = fighterHeap.removeMin()
                fighterDict.pop(min.name)
            #for a in fighterDict.keys():
                #print(a, fighterDict.get(a).score, fighterDict.get(a).score<standard)
            print(len(fighterDict))
            
        

main()
