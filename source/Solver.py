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

    def findClosestWarehouseWithAll(self, items, warehouses):
        for wh in warehouses
            if self.containsAll(items):
                return wh
        return False

    def containsAll(self, items, warehouse):
        for item in items
            if warehouse.howMany(item[0]) < item[1]: 
                return False
        return True

    def solve(drones, orders, warehouses):
        availableDrones = drones
        for order in orders:
            wh = findClosestWarehouseWithAll(order.items, warehouses)
            if wh==False:
               break
            loadInstructions = dronesNeeded(order)
            if loadInstructions.length > availableDrones.length:
                break
            availableDrones = self.sortByDistance(self.position, availableDrones)
            for instruction in loadInstructions:
                for itemID in instruction.keys():
                    availableDrones[0].load(itemID, order.items[itemID])
                availableDrones[0].deliverAll(order.coordinates)
                availableDrones.pop(0)
            
