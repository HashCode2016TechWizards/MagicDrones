from Warehouse import Warehouse
import math

class Solver:

    def sortByDistance(self, position, items):
        sortedItems = []
        for item in items:
            distance = math.sqrt((position[0]-item.position[0])**2 + (position[1]-item.position[1])**2)
            sortedItems.append((distance,item))
        sortedItems.sort()
        return sortedItems

