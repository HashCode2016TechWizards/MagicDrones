from Warehouse import Warehouse
import math

import math

class Solver:

    maxload = 1
    products = {}

    def sortByDistance(self, position, items):
        sortedItems = []
        for item in items:
            distance = math.sqrt((position[0]-item.position[0])**2 + (position[1]-item.position[1])**2)
            sortedItems.append((distance,item))
        sortedItems.sort()
        return sortedItems

    def dronesNeeded(order):
        # Get the sum of item weights for this order
        sumweight = sum([products[i] for i in order.items])
        return math.ceil(sumweight/maxload)
