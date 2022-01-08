# CreditCard Class Assignment

import random


class CreditCard:
    """A simple model of a credit card"""

    # Dictionary class variable card_type
    card_type = {1: 'Visa', 2: 'Mastercard', 3: 'Amex', 4: 'Discover'}

    def __init__(self, card_number, name, exp_date):
        """Initialize attributes to describe a credit card."""
        self.card_number = card_number
        self.name = name
        self.exp_date = exp_date
        self.credit_limit = 1000
        self.card_balance = random.randint(0, 999)
        self.determine_card_type()
    
    def get_cardOwner(self):
        """Obtain the person's name that owns the credit card."""
        return self.name

    def determine_card_type(self):
        """Assigns card type to a given credit card number."""
        if self.card_number[5] == '1':
            self.card_type = CreditCard.card_type[1]
        elif self.card_number[5] == '2':
            self.card_type = CreditCard.card_type[2]
        elif self.card_number[5] == '3':
            self.card_type = CreditCard.card_type[3]
        elif self.card_number[5] == '4':
            self.card_type = CreditCard.card_type[4] 
        else:
            self.card_type = 'Not Supported Card Type'

    def get_cardType(self):
        """Obtain the card type of the credit card."""
        return self.card_type
    
    def processOrder(self, transac_amt):
        """Checks for sufficient balance on the card for processing an order."""
        if transac_amt + self.card_balance > self.credit_limit:
            return False
        elif self.card_type == 'Not Supported Card Type':
            return False
        else:
            self.card_balance += transac_amt
            return True
    
    def __str__(self):
        """Returns info about person's name, credit card number, expiration date."""
        return f"{self.name} is the owner of the credit card with number {self.card_number} which expires on {self.exp_date}."
        
