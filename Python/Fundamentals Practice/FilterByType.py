def filter(val):

#Integer

	if type(val) == int:
		if val > 50:
			print "That's a big number!"
		if val < 50:
			print "That's a small number"

#String
	if type(val) == str:
		if len(val) > 50:
			print "Long sentence."
		if len(val) < 50:
			print "Short sentence."

#List
	if type(val) == list:
		if list(val) >= 10:
			print "Big list!"
		if list(val) < 10:
			print "Short list."

