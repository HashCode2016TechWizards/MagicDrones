
class Warehouse:
    contents = {}

    def __init__(self, contents):
        self.contents = contents

    def take(self, itemType, amount):
        if self.contents[itemType] < amount:
            raise Exception #Tried to remove more than we have
        self.contents[itemType] = self.contents[itemType]-amount

    def howMany(self,itemType):
        if self.contents.has_key(itemType):
            return self.contents[itemType]
        else:
            return 0

    def add(slef, itemType, amount):
        if self.contents.has_key(itemType):
            self.contents[itemType] = self.contents[itemType]+amount
        else:
            self.contents[itemType] = amount
