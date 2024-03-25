def main():
    print('Welcome to ABC Bank')
    restart = 'y'
    chances = 3
    balance = 1000

    while chances > 0:
        pin = int(input("Please enter your 4-Digit Pin: "))

        if pin == 1234:
            print('You entered your pin correctly\n')

            while restart.lower() not in ('n', 'no'):
                print('Please press 1 for your balance')
                print('Please press 2 for your withdrawal')
                print('Please press 3 for your pay-in')
                print('Please press 4 for your return card')

                option = int(input('What would you like to choose? '))

                if option == 1:
                    print('Your balance is $', balance)
                    restart = input('Would you like to go back? ')
                elif option == 2:
                    withdraw_amount = float(input('How much would you like to withdraw? $'))
                    if withdraw_amount in [10, 20, 40, 60, 80, 100]:
                        balance -= withdraw_amount
                        print('\nYour balance is now $', balance)
                        restart = input('Would you like to do more? ')
                    else:
                        print('Invalid amount, please retry\n')
                elif option == 3:
                    pay_in = float(input('How much would you like to pay in? $'))
                    balance += pay_in
                    print('\nYour balance is now $', balance)
                    restart = input('Would you like to go back? ')
                elif option == 4:
                    print('Please wait while your card is returned...')
                    print('Thank you for banking with ABC')
                    return
                else:
                    print('Please enter a correct number.\n')
        else:
            print('Incorrect password')
            chances -= 1
            if chances == 0:
                print('\nNo more tries, contact rimshabibi14325@gmail.com')
                return

if __name__ == "__main__":
    main()
