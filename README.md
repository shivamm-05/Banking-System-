# 🏦 Banking System (Python Mini Project)

A menu-driven command-line banking application developed in Python. This project models standard banking workflows such as new account setup, PIN-based user authentication, monetary transactions, fund transfers, and transaction auditing.

---

## 📌 Features

- **Account Creation**: Generates a unique 6-digit account number with user verification (Name, 10-digit Phone, and 4-digit PIN).
- **Secure Login**: Protects account access via Account Number and PIN validation.
- **Account Summary**: Displays complete account holder credentials immediately upon registration, at login, and on-demand via the dashboard.
- **Balance Inquiries**: Check current balance in real time.
- **Deposits & Withdrawals**: Supports cash deposits and withdrawals with balance validation to prevent overdrafts.
- **Inter-Account Transfers**: Move funds seamlessly between two registered user accounts.
- **Transaction History**: Logs timestamps and monetary changes for every deposit, withdrawal, and transfer.
- **Security**: Update and reset security PIN at any time.

---

## 🛠️ Python Concepts Applied

- **Data Structures**: Dictionaries (in-memory account storage) and Lists (transaction logs).
- **Control Flow**: `while` loops, input verification loops, and `if-elif-else` branches.
- **Modular Design**: Functional decomposition using clean Python functions.
- **Built-in Modules**:
  - `random`: Generates unique 6-digit account numbers.
  - `datetime`: Records formatted timestamps for transactions.
- **Error Handling**: Defends against invalid numerical inputs and zero/negative transfers.

---
