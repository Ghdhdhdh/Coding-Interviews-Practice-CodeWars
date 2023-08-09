for first in range(0, 9999):
	for second in range(0, 9999):
		if not first == 0 or second == 0:
			try:
				if first // second == first / second:
					# division
					# print(f"{first} divided by {second} equals {first // second}")
					# fact familys
					print(f"{first} {second} {first // second}")
			except ZeroDivisionError:
				pass