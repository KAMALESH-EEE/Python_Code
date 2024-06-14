from random import randint
from sys import stdout
class  User:
    _Users = []
    __Block = []
    def Lock(obj):
        User.__Block.append(obj)
        User._Users[obj.__Id - 4001] = None
        obj.Status=False
        print(f"{obj.__Id} is now Locked, If you want to unlock contact Bank Manger")

    def __Unlock(id):
        j=0
        obj=None
        for i in User.__Block:
            if i.__Id == id:
                obj = i
                break
            j+=1
        if(j==len(User.__Block)):
            print("Can't find the user")
        else:
            User._Users[id-4001]=obj
            obj.Status = True
            User.__Block.remove(obj)
            print(f'{obj.__Id} account is unlocked')

    def __init__(self,Name,type,In_deposite,Pass):
        if (type =='savings' and In_deposite>=500) or (type=='current' and In_deposite>=1000):
            self.__Name = Name
            self.__Type = type
            self.__Amount= float(In_deposite)
            self.__Id = 4001+len(User._Users)
            self.__Password = Pass
            self.__History=[In_deposite]
            self.Status =True
            User._Users.append(self)
            print(f"Account is created your Account number: {self.__Id}")
            self.OTP=0

        else:
            raise Exception('In valid Initial Deposite')
    
    def __str__(self):
        return f"""
            Acount NO   : {self.__Id}
            Name        : {self.__Name}
            Type        : {self.__Type}
            Curr.Balance: {self.__Amount}
            Password    : {self.__Password[0] + 'x'*(len((self.__Password))-2) + (self.__Password)[-1]}
        """
    
    def __deposite(self,amount):
        self.__Amount+=amount
        self.__History.append(amount)
        print(f"Hai {self.__Name}, Rs {amount} is credited to your {self.__Type} account. Now your Current Balance is {self.__Amount}")
        
    def __debit(self,amount):
        i=3
        while i>0:
            Pass = input('Enter Password: ')
            stdout.write('\033[F')
            print('Enter Password: '+'*'*len(Pass))
            if (Pass == self.__Password):
                if (self.__Amount-amount >= 500):
                    self.__Amount-=amount+0.10
                    self.__History.append(-1*amount)
                    print(f"Hai {self.__Name}, Rs {amount} is debited from your {self.__Type} account. Now your Current Balance is {self.__Amount}")
                elif (self.__Amount-amount >= 10):
                    self.__Amount-=amount+10
                    self.__History.append(-1*amount)
                    print(f"Hai {self.__Name}, Rs {amount} is debited from your {self.__Type} account. Now your Current Balance is {self.__Amount}.\n Your Account balace is below Minimum balace")
                else:
                    print("Insuffecient Balance to process the traction")
                return
            i-=1
            print(f"Wrong Password You have {i}/3 attampt")
        print("Your Entered wrong password 3 times")
        User.Lock(self)
        

    def Statement(self):
        print('\t***RK Bank***')
        print(f"{self.__Name} [{self.__Id}] bank Statement:")
        j=1
        for i in self.__History[::-1]:
            print(f'{j}| Rs {i}')
            j+=1
        print('    _________')
        print(f'  Rs {self.__Amount}')

    def Generate_OTP(self):
        self.OTP=randint(1010,9999)
        print(f"OTP generated Sucessfully:{self.OTP} ")

    def Validate_OTP(self,OTP):
        return self.OTP == OTP

    def UserPortal(self):
        print(self)
        while self.Status:
            op = UserMenu()
            if op == 0:
                break
            if op == 1:
                am=float(input("Enter Amount:"))
                self.__deposite(am)
            if op == 2:
                am=float(input("Enter Amount:"))
                self.__debit(am)
            if op == 3:
                print(f"Avl.Balance Rs {self.__Amount}")

            if op == 4:
                self.Generate_OTP()
                otp = int(input('Enter your OTP: '))
                if self.Validate_OTP(otp):
                    while True:
                        Pass= input('Create Password: ')
                        stdout.write('\033[F')
                        print('Create Password: '+'*'*len(Pass))
                        rPass=input('Re-enter Password: ')
                        stdout.write('\033[F')
                        print('Re-enter Password: '+'*'*len(rPass))
                        
                        if Pass == rPass:
                            break
                        print("Not Match!")
                    self.__Password=Pass
                    print('Password changed sucessfully')

            
            if op == 5:
                self.Statement()

    def MangerPortal():
        Pass = input('Enter Code: ')
        if not Pass == 'RKbank2024':
            print('\033[91m  Wrong PassWord \033[0m')
            return
        while True:
            op = input("Enter Command: ")
            if op == '0':
                break
            if op == 'new':
                print('Creating new User:')
                na = input('Name: ')
                ty = input('Type (savings/current): ')
                In = float(input('Initial Deposite: '))
                while True:
                    Pass= input('Create Password: ')
                    stdout.write('\033[F')
                    print('Create Password: '+'*'*len(Pass))
                    rPass=input('Re-enter Password: ')
                    stdout.write('\033[F')
                    print('Re-enter Password: '+'*'*len(rPass))
                    if Pass == rPass:
                        break
                    print("Not Match!")
                obj=User(na,ty,In,Pass)

            if op =='unlock':
                id=int(input('Acc.NO: '))
                User.__Unlock(id)
            if op == 'lock':
                id=int(input('Acc.NO: '))
                obj=User._Users[id-4001]
                User.Lock(obj)
                

def UserMenu():
    print("""
         RK Bank user Menu
          1) Deposite
          2) Debit
          3) Balance check
          4) Change Password
          5) Generate Statement
          0) exit to Main menu""")
    return int(input("Enter your option: "))

u1=User('Kamalesh','savings',500,'Kamal')
u2=User('Test','savings',1500,'Kamal')
while True:
    try:
        Id = int(input("Enter Acc.No: "))
        if Id==2024:
            User.MangerPortal()
            continue
        obj = User._Users[Id-4001]
        obj.UserPortal()
    except Exception as e:
        print(f"\033[91m {e}\033[0m")