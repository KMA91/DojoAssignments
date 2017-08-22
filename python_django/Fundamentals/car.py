class car(object):
    
    def __init__(self, price, speed, fuel, mileage):
        self.tax = 0
        if price > 10000:
            self.price = price*1.15
            self.tax = 0.15
        else:
            self.price = price*1.12
            self.tax = 0.12
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
    
    def display_all(self):
        print "Price:", self.price
        print "Speed:", self.speed
        print "Fuel:", self.fuel
        print "Mileage:", self.mileage
        print "Tax:", self.tax

car1 = car(2000, "25mph", "Full", "15mpg")
car1.display_all()
car2 = car(4000, "35mph", "5/6", "25mpg")
car2.display_all()
car3 = car(10000, "45mph", "4/6", "35mpg")
car3.display_all()
car4 = car(12000, "55mph", "3/6", "45mpg")
car4.display_all()
car5 = car(20000, "65mph", "2/6", "55mpg")
car5.display_all()
car6 = car(40000, "75mph", "Empty", "65mpg")
car6.display_all()