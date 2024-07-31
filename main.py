class House:
    housesHistory = []

    def __new__(cls, *args, **kwargs):
        cls = object.__new__(cls)
        cls.housesHistory.append(args[0])
        return cls

    def __init__(self, name, numberOfFloors):
        self.name = name
        self.numberOfFloors = abs(numberOfFloors)

    def __len__(self):
        return self.numberOfFloors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.numberOfFloors}'

    def __eq__(self, other):
        if isinstance(other, House):
            return True if self.numberOfFloors == other.numberOfFloors else False
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, House):
            return True if self.numberOfFloors < other.numberOfFloors else False
        else:
            return False

    def __le__(self, other):
        if isinstance(other, House):
            return True if self.numberOfFloors <= other.numberOfFloors else False
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, House):
            return True if self.numberOfFloors > other.numberOfFloors else False
        else:
            return False

    def __ge__(self, other):
        if isinstance(other, House):
            return True if self.numberOfFloors >= other.numberOfFloors else False
        else:
            return False

    def __ne__(self, other):
        if isinstance(other, House):
            return True if self.numberOfFloors != other.numberOfFloors else False
        else:
            return False

    def __add__(self, other):
        if isinstance(other, int):
            self.numberOfFloors = self.numberOfFloors + other
            return self

    def __iadd__(self, other):
        if isinstance(other, int):
            self.numberOfFloors = self.numberOfFloors + other
            return self

    def __radd__(self, other):
        if isinstance(other, int):
            self.numberOfFloors = self.numberOfFloors + other
            return self
        else:
            return False

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

    def goTo(self, newFloor):
        if newFloor <= self.numberOfFloors and newFloor > 0:
            for i in range(1, newFloor + 1):
                print(i)
        else:
            print('Такого этажа не существует')


h1 = House('ЖК Эльбрус', 10)
print(House.housesHistory)
h2 = House('ЖК Акация', 20)
print(House.housesHistory)
h3 = House('ЖК Матрёшки', 20)
print(House.housesHistory)

# Удаление объектов
del h2
del h3

print(House.housesHistory)
