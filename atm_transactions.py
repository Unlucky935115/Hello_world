# Simple ATM System
# Initial savings balance
savings_balance = 1000.0
def deposit(amount):
    """Function to deposit money into the savings account."""
    global savings_balance
    if amount > 0:
        savings_balance += amount
        print(f"Deposited: ${amount:.2f}")
    else:
        print("Deposit amount must be positive.")
def withdraw(amount):
    """Function to withdraw money from the savings account."""
    global savings_balance
    if amount > 0:
        if amount <= savings_balance:
            savings_balance -= amount
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient balance for this withdrawal.")
    else:
        print("Withdrawal amount must be positive.")
def check_balance():
    """Function to check the current savings balance."""
    print(f"Current savings balance: ${savings_balance:.2f}")
def atm_operations():
    """Function to handle ATM operations."""
    while True:
        print("\nChoose an operation:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check balance")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            try:
                amount = float(input("Enter amount to deposit: "))
                deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif choice == '2':
            try:
                amount = float(input("Enter amount to withdraw: "))
                withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif choice == '3':
            check_balance()
        elif choice == '4':
            print("Exiting the ATM system. Thank you!")
            break
        else:
            print("Invalid choice. Please select a valid operation.")
# Start the ATM operations
atm_operations()
