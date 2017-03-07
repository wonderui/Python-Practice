## define a class named Animal
## pass is nothing
class Animal(object):
	pass

## define a class named Dog inherit from Animal
## a Dog must have a parameter named name	
class Dog(Animal):
	def __init__(self, name):
		self.name = name

## the same as a Dog
class Cat(Animal):
	def __init__(self, name):
		self.name = name

## the same as Dog and Cat
class Person(object):
	def __init__(self, name):
		self.name = name
		self.pet = None

## define a class named Employee inherit from Person
## an Employee must have 2 parameter: name and salary
## super(Employee, self) is the same as Person
class Employee(Person):
	def __init__(self, name, salary):
		super(Employee, self).__init__(name)
		self.salary = salary

## define a class named Fish		
class Fish(object):
	pass

## define a class named Salmon inherited from Fish
class Salmon(Fish):
	pass

## define a class named Halibut inherited from Fish
class Halibut(Fish):
	pass

## create a Dog instance named rover, its name is Rover
rover = Dog("Rover")

satan = Cat("Satan")

mary = Person("Mary")

## satan is a cat called Satan and now its Mary's pet
mary.pet = satan

## frank is a Person called Frank, also an Employee, his salary is 120000
frank = Employee("Frank", 120000)

## now Rover is Frank's pet
frank.pet = rover

flipper = Fish()

crouse = Salmon()

harry = Halibut()

print frank.salary
