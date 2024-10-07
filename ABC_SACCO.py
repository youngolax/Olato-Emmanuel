# Base class representing a Sacco member
class Member:
    def __init__(self, name, member_id, savings=0):
        self.name = name
        self.member_id = member_id
        self.savings = savings

    def deposit(self, amount):
        self.savings += amount
        print(f"{self.name} has deposited Ush {amount}. Total savings: Ush {self.savings}")

    def withdraw(self, amount):
        if amount <= self.savings:
            self.savings -= amount
            print(f"{self.name} has withdrawn Ush {amount}. Remaining savings: Ush {self.savings}")
        else:
            print(f"{self.name} has insufficient savings to withdraw Ush {amount}.")

    def display_info(self):
        print(f"Member ID: {self.member_id}, Name: {self.name}, Savings: Ush {self.savings}")

# Inheritance: Specialized class for Premium members
class PremiumMember(Member):
    def __init__(self, name, member_id, savings=0):
        super().__init__(name, member_id, savings)
        self.loan_discount_rate = 10
    def display_info(self):
        super().display_info()
        print(f"Premium Member - Loan Discount Rate: {self.loan_discount_rate}%")

# Base class representing a loan
class Loan:
    def __init__(self, member, loan_amount, interest_rate, duration):
        self.member = member
        self.loan_amount = loan_amount
        self.interest_rate = interest_rate
        self.duration = duration
        self.is_repaid = False

    def calculate_interest(self):
        # Polymorphism: Each loan type can override this method
        return self.loan_amount * self.interest_rate / 100

    def repay_loan(self):
        self.is_repaid = True
        print(f"Loan of Ush {self.loan_amount} for {self.member.name} has been repaid.")

    def display_info(self):
        status = "Repaid" if self.is_repaid else "Not Repaid"
        print(f"Loan for {self.member.name}: Amount: Ush {self.loan_amount}, Interest Rate: {self.interest_rate}%, Status: {status}")

# Inheritance: Specialized loan for Premium members
class PremiumLoan(Loan):
    def calculate_interest(self):
        # Override the method to offer reduced interest for premium members
        discount_rate = self.member.loan_discount_rate if isinstance(self.member, PremiumMember) else 0
        return self.loan_amount * (self.interest_rate - discount_rate) / 100

# Class representing the Sacco
class Sacco:
    def __init__(self, name):
        self.name = name
        self.members = []
        self.loans = []

    def add_member(self, member):
        self.members.append(member)
        print(f"{member.name} has been added to {self.name} Sacco.")

    def issue_loan(self, member, loan_amount, interest_rate, duration):
        if isinstance(member, PremiumMember):
            loan = PremiumLoan(member, loan_amount, interest_rate, duration)
        else:
            loan = Loan(member, loan_amount, interest_rate, duration)
        self.loans.append(loan)
        print(f"Loan of Ush {loan_amount} issued to {member.name}.")

    def generate_report(self):
        print(f"\n{self.name} REPORT:")
        print("MEMBERS:")
        for member in self.members:
            member.display_info()
        print("\nLOANS:")
        for loan in self.loans:
            loan.display_info()

# Main program demonstrating the system
if __name__ == "__main__":
    # Create a Sacco instance
    sacco = Sacco("ABC SACCO")

    # Create regular and premium members
    member1 = Member("Okello John", "ABC001", 10000)
    member2 = PremiumMember("Mukisa Sam", "ABC002", 15000)

    # Add members to the Sacco
    sacco.add_member(member1)
    sacco.add_member(member2)

    # Members deposit savings
    member1.deposit(5000)
    member2.deposit(3000)
    # Issue loans to members
    sacco.issue_loan(member1, 20000, 5, 12)  # 5% interest for regular member
    sacco.issue_loan(member2, 25000, 5, 12)  # 5% interest for premium member (discount applies)
    # Repay a loan
    loan_for_bob = sacco.loans[1]
    loan_for_bob.repay_loan()

    sacco.generate_report()
