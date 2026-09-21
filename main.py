import datetime
import random

# In-memory database
# Structure: {account_number: {"name": str, "phone": str, "pin": str, "balance": float, "history": list}}
accounts = {}


def generate_account_number():
    """Generates a unique 6-digit account number."""
    while True:
        acc_num = str(random.randint(100000, 999999))
        if acc_num not in accounts:
            return acc_num


def get_current_timestamp():
    """Returns formatted date and time string."""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def create_account():
    """Creates a new account and displays the newly created account details."""
    print("\n" + "=" * 35)
    print("        CREATE NEW ACCOUNT")
    print("=" * 35)

    name = input("Enter your full name: ").strip()
    if not name:
        print("Error: Name cannot be empty.")
        return

    phone = input("Enter your 10-digit phone number: ").strip()
    if not phone.isdigit() or len(phone) != 10:
        print("Error: Invalid phone number. Must be exactly 10 digits.")
        return

    pin = input("Set a 4-digit PIN: ").strip()
    if not pin.isdigit() or len(pin) != 4:
        print("Error: PIN must be exactly 4 digits.")
        return

    confirm_pin = input("Confirm your 4-digit PIN: ").strip()
    if pin != confirm_pin:
        print("Error: PINs do not match. Account creation aborted.")
        return

    while True:
        try:
            initial_deposit = float(input("Enter initial deposit amount (Min Rs0.00): "))
            if initial_deposit < 0:
                print("Error: Initial deposit cannot be negative.")
                continue
            break
        except ValueError:
            print("Error: Please enter a valid numerical value.")

    acc_num = generate_account_number()
    accounts[acc_num] = {
        "name": name,
        "phone": phone,
        "pin": pin,
        "balance": initial_deposit,
        "history": [],
    }

    if initial_deposit > 0:
        accounts[acc_num]["history"].append(
            f"[{get_current_timestamp()}] Initial Deposit: +Rs{initial_deposit:.2f}"
        )

    # Displays account details immediately after creation
    print("\n" + "-" * 35)
    print("   ACCOUNT CREATED SUCCESSFULLY")
    print("-" * 35)
    print(f"Account Holder : {name}")
    print(f"Phone Number   : {phone}")
    print(f"Account Number : {acc_num}")
    print(f"Current Balance: Rs{initial_deposit:.2f}")
    print("-" * 35)
    print("Please keep your Account Number and PIN safe!")


def view_account_details(acc_num):
    """Displays all profile details of the logged-in user."""
    user = accounts[acc_num]
    print("\n" + "-" * 35)
    print("       ACCOUNT HOLDER DETAILS")
    print("-" * 35)
    print(f"Account Holder : {user['name']}")
    print(f"Account Number : {acc_num}")
    print(f"Phone Number   : {user['phone']}")
    print(f"Current Balance: Rs{user['balance']:.2f}")
    print("-" * 35)


def check_balance(acc_num):
    """Displays the user's current balance."""
    print(f"\nCurrent Balance: Rs{accounts[acc_num]['balance']:.2f}")


def deposit_money(acc_num):
    """Deposits a positive amount into the account."""
    try:
        amount = float(input("\nEnter amount to deposit: Rs"))
        if amount <= 0:
            print("Error: Deposit amount must be greater than zero.")
            return

        accounts[acc_num]["balance"] += amount
        timestamp = get_current_timestamp()
        accounts[acc_num]["history"].append(
            f"[{timestamp}] Deposited: +Rs{amount:.2f}"
        )
        print(f"Deposit Successful! New Balance: Rs{accounts[acc_num]['balance']:.2f}")
    except ValueError:
        print("Error: Invalid numerical amount.")


def withdraw_money(acc_num):
    """Withdraws money after checking for sufficient balance."""
    try:
        amount = float(input("\nEnter amount to withdraw: Rs"))
        if amount <= 0:
            print("Error: Withdrawal amount must be greater than zero.")
            return

        if amount > accounts[acc_num]["balance"]:
            print("Error: Insufficient balance.")
            return

        accounts[acc_num]["balance"] -= amount
        timestamp = get_current_timestamp()
        accounts[acc_num]["history"].append(
            f"[{timestamp}] Withdrew: -Rs{amount:.2f}"
        )
        print(f"Withdrawal Successful! New Balance: Rs{accounts[acc_num]['balance']:.2f}")
    except ValueError:
        print("Error: Invalid numerical amount.")


def transfer_money(acc_num):
    """Transfers funds to another registered account."""
    receiver_acc = input("\nEnter recipient's 6-digit Account Number: ").strip()

    if receiver_acc == acc_num:
        print("Error: Cannot transfer money to your own account.")
        return

    if receiver_acc not in accounts:
        print("Error: Recipient account does not exist.")
        return

    try:
        amount = float(input(f"Enter amount to transfer to {accounts[receiver_acc]['name']}: Rs"))
        if amount <= 0:
            print("Error: Transfer amount must be greater than zero.")
            return

        if amount > accounts[acc_num]["balance"]:
            print("Error: Insufficient funds.")
            return

        accounts[acc_num]["balance"] -= amount
        accounts[receiver_acc]["balance"] += amount

        timestamp = get_current_timestamp()
        accounts[acc_num]["history"].append(
            f"[{timestamp}] Transferred to Acc #{receiver_acc}: -Rs{amount:.2f}"
        )
        accounts[receiver_acc]["history"].append(
            f"[{timestamp}] Received from Acc #{acc_num}: +Rs{amount:.2f}"
        )

        print(f"Transfer Successful! New Balance: Rs{accounts[acc_num]['balance']:.2f}")
    except ValueError:
        print("Error: Invalid numerical amount.")


def view_transaction_history(acc_num):
    """Displays the record of all deposits, withdrawals, and transfers."""
    history = accounts[acc_num]["history"]
    print("\n--- TRANSACTION HISTORY ---")
    if not history:
        print("No transactions on record.")
    else:
        for entry in history:
            print(entry)


def change_pin(acc_num):
    """Allows changing the account PIN after verifying the current PIN."""
    old_pin = input("\nEnter current PIN: ").strip()
    if old_pin != accounts[acc_num]["pin"]:
        print("Error: Incorrect current PIN.")
        return

    new_pin = input("Enter new 4-digit PIN: ").strip()
    if not new_pin.isdigit() or len(new_pin) != 4:
        print("Error: PIN must be exactly 4 digits.")
        return

    confirm_pin = input("Confirm new 4-digit PIN: ").strip()
    if new_pin != confirm_pin:
        print("Error: PIN confirmation does not match.")
        return

    accounts[acc_num]["pin"] = new_pin
    print("PIN successfully updated!")


def account_menu(acc_num):
    """Logged-in user menu loop."""
    while True:
        print("\n" + "=" * 30)
        print("         ACCOUNT MENU")
        print("=" * 30)
        print("1. View Account Details")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Transfer Money")
        print("6. Transaction History")
        print("7. Change PIN")
        print("8. Logout")
        print("=" * 30)

        choice = input("Select an option (1-8): ").strip()

        if choice == "1":
            view_account_details(acc_num)
        elif choice == "2":
            check_balance(acc_num)
        elif choice == "3":
            deposit_money(acc_num)
        elif choice == "4":
            withdraw_money(acc_num)
        elif choice == "5":
            transfer_money(acc_num)
        elif choice == "6":
            view_transaction_history(acc_num)
        elif choice == "7":
            change_pin(acc_num)
        elif choice == "8":
            print("\nLogging out... Returning to Main Menu.")
            break
        else:
            print("Invalid selection. Enter a number between 1 and 8.")


def login():
    """Authenticates account holder and prints their details on successful login."""
    print("\n" + "=" * 30)
    print("         USER LOGIN")
    print("=" * 30)
    acc_num = input("Enter your 6-digit Account Number: ").strip()
    pin = input("Enter your 4-digit PIN: ").strip()

    if acc_num in accounts and accounts[acc_num]["pin"] == pin:
        user = accounts[acc_num]
        print(f"\nLogin Successful! Welcome back, {user['name']}!")
        
        # Displays account holder details right upon login
        print("-" * 35)
        print(f"Logged in as   : {user['name']}")
        print(f"Account Number : {acc_num}")
        print(f"Phone Number   : {user['phone']}")
        print(f"Balance        : Rs{user['balance']:.2f}")
        print("-" * 35)
        
        account_menu(acc_num)
    else:
        print("Error: Invalid Account Number or PIN.")


def main():
    """Main application loop."""
    while True:
        print("\n" + "#" * 32)
        print("     BANKING SYSTEM PORTAL")
        print("#" * 32)
        print("1. Create New Account")
        print("2. Login to Account")
        print("3. Exit System")
        print("#" * 32)

        choice = input("Enter choice (1-3): ").strip()

        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "3":
            print("\nThank you for using the Banking System. Have a Nce Day! Visit Again!")
            break
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()