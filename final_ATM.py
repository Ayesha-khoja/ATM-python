import getpass
class Atm:

    balance = 10000  
    def __init__(self):
        self.balance = 10000
        self.w_draw= 0
        self.dep = 0
        self.trans = 0

    def authen(self):
        print("\n\nWELCOME TO YOU <3")
        user = input("Enter user name:")
        # passw = input("Enter your password: ")
        import getpass
        passw = getpass.getpass("Enter your password: ")
        print("You entered:", user)
        if (user == "Ayesha" and passw == "khoja90"):
            self.select_options()
             
        else:
            print("Authentication Failed!, TRY AGAIN\n\n")
            self.authen() 

    def check_balance(self):
        print("***BALANCE***")
        print(f"your current balance is {self.balance}\n\n" )

    def withdraw(self):
        print("WITHDRAW\n")
        # w_draw =input("Enter the amount that you want to withdraw\n\n")
        while True:
            w_draw = input("Enter the amount that you want to withdraw (type 'exit' to return to options):\n\n")
            if(w_draw=="exit"): 
                self.select_options()
            elif w_draw.isdigit():
                w_draw = int(w_draw)

                if(w_draw > 500):

                    if(w_draw <50000):
                        if (w_draw <= self.balance):
                            self.w_draw = w_draw
                            self.balance = self.balance - w_draw
                            
                            print(f"******{w_draw}, withdrawn successfull*******\n")
                        else:
                            print("*****  Insufficient balance:)   ****")   
                    else:
                        print("please enter value less than 50000")   
                        continue    
                else:
                    print("please enter value greater than 500 ") 
                    continue
            break         


            

    def deposit(self):    
        dep = input("Enter the amount you want to deposit (type 'exit' to return to options):\n\n ")
        if(dep=="exit"):
            self.select_options()
        elif dep.isdigit():
            dep = int(dep)  
            self.dep = dep  
            self.balance  = self.balance + dep
        print(f"you deposited {dep} successfully!!\n")
        # print(f"*****your total amount is: , {self.balance}")
    def transfer(self):
        print("***TRANSFER***")
        while True:
            trans = input("Enter transfer amount value (type 'exit' to return to options):\n\n ")
            if trans == "exit":
                self.select_options()
            elif trans.isdigit():
                trans = int(trans)
                if trans <= self.balance and trans > 0:
                    self.trans = trans 
                    self.balance -= trans
                    transfer_name = input("Enter the name of the recipient: ")
                    while True:
                        transfer_account = input("Enter the account number of the recipient (must be 17 digits): ")
                        if len(transfer_account) == 17 and transfer_account.isdigit():
                            print(f"Transfer successful! {trans} transferred to account {transfer_account} (Recipient: {transfer_name})")
                            print(f"Transfer amount is: {trans}\n")
                            print("***Transaction completed***")
                            break
                        else:
                            print("Please enter correct account number")
                    break
                else:
                    print("Insufficient balance :(")
            else:
                print("Please enter a valid number for transfer amount (type 'exit' to return to options):\n\n")
        

    
    def receipt(self):
        print("********************************************************")
        print("****     your current balance is: ", self.balance) 
        print("****     your withdraw amount:    ", self.w_draw)  
        print("****     your deposit amount is:  ", self.dep)
        print("****     your transfer amount is: ", self.trans)
        print("********************************************************")      

    def exit(self):
        print("\n")
        print("************************************")
        print("*          THANK YOU               *")
        print("************************************")
        rec=input("\nDo you want your receipt?").lower()

    
        if(rec=="yes"):
            self.receipt()
            

    def select_options(self):
        options = {
            "1": self.check_balance,
            "2": self.withdraw,
            "3": self.deposit,
            "4": self.transfer,
            "5": self.exit,
        }
        while True:
            print("1) chack balance")
            print("2) withdraw")
            print("3) deposit")
            print("4) Transfer")
            print("5) Exit\n")
            select =  input("Select any number: ")
            if select in options:
                options[select]()
                if select == "5":  # Exit condition
                    break
            else:
                print("Invalid selection! Please try again.")    

obj = Atm()
obj.authen()
