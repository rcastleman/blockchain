# hash test

from hashlib import sha256

x = 9
y = 0

# while sha256(f'{x*y}'.encode()).hexdigest()[-1] !="0":
	# y += 1

while sha256(f'{x*y}'.encode()).hexdigest()[-1] != "0":
	    y += 1

print(f'the solution is y = {y}')