# -------- Welcome to ATM --------

atm_pin = "1234"
transaction_pin = "7890"

print("-------- Welcome to ATM --------")
name = input("Enter your name: ")
entered_pin = input("Enter your PIN: ")

if entered_pin == atm_pin:
   
    balance = 50000
    print(f"\nHello {name}, your available balance is ₹{balance}")
    
    withdraw_amount = int(input("How much do you want to withdraw? ₹"))
    
    if withdraw_amount > balance:
        print("Insufficient balance.")
    else:
        entered_trx_pin = input("Enter your transaction PIN: ")
        
        if entered_trx_pin == transaction_pin:
            balance -= withdraw_amount
            print(f"Your amount ₹{withdraw_amount} is successfully withdrawn.")
            print(f"Your current balance is ₹{balance}")
        else:
            print("Incorrect transaction PIN.")
else:
    print("Incorrect ATM PIN.")
