def find(list):
    letters = set("o")
    for word in list:
        if letters & set(word):
            print word

find(['hello','2','smell'])