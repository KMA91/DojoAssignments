class Call(object):
    def __init__(self, an_id, name, number, time, reason):
        self.id = an_id
        self.name = name
        self.number = number
        self.time = time
        self.reason = reason
    
    def display(self):
        print "Unique id:", self.id
        print "Caller name:", self.name
        print "Caller phone number:", self.number
        print "Time of call", self.time
        print "Reason for call:", self.reason
        return self
    
class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue = 0

    def add(self, new):
        self.calls.append(new)
        self.queue += 1
        return self

    def remove(self):
        if self.queue <= 0:
            del self.calls[0]
            self.queue -= 1
        return self

    def getinfo(self):
        for calls in self.calls:
            print calls.number
        print self.queue

    def remove_num(self, num):
        

call1 = Call(1, "kevin", "555", "10:05AM", "hungry")
call2 = Call(1, "steven", "123", "10:10AM", "bored")
# call3 = Call(1, "eric", "245", "10:10AM", "bored")
center1 = CallCenter()
center1.add(call1).add(call2).getinfo().remove().getinfo()
print "Reuben is the best"