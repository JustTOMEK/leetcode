import random
class RandomizedSet:

    def __init__(self):
        self.items = []
        self.indexes = {}
        self.current_index = 0

    def insert(self, val: int) -> bool:
        if val in self.indexes:
            return False
        else:
            self.indexes[val] = self.current_index
            self.current_index += 1
            self.items.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val not in self.items:
            return False
        else:
            index = self.indexes[val]
            self.items[index] = self.items[-1]
            self.indexes[self.items[-1]] = index
            del self.indexes[val]
            self.items.pop()
            self.current_index -= 1
            return True

    def getRandom(self) -> int:
        return random.choice(self.items)
