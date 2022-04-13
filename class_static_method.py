class person(object):

    population = 0

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        person.population += 1

    @classmethod #decorator to separate class methods from regular methods.
    def getPopulation(cls):
        return cls.population
    
    @staticmethod #completely independent of the class except for call, also cannot access class properties
    def isAdult(age):
        return age >= 18

    def display(self):
        print(f"{self.name} is {self.age} years old")


newPerson = person('tim', 18)
newPerson2 = person('timmy', 28)

newPerson.display()

print(newPerson.getPopulation())

print(person.isAdult(19))