# تعريف كلاس BankAccount مع الخصائص والطرق المطلوبة
class BankAccount:
    # الخصائص: رقم الحساب، اسم صاحب الحساب، والرصيد
    def __init__(self, account_number, account_holder):
        self._account_number = account_number
        self._account_holder = account_holder
        self._balance = 0.0

    # طريقة إيداع مبلغ
    def deposit(self, amount):
        self._balance += amount

    # طريقة سحب مبلغ
    def withdraw(self, amount):
        self._balance -= amount

    # طريقة الحصول على الرصيد الحالي
    def get_balance(self):
        return self._balance

# إنشاء كائن من نوع BankAccount
bank_account = BankAccount("2961", "Azez Kiwan")

# إيداع 1000 دولار
bank_account.deposit(1000)
print(bank_account.get_balance())

# سحب 500 دولار
bank_account.withdraw(500)
print(bank_account.get_balance())

# تعريف كلاس SavingsAccount التي ترث من BankAccount
class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, interest_rate):
        # استدعاء المُنشئ الأصلي من كلاس BankAccount
        super().__init__(account_number, account_holder)
        self._interest_rate = interest_rate


    # طريقة تطبيق الفوائد على الرصيد
    def apply_interest(self):
        self._balance += self._balance * self._interest_rate

    # طريقة طباعة البيانات
    def __str__(self):
        return f"Account Number: {self._account_number}, Account Holder: {self._account_holder}, Balance: {self._balance}, Interest Rate: {self._interest_rate}"

# إنشاء كائن من نوع SavingsAccount
savings_account = SavingsAccount("11111", "Issa ali", 0.44)
savings_account.deposit(200)
# تطبيق الفوائد على الرصيد
savings_account.apply_interest()
print(savings_account)