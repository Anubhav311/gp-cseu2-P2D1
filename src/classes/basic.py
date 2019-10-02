# create a basic Animal class add some getter and setter methods

class Animal:
    # constructor
    def __init__(self, name, num_legs):
        self.name = name
        self.num_legs = num_legs

    # methods

    # getters
    def getName(self):
        return self.name

    def getLegs(self):
        return self.num_legs

    # setters
    def setName(self, name):
        self.name = name

    def set_legs(self, num_legs):
        self.num_legs = num_legs


a = Animal("Bob", 20)
a.name = "Dave"
a.age = 23