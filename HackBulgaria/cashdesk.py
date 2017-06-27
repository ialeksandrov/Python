class Bill:
    def __init__(self, amount):
        if not isinstance(amount, int):
            raise TypeError

        if amount < 0:
            raise ValueError

        self.amount = amount

    def __str__(self):
        return "A {}$ bill".format(self.amount)

    def __repr__(self):
        return "A {}$ bill".format(self.amount)

    def __int__(self):
        return int(self.amount)

    def __eq__(self, other):
        return self.amount == other.amount

    def __hash__(self):
        return hash(str(self.amount))

    def __lt__(self, other):
        return int(self) < int(other)


class BatchBill:
    def __init__(self, bills):
        self.bills = bills

    def __len__(self):
        return len(self.bills)

    def total(self):
        return sum([int(bill) for bill in self.bills])

    def __getitem__(self, index):
        return self.bills[index]


class CashDesk:
    def __init__(self):
        self.coins = 0
        self.bank = {}

    def add_in_bank(self, money):
        if money in self.bank:
            self.bank[money] += 1
        else:
            self.bank[money] = 1

    def take_money(self, money):
        if isinstance(money, Bill):
            self.coins += int(money)
            self.add_in_bank(money)
        elif isinstance(money, BatchBill):
            self.coins += money.total()
            for bill in money:
                self.add_in_bank(bill)

    def total(self):
        return self.coins

    def inspect(self):
        sorted_bills = sorted(self.bank)
        print("We have the following count of bills,\
 sorted in ascending order:")
        for bill in sorted_bills:
            print("{} - {}".format(repr(bill), self.bank[bill]))



values = [10, 20, 50, 100, 100, 100]
bills = [Bill(value) for value in values]

batch = BatchBill(bills)

desk = CashDesk()

desk.take_money(batch)
desk.take_money(Bill(10))

print(desk.total()) # 390
desk.inspect()
