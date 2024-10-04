# ATM Project

A simple, Python-based ATM (Automated Teller Machine) simulation. This project provides basic ATM functionalities such as balance inquiry, money withdrawal, deposits, fund transfers, and receipt generation.

## Features

- **Check Balance**: View your current account balance.
- **Withdraw Funds**: Withdraw money from your account.
- **Deposit Funds**: Deposit money into your account.
- **Transfer Funds**: Transfer money to another account.
- **Receipt Generation**: Get a receipt showing transaction history after exiting.

## Getting Started

### Prerequisites

- **Python 3.x**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

### Running the Program

1. Clone this repository or download the code.
   ```bash
   git clone https://github.com/Ayesha-khoja/ATM-python.git

   ```
2. Run the ATM program using Python:
   ```bash
   python ATM-python/atm.py
   ```

3. On running the program, you'll be prompted to enter your **username** and **password** for authentication. The default credentials are:

   - **Username**: Ayesha
   - **Password**: khoja90

   You can change these credentials in the `authen` method within the code.

4. Once authenticated, the main menu will appear, allowing you to:
   - Check your balance.
   - Withdraw, deposit, or transfer funds.
   - Exit the program and optionally generate a receipt for your transactions.

## ATM Operations

- **Check Balance**: View your account balance.
- **Withdraw**: Enter the amount you'd like to withdraw.
- **Deposit**: Add funds to your account by entering the deposit amount.
- **Transfer**: Transfer money by providing the recipient's account number and name.
- **Exit**: Choose to exit the system. You will be asked if you'd like to generate a receipt displaying:
  - Current balance.
  - Total withdrawals.
  - Deposits made.
  - Transfers processed.

## Modifying Authentication

To change the default username and password, simply edit the `authen` method in the code. Update the values for username and password as needed.

```python
def authen():
    username = "Ayesha"
    password = "khoja90"
```

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, feel free to:

1. Open an issue on this repository.
2. Submit a pull request with your improvements.

### Guidelines for Contributions:
- Ensure your changes are properly tested.
- Follow Python coding standards and conventions.
- Include descriptive commit messages and documentation where necessary.

## License

This project is open-source and available under the [MIT License](LICENSE).

---
