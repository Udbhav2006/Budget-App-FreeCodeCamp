class Category():
    def __init__(self, category):
        self.category = category
        self.ledger = []
        self.balance = 0.00

    def check_funds(self, amount):

        if self.balance < float(amount):
            return False

        else:
            return True

    def deposit(self, amount, description=''):

        d = {"amount": amount, "description": description}
        self.ledger.append(d)
        self.balance += float(amount)

    def withdraw(self, amount, description=''):

        if self.check_funds(amount) == False:
            return False

        else:
            l = list(str(amount))
            l.insert(0, '-')
            amount_final = ''

            for i in l:
                amount_final += i

            d = {"amount": float(amount_final), "description": description}

            self.ledger.append(d)
            self.balance -= float(amount)
            return True

    def get_balance(self):
        return self.balance

    def transfer(self, amount, transfer_category):

        if self.check_funds(amount) == False:
            return False

        else:
            self.withdraw(amount, f"Transfer to {transfer_category.category}")

            transfer_category.deposit(amount, f"Transfer from {self.category}")

            return True

    def __str__(self):

        final = ''
        no_of_stars = 30 - len(self.category)
        if no_of_stars % 2 == 1:
            x = no_of_stars // 2 + 1
            final += '*' * x
            final += self.category
            x = no_of_stars // 2
            final += '*' * x

        else:
            x = no_of_stars // 2
            final += '*' * x
            final += self.category
            x = no_of_stars // 2
            final += '*' * x

        final += '\n'

        total_amount = 0.00
        for item in self.ledger:
            total_amount += float(item["amount"])

            desc = item["description"][:24]
            amt = float(item["amount"])
            spaces = ' '
            amt = str(amt)[:8]
            if len(amt.split('.')[1]) < 2:
                amt += '0'

            if len(desc) + len(amt) + len(spaces) < 30:
                x = 30 - len(desc) - len(amt) - len(spaces)
                spaces += ' ' * x

            item_string = desc + spaces + amt
            if len(item_string) > 30:
                x = len(item_string) - 30
                desc = desc[:-x]
                item_string = desc + spaces + amt

            final += item_string + '\n'

        final += f'Total: {total_amount}'
        return final


def create_spend_chart(categories):

    spent_amts = []

    for category in categories:
        spent_amt = 0
        for item in category.ledger:
            if float(item['amount']) < 0:
                a = str(item['amount'])[1:]
                spent_amt += float(a)

        spent_amts.append(spent_amt)

    total = 0

    for i in spent_amts:
        total += i

    averages = []
    for amt in spent_amts:
        x = amt / total
        averages.append(x * 100)

    chart = 'Percentage spent by category\n'
    count = 100
    while count >= 0:
        if count == 100:
            chart += str(count) + '| '

        elif count == 0:
            chart += ' ' * 2 + str(count) + '|' + ' ' 
        else:
            chart += ' ' + str(count) + '|' + ' '

        for avg in averages:
            if avg > count:
                chart += 'o' + ' ' * 2
            else:
                chart += ' ' * 3
            
            
        chart += '\n'
        count -= 10

    chart = chart.strip()
    x = len(averages) * 3 + 4
    chart +=  ' ' * 2 + '\n'
    chart += ' ' * 4 + '-' * (x - 3) + '\n'

    max_length = 0
    category_list = []
    for category in categories:
        category_list.append(category.category)
        if len(category.category) > max_length:
            max_length = len(category.category)


    for category in category_list:
      c = max_length-len(category)
      category += ' ' * c
      
    for i in range(0, max_length):
        chart += ' ' * 5
        for category in category_list:
            try:
              chart += category[i] + ' ' * 2
            except:
              chart += ' ' * 3
        chart += '\n'

    chart = chart.strip()
    chart += ' ' * 2

    return chart
