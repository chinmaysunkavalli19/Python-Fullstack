price = float(input("Enter price: "))
coupon = input("Enter coupon code: ").strip().upper()

if coupon == "SAVE20":
    discount = 20
    final_price = price * 0.80
    print("Discount: 20%")
    print("Final price:", final_price)
elif coupon == "SAVE10":
    discount = 10
    final_price = price * 0.90
    print("Discount: 10%")
    print("Final price:", final_price)
else:
    print("Invalid coupon code")
    print("Final price:", price)
