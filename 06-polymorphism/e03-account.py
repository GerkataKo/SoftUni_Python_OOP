class Account:
    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def add_transaction(self, amount):
        if not type(amount) == int:
            raise ValueError("please use int for amount")
        self._transactions.append(amount)

    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def validate_transaction(self, amount_to_add):
        if type(amount_to_add) == int:
            self._transactions.append(amount_to_add)
            if self.balance < 0:
                self._transactions.pop()
                raise ValueError("sorry cannot go in debt!")
            return f"New balance: {self.balance}"

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, index):
        return self._transactions[index]

    def __eq__(self, other):
        return self.balance == other.balance

    def __gt__(self, other):
        return self.balance >= other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __add__(self, other):
        new_obj = Account(f'{self.owner}&{other.owner}', self.amount + other.amount)
        new_obj._transactions = self._transactions + other._transactions
        return new_obj


acc = Account('bob', 10)
acc2 = Account('john')
print(acc)
print(repr(acc))
acc.add_transaction(20)
acc.add_transaction(-20)
acc.add_transaction(30)
print(acc.balance)
print(len(acc))
for transaction in acc:
    print(transaction)
print(acc[1])
print(list(reversed(acc)))
acc2.add_transaction(10)
acc2.add_transaction(60)
print(acc > acc2)
print(acc >= acc2)
print(acc < acc2)
print(acc <= acc2)
print(acc == acc2)
print(acc != acc2)
acc3 = acc + acc2
print(acc3)
print(acc3._transactions)
