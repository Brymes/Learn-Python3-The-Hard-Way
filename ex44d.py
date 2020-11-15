class Parent(object):

    def override(self):
        print('PARENT override()')
    
    def implicit(self):
        print("PARENT implicit()")
    
    def altered(self):
        print('PARENT altered()')

class Child(Parent):

    def override(self):
        print('CHILD override()')
    
    def altered(self):
        print('CHILD, BEFORE PARENT altered')
        super(Child, self).altered()
        print('CHILD, AFTER PARENT altered()')

dad = Parent()
son = Child()

# both print the same output
dad.implicit()
son.implicit()

#Parent prints self...Child prints ('CHILD override()')
dad.override()
son.override()

#Prints self
dad.altered()
#prints before, parent, then after
son.altered()