pin = 0000
network = ['Airtel','Glo','Mtn','9mobile']
banks = ['Gtb','Zenith','Polaris','Access','Uba']
account_type = ['Savings','Current']
balance = 10000
counter = 0

print('Welcome to the ATM SIMULATOR')
print('Insert your card')

user_pin = int(input('Enter your pin(default is 0000):'))




if user_pin == 0000:
    
    while counter <= 2:
        user_operation = int(input('Enter 1 to Recharge, 2 to Transfer, 3 to Withdraw, 4 to Check Balance:'))
        # Recharge
        if user_operation == 1:
            user_network = input('What network do you want to recharge? :').title()
            if user_network in network:
                amount_to_recharge = int(input('Amount to recharge: '))
                if amount_to_recharge <= balance:
                    num_to_recharge = int(input('Enter 11 digit number to top up:'))
                    confirm_pin = int(input('Re-enter your pin: '))
                    if confirm_pin == 0000:
                        balance = balance - amount_to_recharge
                        print(f'You have succesfully recharged {num_to_recharge} with N{amount_to_recharge} airtime.')
                    else:
                        print("Incorrect Pin.")
                else:
                    print('Insufficient balance to process the transaction.')
            else:
                print("Invalid Network.")

        # Transfer
        elif user_operation == 2:
            user_acct_num = int(input('Enter Account number:'))
            user_bank = input('Enter beneficiary bank: ').title()
            if user_bank in banks:
                amount_to_transfer = int(input('Amount to transfer: '))
                if amount_to_transfer <= balance:
                    confirm_pin = int(input('Re-enter your pin: '))
                    if confirm_pin == 0000:
                        balance = balance - amount_to_transfer
                        print(f'You have succesfully transfered N{amount_to_transfer} to {user_acct_num}.')
                    else:
                        print("Incorrect Pin")
                else:
                    print('Insufficient balance to process the transaction.')
            else:
                print("Bank not available.")
        

        # Withdraw
        elif user_operation == 3:
            amount_to_withdraw = int(input("Enter amount to withdraw: "))
            user_acct = input('Which account(Savings or Current): ').title()
            if user_acct in account_type:
                if amount_to_withdraw <= balance:
                    confirm_pin = int(input('Re-enter your pin: '))
                    if confirm_pin == 0000:
                        balance = balance - amount_to_withdraw
                        print(f'You have succesfully withdrawn N{amount_to_withdraw}.')
                    else:
                        print("Incorrect Pin.")
                else:
                    print('Insufficient balance to process the transaction.')
            else:
                print("Account not available.")

        # Check Balance
        
        elif user_operation == 4:
            print(f'Your account balance is {balance}')

        print("Do you want to run another transaction: ")
        response = input('"yes" to continue, "no" to end:')
        if response == 'yes':
            counter += 1
            continue
        else:
            break

        
    if counter == 3:    
        print("Total amount of transactions on this machine has been met!")
    else:
        print("Thank you for using our services! Have a nice day.")
else:
    print('INCORRECT PIN')







