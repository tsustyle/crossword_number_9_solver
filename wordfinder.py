with open('wordlist', 'r') as f:
	print([x for x in f.readlines() if x[3] == 'i' and x[6] == 'c'])
