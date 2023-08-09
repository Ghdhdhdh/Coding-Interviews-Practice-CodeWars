for threedigit in range(100,999):
	for onedigit in range(1,9):
		answer = threedigit / onedigit
		if answer == threedigit // onedigit:
			pass
		else:
			continue
	#Zero Checks
	for number in str(threedigit):
		if number == 0:
			break
		break
	continue
	
	for number in str(onedigit):
		if number == 0:
			break
		break
	continue
	
	for number in str(answer):
		if number == 0:
			break
		break
	continue
	
	#No Repeat Check
	
	usednumbers = []
	
	for number in str(threedigit):
		if number in usednumbers:
			break
		else:
			usednumbers.append(number)
		
	continue
	
	for number in str(onedigit):
		if number in usednumbers:
			break
		else:
			usednumbers.append(number)
	
	continue
	
	for number in str(answer):
		if number in usednumbers:
			break
		else:
			usednumbers.append(number)
	
	continue
	
	print(f"{threedigit} / {onedigit} = {answer}")