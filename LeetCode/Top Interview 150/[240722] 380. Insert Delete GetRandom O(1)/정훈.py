from random import randint

class RandomizedSet:
    rs: Set

    def __init__(self):
        self.rs = set()

    def insert(self, val: int) -> bool:
        if val not in self.rs:
            self.rs.add(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val not in self.rs:
            return False
        self.rs.remove(val)
        return True

    def getRandom(self) -> int:
        ri = randint(0, len(self.rs)-1)
        return list(self.rs)[ri]
