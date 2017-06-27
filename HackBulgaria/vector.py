class Vector:
    def __init__(self):
        self.__capacity = 10
        self.__current_capacity = 0
        self.__storage = [None] * self.__capacity

    def add(self, x):
        """ ADD LAST"""
        if self.__current_capacity + 1 > self.__capacity:
            self.__resize()

        self.__storage[self.__current_capacity] = x
        self.__current_capacity += 1

    def __resize(self):
        print("Resizing Take CARE !")
        new_capacity = self.__capacity * 2 + 1
        new_storage = [None] * new_capacity

        for i in range(len(self.__storage)):
            new_storage[i] = self.__storage[i]
        
        self.__storage = new_storage
        self.__capacity = new_capacity

    def get(self, index):
        return self.__storage[index]

    def __len__(self):
        return self.__current_capacity

    def size(self):
        return len(self)
