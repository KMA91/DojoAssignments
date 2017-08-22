import random

def scores(score):
    for i in range(1, score):
        num = random.randint(60,101)
        if num <= 100 and num >= 90:
            print "Score:", num, ";", "Your grade is A"
        elif num <= 90 and num >= 80:
            print "Score:", num, ";", "Your grade is B"
        elif num <= 80 and num >= 70:
            print "Score:", num, ";", "Your grade is C"
        elif num <= 70 and num >= 60:
            print "Score:", num, ";", "Your grade is D"
        else:
            "F!"
scores(10)