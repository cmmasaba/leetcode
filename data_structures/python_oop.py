class CreditCard():
    """A consumer credit card."""

    def __init__(self, customer: str, bank: str, account:str, limit: float):
        """Create a new credit card instance.
        
        The initial balance iz zero.
        
        @param customer: the name of the customer (e.g., 'Collins Mmasaba')
        @param bank: the name of the bank (e.g., 'KCB Bank')
        @param account: the account number (e.g., '5391 0375 9387 5309')
        @param limit: the credit limit in dollars
        """
        self._customer = customer
        self._bank = bank
        self._account = account
        self._limit = limit
        self._balance = 0
    
    def __repr__(self) -> str:
        """Return a string representation of the object."""
        return f'CreditCard({self._customer}, {self._bank}, {self._account}, {self._limit})'

    @property
    def customer(self) -> str:
        """Return name of the customer."""
        return self._customer
    
    @property
    def bank(self) -> str:
        """Return the name of the bank."""
        return self._bank
    
    @property
    def account(self) -> str:
        """Return the account number."""
        return self._account
    
    @property
    def limit(self) -> float:
        """Return the credit limit."""
        return self._limit
    
    @property
    def balance(self) -> float:
        """Return the current balance."""
        return self._balance
    
    def charge(self, price: float) -> bool:
        """Charge given price to the card, assuming sufficient credit limit.
        
        Return True if charge was processed; False if charge was denied.
        """
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True
    
    def make_payment(self, amount: float):
        """Process customer payment that reduces balance."""
        self._balance -= amount

if __name__ == '__main__':
    """Tests for the CreditCard class."""
    wallet = []
    wallet.append(CreditCard('Collins Mmasaba', 'KCB', '5391 0375 9387 5309', 10000))
    wallet.append(CreditCard('Frandel Wanjawa', 'Equity', '3485 0399 3395 1954', 7000))
    wallet.append(CreditCard('Aineah Bwire', 'Bank of Baroda', '5391 0375 9387 5309', 6000))

    for value in range(1, 5):
        wallet[0].charge(value)
        wallet[1].charge(2 * value)
        wallet[2].charge(3 * value)
    
    for i in range(3):
        print('Customer ==> ', wallet[i].customer)
        print('Bank ==> ', wallet[i].bank)
        print('Account ==> ', wallet[i].account)
        print('Limit ==> ', wallet[i].limit)
        print('Balance ==> ', wallet[i].balance)
        while wallet[i].balance > 100:
            wallet[i].make_payment(100)
            print('New balance ==> ', wallet[i].balance)
        print()