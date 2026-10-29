
class Payment:
    def pay(self, amount):
        print("Processing payment...")


class UPI(Payment):
    def pay(self, amount):
        print("UPI Payment Successful: ₹", amount)


class CreditCard(Payment):
    def pay(self, amount):
        print("Credit Card Payment Successful: ₹", amount)


class Cash(Payment):
    def pay(self, amount):
        print("Cash Payment Successful: ₹", amount)


name = input("Enter Customer Name: ")
amount = float(input("Enter Amount: ₹"))

print("\n1. UPI")
print("2. Credit Card")
print("3. Cash")

choice = input("Choose Payment Method (1/2/3): ")

if amount <= 0:
    print("Invalid amount!")
elif choice == "1":
    payment = UPI()
    payment.pay(amount)
elif choice == "2":
    payment = CreditCard()
    payment.pay(amount)
elif choice == "3":
    payment = Cash()
    payment.pay(amount)
else:
    print("Invalid Payment Method!")
