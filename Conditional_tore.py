purchase_amount = int(input("How mush is your purchase? "))
if purchase_amount > 50000:
    discount_amount = (purchase_amount // 5)
    new_amount = purchase_amount - discount_amount
    print(new_amount)
elif 2000 < purchase_amount < 50000:
    discount_amount = (purchase_amount // 10)
    new_amount = purchase_amount - discount_amount
    print(new_amount)
else:
    new_amount = purchase_amount
    print(new_amount)