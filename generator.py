import random

LINES = 10
LENGTH = 70
LETTERS = 'CGAT'

for _ in range(LINES):
	for _ in range(LENGTH):
		print(random.choice(LETTERS), end = '')
	print()
