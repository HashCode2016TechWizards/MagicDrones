import math

class Drone:

    _items = []
    _busy = 0
    position = [0,0]

    def __init__(self,position):
        self.position = position

    def calcWaitTime(self, pos1, pos2):
        return math.sqrt((pos1[0]-pos2[0])**2 + (pos1[1]-pos2[1])**2)

    def move(self,position):
        self._busy = calcWaitTime(self, self.position, position)
        self.position = position

    def load(self,item):
        self._items.add(item)

    def deliver(self,item):
        self._items.remove(item)

    def unload(self,item):
        self._items.remove(item)

    def weight(self):
        m = 0
        for item in self.items:
             m = m + item.weight
        return m

if __name__ == "__main__":
    pos1 = [0,0]
    pos2 = [1,0]
    drone1 = Drone([0,0])
    print drone1.calcWaitTime(pos1,pos2)
