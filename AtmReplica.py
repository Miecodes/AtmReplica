print('Welcome')
Username = input('Enter Your Name: ')
print(f'Hi {Username}, \nSelect an Option')
print()
Options = ['a. Check Balance', 'b. Deposit', 'c. Withdrawal', 'd. Transfer', 'e. Buy Airtime']
print(*Options, sep='\n')
Balance = 100000


def restart():
    choice = input('Do you want to perform another transaction?(Yes/No): ')
    if choice == 'Yes':
        username = input('Enter Your Name: ')
        print(f'Hi {username}, \nSelect an Option')
        print()
        options = ['a. Check Balance', 'b. Deposit', 'c. Withdrawal', 'd. Transfer', 'e. Buy Airtime']
        print(*options, sep='\n')
        transactions()
    else:
        print('Thanks for using our services')


def transactions():
    print()
    o = input('Accept option: ')
    if o == 'a':
        print(f'Your account balance is {Balance} Naira')
        restart()
    elif o == 'b':
        deposited_amount = int(input('Insert amount to deposit: '))
        print('Accept Deposit')
        new_balance = Balance + deposited_amount
        print(f'Your new balance is {new_balance}')
        restart()
    elif o == 'c':
        amount_to_withdraw = int(input('Amount to Withdraw: '))
        if amount_to_withdraw > Balance:
            print('Insufficient Funds')
        else:
            print('Take your cash')
        restart()
    elif o == 'd':
        input('Recipient Account: ')
        amount_to_transfer = int(input('Amount to transfer: '))
        if amount_to_transfer > Balance:
            print('Insufficient Funds')
        else:
            print('Transaction Successful')
        restart()
    elif o == 'e':
        int(input('Phone number: '))
        network_operators = ['MTN', 'Glo', 'Airtel', '9mobile']
        print(*network_operators, sep='\n')
        network_operator = input('Select Network Operator: ')
        if network_operator == 'MTN' or 'Glo' or 'Airtel' or '9mobile':
            print()
            amount_to_recharge = int(input('Amount To Recharge: '))
            if amount_to_recharge > Balance:
                print('Insufficient Funds')
            else:
                print('Transaction Successful')
        else:
            print('Wrong option chosen')
        restart()
    else:
        print('Invalid Operator')
        restart()


transactions()
