from Order import Order
from Warehouse import Warehouse

class ASCII_reader():

    def __init__(self, inputfile):
        self.inputfile = inputfile

    def load_parameters(self):
        # Settings and number of products
        self.inputfile.readline()
        self.inputfile.readline()

        productweights = self.inputfile.readline()
        products = dict(enumerate([int(i) for i in productweights.split(' ')]))

        # Warehouses
        wareamount = int(self.inputfile.readline())
        warehouses = []
        for i in range(wareamount):
            # Warehouse coordinates
            coords = [int(i) for i in self.inputfile.readline().split(' ')]
            # Warehouse contains (dictionary)
            contents = dict(enumerate([int(i) for i in self.inputfile.readline().split(' ')]))
            thiswarehouse = Warehouse(contents, coords)
            warehouses.append(thiswarehouse)

        # Orders
        orderamount = int(self.inputfile.readline())
        orders = []
        for i in range(orderamount):
            # Customer coordinates
            coords = [int(i) for i in self.inputfile.readline().split(' ')]
            # Order item amount
            self.inputfile.readline()
            # Item product ids
            items = {}
            for i in self.inputfile.readline().split(' '):
                if not int(i) in items:
                    items[int(i)] = 1
                else:
                    items[int(i)] += 1
            thisorder = Order(coords, items)
            orders.append(thisorder)

        return (products, warehouses, orders)
