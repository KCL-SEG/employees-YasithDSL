"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""
class Contract:
    def __init__(self, hourly, rate):
        self.requires_hours = hourly
        self.rate = rate
        
    def get_contract_pay(self, hours = 0):
        if self.requires_hours:
            return hours * self.rate
        return self.rate

class Commision:
    def __init__(self, is_contracts: bool, rate: int):
        self.requires_ncontracts = is_contracts
        self.rate = rate
    
    def get_commision_pay(self, contracts = 0):
        if self.requires_ncontracts:
            return self.rate * contracts
        return self.rate

class Employee:
    def __init__(self, name):
        self.name = name
        self.commission = None

    def add_contract(self, contract: Contract, hours = 0):
        self.contract = contract
        self.hours = hours

    def add_commision(self, commision: Commision, contracts = 0):
        self.commission = commision
        self.contracts = contracts

    def get_pay(self):
        contract_pay = self.contract.get_contract_pay(self.hours)
        if self.commission != None:
            return contract_pay + self.commission.get_commision_pay(self.contracts)
        return contract_pay
        
        
    def __str__(self):
        total = self.get_pay()
        contract = ""
        if self.hours > 0:
            contract = f"contract of {self.hours} hours at {self.contract.rate}/hour"
        else:
            contract = f"monthly salary of {self.contract.rate}"
        commission = ""
        if self.commission != None:
            if self.commission.requires_ncontracts:
                commission = f" and receives a commission for {self.contracts} contract(s) at {self.commission.rate}/contract"
            else:
                commission = f" and receives a bonus commission of {self.commission.rate}"
        return f"{self.name} works on a {contract}{commission}. Their total pay is {total}."

    

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie')
billie.add_contract(Contract(False, 4000))

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie')
charlie.add_contract(Contract(True, 25), 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee')
renee.add_contract(Contract(False, 3000))
renee.add_commision(Commision(True, 200), 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan')
jan.add_contract(Contract(True, 25), 150)
jan.add_commision(Commision(True, 220), 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie')
robbie.add_contract(Contract(False, 2000))
robbie.add_commision(Commision(False, 1500))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel')
ariel.add_contract(Contract(True, 30), 120)
ariel.add_commision(Commision(False, 600))