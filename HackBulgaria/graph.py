class Panda:
    def __init__(self, name, email, gender):
        self.__name = name
        self.__email = email
        self.__gender = gender

    def __eq__(self, other):
        if hash(self) == hash(other):
            return True
        return False

    def __hash__(self):
        return hash(str(self))

    def __str__(self):
        return "{} {} {}".format(self.__name, self.__email, self.__gender)

    def name(self):
        return self.__name

    def email(self):
        return self.__email

    def gender(self):
        return self.__gender

    def isMale(self):
        if self.__gender is 'male':
            return True
        return False

    def isFemale(self):
        if self.__gender is not 'male':
            return True
        return False


class PandaSocialNetwork:
    def __init__(self):
        self.__network = {}

    def add_panda(self, panda):
        self.__network.update(panda)

    def friends_of(self, panda):
        if panda not in self.__network:
            return False






