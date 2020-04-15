text = open("1155107970.txt", 'r')

sum_positive = 0
sum_negative = 0
total = 0

for line in text:
	line = line.strip()
	words = line.split()
	for w in words:
		while(not w[0].isalpha):
			w = w[1:]
		while(not w[-1].isalpha):
			w = w[:-1]

		total += 1
		if w in positive:
			sum_positive += 1
		if w in negative:
			sum_negative += 1

print("Score:")
print((sum_positive - sum_negative) / total)

