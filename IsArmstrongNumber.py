def narcissistic( value ):
    the_power = len(value)
    total = 0
    for num in range(value):
        total += num ** the_power
    if total == value:
        return True
    else:
        return False

# Not Finished


