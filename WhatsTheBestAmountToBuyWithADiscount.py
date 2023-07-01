discount_percentage = 15
max_amount = 69000
best_amount = 0
max_discount_in_dollars = 0
for value in range(max_amount+1):
    discount = value * discount_percentage / 100

    if discount > max_discount_in_dollars:
        max_discount_in_dollars = discount
        best_amount = value

print(f"You will get ${max_discount_in_dollars} in discounts by buying something thatb costs {best_amount}")
