class Call(object):
    
    def __init__(self, call_id, caller_name, caller_pnumber, time, reason):
        self.call_id = call_id
        self.caller_name = caller_name
        self.caller_pnumber = caller_pnumber
        self.time = time
        self.reason = reason

    def displayall(self):
        ListInfo=[self.call_id, self.caller_name, self.caller_pnumber, self.time, self.reason]
        # print ListInfo
        return ListInfo

call1=Call(1,"chen",12155,5.15,"why")
call2=Call(2,"chen",21277,2.25,"hi")
call3=Call(3,"chen",13123,0.15,"ho")
call4=Call(4,"chen",35446,1.25,"ha")
call5=Call(5,"chen",23244,3.36,"h8")
call6=Call(6,"chen",25454,8.12,"yo")
# call1.displayall()

class CallCenter(object):

    def __init__(self):
        self.calls = []
        self.queue_length=0
        
    def add(self, new):
        self.calls.append(new.displayall())
        self.queue_length+=1
        print self.calls
        #print self.queue_length
        return self

    def remove(self):
        del self.calls[0]
        self.queue_length-=1
        return self

    def info(self):
        print self.calls
        print self.queue_length
        return self

    def findremove(self,caller_pnumber):
        for i in self.calls:
            if i[2]==caller_pnumber:
                self.calls.remove(i)
                self.queue_length-=1
        return self

    def sortsbytime(self):
        self.calls = sorted(self.calls, key=itemgetter(3))
        return self

center1=CallCenter()
center1.add(call1).info()
# .add(call2).remove()
# .add(call3).add(call4).add(call5).add(call6).remove().findremove(13123).sortsbytime().info()