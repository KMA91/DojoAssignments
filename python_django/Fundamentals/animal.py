class Animal(object):
    
    def __init__(self, name):
        self.name = name
        self.health = 100

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 11
        return self

    def displayHealth(self):
        print "Name is:", self.name
        print "Health is:", self.health
        return self

class Dog(Animal):
    
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150

    def pet(self):
        self.health += 5
        return self

doge = Dog("kevin")
doge.walk().walk().walk().run().run().pet().displayHealth()

class Dragon(Animal):

    def __init__(self, name):
        super(Dragon, self).__init__(name)
        print "This is a dragon!"
        self.health = 170

    def fly(self):
        self.health -= 10
        return self

toothless = Dragon("steven")
toothless.walk().walk().walk().run().run().fly().fly().displayHealth()
toothless.displayHealth()