with open('wordlist', 'r') as f:
	data = f.readlines()

good_data = [x for x in data if x[3] == 'i' and x[6] == 'c']

print(good_data)		
