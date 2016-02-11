

class Drone:

    _items = []

    def move(position):
        pass

    def load(item):
        _items.add(item)

    def deliver(item):
        _items.remove(item)

    def unload(item):
        _items.remove(item)

    def weight():
        m = 0
        for item in items:
             m = m + item.weight
        return m

