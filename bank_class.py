import sys
from loguru import logger
from user_class import User


class Bank(User):
    def __init__(self, name, age, gender, username, password):
        super().__init__(name, age, gender, username, password)
        self.count = 0
        self.balance = 0
        print(self.name, self.username, self.password)
        logger.info('Initial deposit bonus is 1.5 times today.')

        initial_deposit = input('Do you want to make a first special deposit?Y/N\n')
        if initial_deposit == 'Y' or initial_deposit == 'y':
            money = int(input('How much money do you wish to deposit:\n'))
            self.balance = money * 1.5
            self.ask_questions()
        elif initial_deposit == 'N' or initial_deposit == 'n':
            logger.debug('You miss out on a lucky day!!!')
            self.ask_questions()
        else:
            logger.error('Incorrect input')
            sys.exit()

    def ask_questions(self):
        q1 = input('Do you wish to make a normal deposit?Y/N\n')
        if q1 == 'Y' or q1 == 'y':
            self.deposit()
        elif q1 == 'N' or q1 == 'n':
            logger.info('Thank you for banking with us. Have a good day!!!')
        else:
            logger.error('Incorrect input!!!')
            sys.exit()

        if self.balance == 0:
            logger.error('You have no money in your account. Please add funds to continue.')
            self.deposit()
            self.withdraw()
        elif self.balance > 0:
            q2 = input('Do you wish to make a withdrawal?Y/N\n')
            if q2 == 'Y' or q2 == 'y':
                self.withdraw()
            elif q2 == 'N' or q2 == 'n':
                logger.info('Thank you for banking with us. Have a good day!!!')
        else:
            logger.error('Incorrect input!!!')
            sys.exit()

        q3 = input('Do you wish to view your account balance?Y/N')
        if q3 == 'Y' or q3 == 'y':
            self.view_balance()
        elif q3 == 'N' or q3 == 'n':
            logger.info('Thank you for banking with us. Have a good day!!!')
        else:
            logger.error('Incorrect input!!!')
            sys.exit()

    def check_credentials(self):
        if self.count == 0:
            u_name = input('Please enter your username:\n')
            p_word = input('Please enter your password:\n')
            if u_name == self.username and p_word == self.password:
                pass
                self.count = 1
            else:
                logger.error('Incorrect username or password')
                sys.exit()
        else:
            pass

    def deposit(self):
        print('----DEPOSIT----')
        amount = int(input('Enter the amount to be deposited:\n'))
        self.check_credentials()
        self.balance = self.balance + amount
        logger.debug(f'Account balance has been updated. You have deposited {amount}')
        self.view_balance()

    def withdraw(self):
        print('----WITHDRAWAL----')
        self.check_credentials()
        amount = int(input('Enter the amount to be withdrawn:\n'))
        if self.balance >= amount:
            self.balance = self.balance - amount
            logger.debug(f'Please collect the desired amount {amount}')
        else:
            logger.info('Insufficient account balance.')
            response = input('Do you want to see your balance amount? Y/N\n')
            if response == 'Y' or response == 'y':
                self.view_balance()
            elif response == 'N' or response == 'n':
                logger.info('GoodBye')
            else:
                logger.error('Incorrect input. The session is terminated.')
                sys.exit()

    def view_balance(self):
        print('----VIEW BALANCE----')
        self.check_credentials()
        logger.debug(f'Your current account balance is: {self.balance}')