'''
Payment System (Runtime Polymorphism)
An online store supports multiple payment methods: CreditCard, UPI, and
NetBanking. Create a base class Payment with a method process_payment() and
override it in each payment type.
'''

class Payment:
    def process_payment(self):
        print("Only Cash is Accepted here"+"\n")
class CreditCard(Payment):
    def process_payment(self):
        print("Credit Card")
        print("Make your Payment Throught Credit Card"+"\n")
class UPI(Payment):
    def process_payment(self):
        print("UPI Payment")
        print("UPI Payments are Accepted here"+"\n")
class NetBanking(Payment):
    def process_payment(self):
        print("Net Banking")
        print("Complete the Transaction through Net Banking"+"\n")

p=Payment()        
card=CreditCard()
upi=UPI()
NB=NetBanking()

print("Payment process in an Onilne Store"+"\n")

p.process_payment()
print("After Method Overriding!"+"\n")
card.process_payment()
upi.process_payment()
NB.process_payment()