## Animal is-a object (yes , sort of confusing) look at the extra credit
class Animal(object):
	pass

## Dog is-a Animal
class Dog(Animal):
    
    def __init__(self, name):
        ## Dog has-a name
        self.name = name

## cat is-a Animal  
class Cat(Animal):
    
    def __init__(self, name):
        ## Cat has-a name
        self.name = name

## Person is-a object
class Person(object):
    
    def __init__(self, name):
        ## Person has-a name
        self.name = name
        
        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a Person
class Employee(Person):
    
    def __init__(self, name, salary):
        ## ??
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

##Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog('Rover')

## Satan is-a Cat
satan = Cat('Satan')

## Mary is-a person
mary = Person('Mary')

## Mary has-a pet,..... Pet is-a Cat
mary.pet= satan

## Frank is-a Employee------ Frank is a Person
frank = Employee('Frank', 120000)

## Frank has-a pet,-------- Pet is-a Dog
frank.pet = rover

## Fish has flipper
flipper = Fish()

## ??
crouse = Salmon()

## ??
harry = Halibut()