accounts = {
    "1001" : {
        "name" : "Ahmad",
        "balance" : 50000,
        "history" : []
    }
}

def menu():
    """
    This function displays the menu.
    """
    print(12 * "- ")
    print("BANK MANAGEMENT SYSTEM")
    print(12 * "- ")
    print("1. Create account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Transfer Money")
    print("6. Transaction History")
    print("7. Exit")
    print(12 * "- ")

def amount_validation():
    while(True):
        try:
            amount = int(input("Enter amount: "))

            if amount <= 0:
                print("Amount must be Positive!")
                continue
            break
        except ValueError:
            print("Amount must be Integer!")
    return amount
    

def CreateAccount():
    """
    This function helps to create a new account.
    """
    name = input("Enter the name: ").strip().title()
    acc_num = input("Enter account number: ").strip()

    if acc_num in accounts:
        print("Account already exists!")
        return

    accounts[acc_num] = {
        "name": name,
        "balance": 0,
        "history": []
    }

    print("Account created successfully!")


def deposit():
    """
    This function updates the deposited money.
    """
    acc = input("Enter the account number: ").strip()

    if acc not in accounts:
        print("Account not found!")
        return

    amount = amount_validation()

    accounts[acc]["balance"] += amount
    accounts[acc]["history"].append(f"Deposited Rs. {amount}")

    print("Amount deposited successfully!")


def CheckBalance():
    acc = input("Enter account number: ").strip()
    if acc not in accounts:
        print("Account not found!")
        return
    
    print(f"Name: {accounts[acc]['name']}")
    print(f"Balance: {accounts[acc]['balance']} Rs.")


def withdraw():
    """
    This function updates the withdrawl money.
    """
    acc = input("Enter account number: ").strip()
    if acc not in accounts:
        print("Acount not found! ")
        return
    
    amount = amount_validation()

    if accounts[acc]['balance'] >= amount:
        accounts[acc]["balance"] -= amount
        accounts[acc]["history"].append(f"Withdraws Rs. {amount}")
        print("Amount Withdraws Successfully! ")
    else:
        print("Insufficient Balance!")
        input("Press Enter to continue...")


def transfer():
    """
    This function updates the Transfered money.
    """
    sender_acc = input("Enter Sender account number: ").strip()
    if sender_acc not in accounts:
        print("Account not found!")
        input("Press Enter to continue...")
        return
    
    reciever_acc = input("Enter reciever account number: ").strip()
    if reciever_acc not in accounts:
        print("Account not found!")
        input("Press Enter to continue...")
        return
    
    if sender_acc == reciever_acc:
        print("Sender and receiver accounts cannot be the same!")
        return

    amount = amount_validation()

    if accounts[sender_acc]['balance'] >= amount:
        accounts[sender_acc]['balance'] -= amount
        accounts[reciever_acc]['balance'] += amount

        accounts[sender_acc]['history'].append(f"Transferred Rs. {amount} to Account {reciever_acc}")
        accounts[reciever_acc]['history'].append(f"Received Rs. {amount} from Account {sender_acc}")

        print("Transferred Successfully!")
    else:
        print("Low Balance")


def transaction_history():
    acc = input("Enter account number: ").strip()
    if acc not in accounts:
        print("Acount not found! ")
        return
    
    if not accounts[acc]["history"]:
        print("No History")
    else:
        print("History:")
        for transaction in accounts[acc]["history"]:
            print(transaction)

choice = 0
while(choice != 7):
    menu()
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("\nEnter an Integer! ")
        input("Press Enter to continue...")
        continue

    if choice == 1:
        CreateAccount()
    elif choice == 2:
        deposit()
    elif choice == 3:
        withdraw()
    elif choice == 4:
        CheckBalance()
    elif choice == 5:
        transfer()
    elif choice == 6:
        transaction_history()
    elif choice == 7:
        print("Exiting the Program!")
    else:
        print("Wrong Choice!")
