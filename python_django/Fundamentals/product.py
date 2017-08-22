class product(object):

    def __init__(self, price, itemname, weight, brand, cost):
        self.price = price
        self.itemname = itemname
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "for sale"
    
    def sell(self):
  
        return self

    def add_tax(self, taxamt):
        print "tax =", taxamt*100, "%"
        self.price = self.price + (self.price*taxamt)
        return self

    def a_return(self, reason):
        if reason == "defective":
            self.status = "defective"
            self.price = 0
        elif reason == "return like new":
            self.status = "for sale"
        elif reason == "open box":
            self.status = "used"
            print "This will receive a 20% discount"
            self.price = self.price*0.20
        return self
    
    def displayInfo(self):
        print "Price:", self.price
        print "Item Name:", self.itemname
        print "Weight:", self.weight
        print "Brand:", self.brand
        print "Cost:", self.cost
        print "Status:", self.status

bike = product(2000, "bike", "10lbs", "MountaiNEER", 1000)
bike.a_return("open box").displayInfo()
bottle = product(50, "bottle", "1lbs", "CRAZYwater", 5)
bottle.sell().displayInfo()
pen = product(350, "pen", "3lbs", "hevypen", 25)
pen.add_tax(0.12).displayInfo()