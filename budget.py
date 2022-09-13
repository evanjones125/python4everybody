import math

class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []
        self.balance = 0

    def __str__(self):
        output = ''

        # create title line
        output += int((30 - len(self.category)) / 2) * '*' + self.category + int((30 - len(self.category)) / 2) * '*' + '\n'
        
        # create transaction lines
        for transaction in self.ledger:          
            # add first 23 characters of description to output
            output += transaction['description'][0:23]
            desc_length = 23
            if len(transaction['description']) < 23: desc_length = len(transaction['description'])
            
            # determine if 'amount' has decimals
            am_output = str(transaction['amount'])
            
            if len(am_output) > 2:
                if am_output[-3] != '.': am_output += '.00'
            else: am_output += '.00'

            # concat output with spaces and amount
            output += ' ' * (30 - desc_length - len(am_output)) + am_output + '\n'
        
        # create total line
        if transaction != self.ledger[-1]:
            output += 'Total: ' + str(self.balance) + '\n'
        else: output += 'Total: ' + str(self.balance)

        return output
    
    def deposit(self, amount, description = ''):
        output = { 'amount': amount, 'description': description }
        self.ledger.append(output)
        self.balance += amount
        return
    
    def withdraw(self, amount, description = ''):
        if amount <= self.balance:
            output = { 'amount': -amount, 'description': description }
            self.ledger.append(output)
            self.balance -= amount
            return True
        else: return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, destination):
        if self.balance > amount:
            destination.balance += amount
            destination.ledger.append({ 'amount': amount, 'description': 'Transfer from ' + str(self.category) })
            self.balance -= amount
            self.ledger.append({ 'amount': -amount, 'description': 'Transfer to ' + str(destination.category) })
            return True
        else: return False

    def check_funds(self, amount):
        if amount > self.balance: return False
        else: return True

def create_spend_chart(categories):
    output = 'Percentage spent by category\n'
    
    # find total of all spending for each category
    totals = []
    for cat in categories:
        t = 0
        for transaction in cat.ledger:
            if int(transaction['amount']) < 0:
                t += -transaction['amount']
        totals.append(t)

    # find percentages of each category
    percs = []
    rounded_down = []
    t = 0
    for i in totals:
        t += i
    for i in totals:
        percs.append((i / t) * 100)
    for i in percs:
        rounded_down.append(int(i - (i % 10)))

    # add top half of bar chart
    for num in range(100, -10, -10):
        to_output = ''
        
        # add numbers and correct preceding spaces
        if num != 100: to_output += ' '
        if num == 0: to_output += ' '
        to_output += str(num) + '|'

        # add 'o's if needed
        to_output += ' '
        if rounded_down[0] >= num:
            to_output += 'o  '
        else: to_output += '   '

        if rounded_down[1] >= num:
            # if rounded_down[0] < num:
            #     output += '  '
            to_output += 'o  '
        
        if len(rounded_down) > 2:
            if rounded_down[2] >= num:
                # if rounded_down[0] < num and rounded_down[1] < num:
                #     output += '    '
                to_output += 'o  '
            
        if len(rounded_down) > 3:
            if rounded_down[3] >= num:
                # if rounded_down[0] < num and rounded_down[1] < num and rounded_down[2] < num:
                #     output += '      '
                to_output += 'o  '
        
        to_output += ' ' * (14 - len(to_output))
        to_output += '\n'

        output += to_output

    # add dashes under chart
    output += '    '
    output += '-' * (len(percs) * 3 + 1)
    output += '\n'

    # add labels under each bar
    letters = [] # 2d array with x subarrays of length len(input array) where x is the longest word in the input array
    inputs = []
    for i in categories:
        inputs.append(i.category)

    # populate letters list
    for idx, i in enumerate(max(inputs, key = len)):
        to_letters = []

        for j in inputs:
            if idx >= len(j):
                to_letters.append(' ')
            else:
                to_letters.append(j[idx])

        letters.append(to_letters)

    # add letters to output
    for sub in letters:
        output += '     '

        for j in sub:
            output += j + '  '

        if sub != letters[-1]: output += '\n'

    return output

food = Category("Food")
food.deposit(900, "deposit")
entertainment = Category("Entertainment")
entertainment.deposit(900, "deposit")
business = Category("Business")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
print(create_spend_chart([business, food, entertainment]))


# food = Category("Food")
# food.deposit(1000, "initial deposit")
# food.withdraw(10.15, "groceries")
# food.withdraw(15.89, "restaurant and more food for dessert")
# food.get_balance()
# clothing = Category("Clothing")
# food.transfer(50, clothing)
# clothing.withdraw(25.55)
# clothing.withdraw(100)
# auto = Category("Auto")
# auto.deposit(1000, "initial deposit")
# auto.withdraw(15)
# print(create_spend_chart([food, clothing, auto]))