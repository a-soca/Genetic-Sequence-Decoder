import random

code=""
for i in range(300):
	code = code + codons[random.randint(1,4)]
	
print(code)
