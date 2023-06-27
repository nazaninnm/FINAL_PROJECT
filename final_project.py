class UserAccount:
    def __init__(self, First_name, Last_name, national_id, date_of_birth, balance):
        self.First_name = First_name
        self.Last_name = Last_name
        self.national_id = national_id
        self.date_of_birth = date_of_birth
        self.balance = balance

    def display_account_info(self):
        First_Name= self.First_name.capitalize()
        Last_Name= self.Last_name.capitalize()
        print("Account Information:")
        print("FirstName: ", First_Name)
        print("LastName: ", Last_Name)
        print("National ID: ", self.national_id)
        print("Date of Birth: ", self.date_of_birth)
        print("Balance: ", self.balance)


First_name = input("Enter your Firstname: ")
Last_name = input("Enter your Lastname: ")
national_id = input("Enter your national ID: ")
date_of_birth = input("Enter your date of birth: ")
balance = float(input("Enter your account balance: "))

user = UserAccount(First_name, Last_name, national_id, date_of_birth, balance)
user.display_account_info()
