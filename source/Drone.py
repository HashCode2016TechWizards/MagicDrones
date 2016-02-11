import math

class Drone:

    _items = []
    _busy = 0
    position = [0,0]

    def __init__(self,position):
        self.position = position

    def calcWaitTime(self, pos1, pos2):
        return math.sqrt((pos1[0]-pos2[0])**2 + (pos1[1]-pos2[1])**2)

    def readyIn():
        return self._busy

    def checkIfBusy(self):
        if (self._busy > 0):
            raise Exception

    def move(self,position):
        self.checkIfBusy()
        self._busy = calcWaitTime(self, self.position, position)
        self.position = position

    def load(self, item, warehouse):
        self.move(warehouse.position)
        self._items.add(item)
        self._busy = self._busy+1

    def deliver(self, item, position):
        self.move(position)
        self._items.remove(item)
        self._busy = self._busy+1

    def unload(self, item, warehouse):
        self.move(warehouse.position)
        self._items.remove(item)
        self._busy = self._busy+1

    def wait(self, time):
        self._busy = self._busy+time

    def weight(self):
        m = 0
        for item in self.items:
             m = m + item.weight
        return m
