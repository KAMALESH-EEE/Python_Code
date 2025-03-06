class RF_link:
    def __init__(self,radio):
        self.Radio=radio
        self.Rx_pow=0
        self.Attenuation=0

    def __str__(self):
        return f"{self.Radio.Name}|| Rx_pow: {self.Rx_pow}dBm"
        
class open:
    Name='[open]'
    def Link(R,Att,p_ref):
        return

class Radio:
    Name="Radio"
    def __init__(self,Id,Tx,Rx,Attu=40):

        self.Id=Id
        self.Name = "Radio_"+str(Id+1)
        self.TX_power=Tx
        self.RX_sen = Rx
        self.Attenuation = Attu
        self.ANT=open
        self.Vis=[]

    def __str__(self):
        return f" {self.Name} <=> {self.ANT.Name} dB"
    
    def Link (self,R,Att,p_ref):
        Att+=self.Attenuation
        Rx_power = R.TX_power - Att
        if Rx_power >= self.RX_sen:
            v=RF_link(R)
            v.Rx_pow=Rx_power
            v.Attenuation=Att
            self.Vis.append(v)

    def TX_link(self):
        Att=self.Attenuation
        self.ANT.Link(self,Att,self)

    def VisList(self):
        if len(self.Vis) == 0:
            print("No Radios are Visible")
        print("Visible Radios")
        for i in self.Vis:
            print(i)

    def View(self,F=False):
        print('=============')
        print(f"{self.Name}\n1-> TX power{self.TX_power}\n2-> Sensitivity{self.RX_sen}\n3-> Attenuator{self.Attenuation}")
        print('\n=============')
        if F:
            t=int(input('Choose to Edit:'))
            if t==1:
                v=int(input('Enter new TX power:'))
                self.TX_power=v
            elif t==2:
                v=int(input('Enter new RX sensitivity:'))
                self.RX_sen=v

            elif t==3:
                v=int(input('Enter new Attenuation:'))
                self.Attenuation=v
            else:
                print('Wrong Input')
                return
            print('Updated....\n')


class Attenuator:
    Name = 'Attenuator'
    def __init__(self,Id,Attu):

        self.Id=Id
        self.Attenuation = Attu
        self.Name =  str(self.Attenuation)+"dB-Attenuator_"+str(Id+1)
        self.Port1=open
        self.Port2=open

    def __str__(self):
        return f" {self.Port1.Name} <=> ({self.Attenuation}dB ){self.Name} <=> {self.Port2.Name} "
    
    def Link(self,R,Att,p_ref):
        Att+=self.Attenuation
        if p_ref == self.Port1:
            self.Port2.Link(R,Att,self)
        else:
            self.Port1.Link(R,Att,self)
        
    def View(self,F=False):
        print('=============')
        print(f'{self.Name}\nAttenuation{self.Attenuation}')
        print('=============')
        if F:
            v=int(input('Enter new Attenuation:'))
            self.Attenuation=v
            self.Name =  str(self.Attenuation)+"dB-Attenuator_"+str(self.Id+1)
            print('Updated....\n')

    
class Divider:
    Name='Divider'
    def __init__(self,Id,sum=3,iso=36):
        self.Id=Id
        self.Name="Divider_"+str(Id+1)
        self.sum=sum
        self.iso=iso

        self.Port1=open
        self.PortS=open
        self.Port2=open

    def __str__(self):
        return f"{self.Port1.Name} <=> {self.Name} <=> {self.Port2.Name}\n{' '*(len(self.Port1.Name)+7)}||\n{' '*(len(self.Port1.Name)+3)}{self.PortS.Name}"
        
    def Link(self,R,Att,p_ref):
        if p_ref == self.Port1:
            temp=Att+self.iso
            self.Port2.Link(R,temp,self)
            temp=Att+self.sum
            self.PortS.Link(R,temp,self)
        elif p_ref == self.Port2:
            temp=Att+self.iso
            self.Port1.Link(R,temp,self)
            temp=Att+self.sum
            self.PortS.Link(R,temp,self)
        else:
            temp=Att+self.sum
            self.Port1.Link(R,temp,self)
            temp=Att+self.sum
            self.Port2.Link(R,temp,self)

    def View(self,F=False):
        print('=============')
        print(self.Name +'\n1-> Sum'+self.sum+'\n2-> Isolation '+self.iso)
        print('\n=============')
        if F:
            t=input('Enter Value [sum iso]')
            try:
                temp=t.split(' ')
                self.sum,self.iso = int(temp[0]) , int(temp[1])
            except:
                print('Invalid Input')
                return
            print('Updated....\n')

PARTS=[Radio,Attenuator,Divider]
RADIO=[]
ATTU=[]
DIVIDER=[]

def Radio_create(tx,rx):
    t=Radio(len(RADIO),tx,rx)
    RADIO.append(t)
    print(f'{t.Name} created')

def Attu_create(Attu):
    t=Attenuator(len(ATTU),Attu)
    ATTU.append(t)
    print(f'{t.Name} created')

def Divider_create():
    t=Divider(len(DIVIDER))
    DIVIDER.append(t)
    print(f'{t.Name} created')


def Part_create():
    t=1
    print("Part Creation")
    for i in PARTS:
        print(f'{t}=> {i.Name}')
        t+=1
    t=int(input('Enter input: '))

    if t == 1:
        tx = int(input("Enter Tx power (dBm): "))
        rx = int(input("Enter Rx Sensitivity (dBm): "))
        Radio_create(tx,rx)

    if t == 2:
        Att = int(input("Enter Atteunation (dB): "))
        Attu_create(Att)

    if t == 3:
        Divider_create()

def Part_duplicate():
    p_ref = PRT_list()

    n=int(input("No. of Parts"))

    if type(p_ref) == Radio:
        for i in range(n):
            Radio_create(p_ref.TX_power,p_ref.RX_sen)
    
    if type(p_ref) == Attenuator:
        for i in range(n):
            Attu_create(p_ref.Attenuation)
    
    if type(p_ref) == Divider:
        for i in range(n):
            Divider_create()

def PRT_list():
    t=1
    
    for i in PARTS:
        print(f'{t}=> {i.Name}')
        t+=1
    t=int(input('Enter input: '))

    if t == 1:
        l=1
        for i in RADIO:
            print(f"{l} => {i.Name}")
            l+=1
        return RADIO[int(input('Enter Radio ID: ')) -1]
        

    if t == 2:
        l=1
        for i in ATTU:
            print(f"{l} => {i.Name}")
            l+=1
        return ATTU[int(input('Enter Attenuator ID: ')) -1]
        
    
    if t == 3:
        l=1
        for i in DIVIDER:
            print(f"{l} => {i.Name}")
            l+=1
        return DIVIDER[int(input('Enter Divider ID: ')) -1]
    
def Connect(p_ref,t):
        
        print(f'Linking{p_ref.Name} == {t.Name}')
        if id(t)==id(p_ref):

            print("LoopBack Not Possible")
            return
        if type(p_ref) == Radio:
            p_ref.ANT=t
        print(f"Select {p_ref.Name} Ports")
        if type(p_ref) == Attenuator:
            p=int(input('Port (1/2):'))
            if p==1:
                p_ref.Port1=t

            else:
                p_ref.Port2=t
        
        if type(p_ref) == Divider:

            p=input('Port (1/s/2):')
            if p=='1':
                p_ref.Port1=t

            elif p == '2':
                p_ref.Port2=t
            
            else:
                p_ref.PortS=t


        if type(t) == Radio:
            t.ANT=p_ref

        if type(t) == Attenuator:
            p=int(input('Enter Port (1/2):'))
            if p==1:
                t.Port1=p_ref

            else:
                t.Port2=p_ref
        
        if type(t) == Divider:

            p=input('Enter Port (1/s/2):')
            if p=='1':
                t.Port1=p_ref

            elif p == '2':
                t.Port2=p_ref
            
            else:
                t.PortS=p_ref
        
def check():
    p_ref = PRT_list()
    if type(p_ref) == Radio:
        t=int(input("1->Visibility\n2->Link"))

        if t ==1:
            p_ref.VisList()
        else:
            print(p_ref)
    else:
        print(p_ref)


#==================================

n=int(input('Enter No. Radio'))

for i in range(n):
    Radio_create(40,-90)

for i in range(n-1):
    Attu_create(30)

for i in range(n-2):
    Divider_create()

R1=RADIO[0]
RL=RADIO[-1]

R1.ANT=ATTU[0]
ATTU[0].Port1=R1

A=ATTU[0]


for i in range(len(DIVIDER)):
    D=DIVIDER[i]
    R=RADIO[i+1]
    A.Port2=D
    D.Port1=A
    D.PortS=R
    R.ANT=D
    A=ATTU[i+1]
    A.Port1=D
    D.Port2=A

A.Port2=RL
RL.ANT=A

#====================================


while True:
    op=int(input("\n\n1->Create Part\n2->Duplicate Part\n"
    "3->Connect Parts\n4->RUN\n5->check\n"
    "6->View Part\n7->Edit part\nSelect:"))
    if op==1:
        Part_create()
    elif op==2:
        Part_duplicate()
    elif op==3:
        p_ref=PRT_list()        
        t=PRT_list()
        Connect(p_ref,t)

    elif op==4:
        for i in RADIO:
            i.Vis=[]
        for i in RADIO:
            i.TX_link()
        for i in RADIO:
            print(f'======{i.Name}======')
            i.VisList()
            print('======================\n')
    elif op ==6:
        part=PRT_list()
        part.View()

    elif op ==7:
        part=PRT_list()
        part.View(F=True)

    else:
        check()

        
#======================================
