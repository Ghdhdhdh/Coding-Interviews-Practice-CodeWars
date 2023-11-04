numerator = 0

denominator = 0

wholenumber = 0


def getnumerator():
	global numerator
	numerator = int(input("Whats the numerator? "))


def getdenominator():
	global denominator
	denominator = int(input("Whats the denominator? "))


def getwholenumber():
	global wholenumber
	wholenumber = int(input(f"""What the whole number? (As in {numerator}
                              -
                              {denominator} of whole number"""))

while True:
	try:
		getnumerator()
	except:
		print("Invalid Numerator!")
		input("Press any key to try again...")
	else:
		break

while True:
	try:
		getdenominator()
	except:
		print("Invalid Denominator!")
		input("Press any key to try again...")
	else:
		break
	
	
while True:
	try:
		getwholenumber()
	except:
		print("Invalid Whole Number!")
		input("Press any key to try again...")
	else:
		break
		

pass

if wholenumber / denominator * numerator % 2 == 0:
	print(f"{numerator} {denominator}th's of {wholenumber} is {wholenumber // denominator * numerator}")
else:
	print(f"{numerator} {denominator}th's of {wholenumber} is {wholenumber / denominator * numerator}")