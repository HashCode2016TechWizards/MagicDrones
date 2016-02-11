
import math

class Solver:

    maxload = 1
    products = {}

    def dronesNeeded(order):
        # Get the sum of item weights for this order
        sumweight = sum([products[i] for i in order.items])
        return math.ceil(sumweight/maxload)

    pass
