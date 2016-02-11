import Order

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
        for i in range(wareamount):
            # Warehouse coordinate
            self.inputfile.readline()
            # Warehouse contains (dictionary)
            self.inputfile.readline()

        # Orders
        orderamount = int(self.inputfile.readline())
        orders = []
        for i in range(orderamount):
            # Customer coordinates
            coords = [int(i) for i in self.inputfile.readline().split(' ')]
            # Order item amount
            self.inputfile.readline()
            # Item product ids
            items = [int(i) for i in self.inputfile.readline().split(' ')]
            thisorder = Order(coords, items)
            orders.append(thisorder)

        return (products, {}, orders)
