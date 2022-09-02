class Box:
    def __init__(self, name: str, max_weight: int):
        self._name = name
        self._max_weight = max_weight
        self._things = list()
        self.sum_weight = 0

    def add_thing(self, obj):
        self.check_weight(obj)
        self._things.append(obj)

    def check_weight(self, objec):
        self.sum_weight += objec[1]
        if self.sum_weight > self._max_weight:
            raise ValueError('превышен суммарный вес вещей')
        return True


class BoxDefender:
    def __init__(self, box):
        self._box = box
        self._things = box._things[:]

    def __enter__(self):
        return self._box

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self._box._things = self._things




box = Box('Box', 50)
box.add_thing(('orange', 25))
box.add_thing(('lime', 20))
box.add_thing(('banan', 7))
print(box.sum_weight)


