class EquipmentPool:
    def __init__(self, size):
        self._reusables = [Equipment("Simple Armor", "armor", 1) for _ in range(size)]

    def acquire(self):
        return self._reusables.pop()

    def release(self, reusable):
        self._reusables.append(reusable)


class Equipment:
    name = None
    eqType = None
    bonuses = None

    def __init__(self, name, eqType, bonuses):
        self.name = name
        self.eqType = eqType
        self.bonuses = bonuses

    def changeType(self, eqType):
        self.eqType = eqType

    def printInfo(self):
        print(self.name, self.eqType, self.bonuses)

    pass


def main():
    reusable_pool = EquipmentPool(10)
    reusable = reusable_pool.acquire()
    reusable.printInfo()
    reusable_pool.release(reusable)


if __name__ == "__main__":
    main()
