import random

def coin(toss):
    heads = 0
    tails = 0

    print "Starting the program..."

    for count in range(1, toss):
        toss = random.random()
        result = ""
        if toss >= 0.50:
            heads += 1
            result = "head"
        if toss <= 0.50:
            tails += 1
            result = "tail"
        print "Attempt #", count, ": Throwing a coin... It's a", result, "... Got", heads, "head(s) so far and", tails, "tail(s) so far"


coin(5001)