#1

class MathDojo(object):
    
    def __init__(self):
        self.start = 0

    def add(self, *args):
        for i in args:
        self.start += i
        return self

    def subtract(self, *args2):
        for i in args2:
            self.start -= i
        return self

    def result(self):
        print self.start


md = MathDojo()

#2

class MathDojo2(object):
    
    def __init__(self):
        self.start = 0

    def add(self, *args):
        for i in args:
            if isinstance(i, (list,tuple)):
                for val in i:
                    self.start += val
            else:
                self.start += i
        print self.start
        return self

    def subtract(self, *args2):
        for i in args2:
            if isinstance(i, (list,tuple)):
                for val in i:
                    self.start -= val
            else:
                self.start -= i
        print self.start
        return self

    def result(self):
        print self.start

md = MathDojo2()
md.subtract([1],3,4)