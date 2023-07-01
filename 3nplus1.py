i = 1
while True:
    # setup for each number
    amountOfLoops = 0
    has1beenreached = False
    has4beenreached = False
    has2beenReached = False
    num = i
    # Test
    while True:
        # 3x+1 case
        if num % 2 == 1:
            num *= 3
            num += 1
        # x/2 case
        elif num % 2 == 0:
            num /= 2
        # Check if num is 4,2 or 1 to test for possible loop
        if num == 4:
            has4beenreached = True
        elif num == 2:
            has2beenReached = True
        elif num == 1:
            # Check for loop
            has1beenreached = True
            amountOfLoops += 1
            if amountOfLoops == 2:
                print(f'{i} has returned true')
                i += 1
                break
            else:
                print(f'{i} Has returned False')
                with open('3nplus1FAILED.txt', 'a') as file:
                    file.write(i)

# start at any number
# if the number is odd, multiply it by 3 and add 1
# if it is even, divide by 2
