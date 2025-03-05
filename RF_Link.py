'''

RF Link - Power Calculator

'''


class RF_link:
    def __init__(self,radio):
        self.Radio=radio
        self.Rx_pow=0
        self.Attenuation=0

    def __str__(self):
        return f"{self.Radio.Name}|| Rx_pow: {self.Rx_pow}dBm"
        

class Radio:
    Name="Radio"
    def __init__(self,Id,Tx,Rx,Attu=40):

        self.Id=Id
        self.Name = "Radio_"+str(Id+1)
        self.TX_power=Tx
        self.RX_sen = Rx
        self.Attenuation = Attu
        self.ANT=None
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

    

        

                        

class Attenuator:
    Name = 'Attenuator'
    def __init__(self,Id,Attu):

        self.Id=Id
        self.Attenuation = Attu
        self.Name =  "Attenuator_"+str(Id+1)
        self.Port1=None
        self.Port2=None

    def __str__(self):
        return f" {self.Port1.Name} <=> ({self.Attenuation}dB ){self.Name} <=> {self.Port2.Name} "
    
    def Link(self,R,Att,p_ref):
        Att+=self.Attenuation
        if p_ref == self.Port1:
            self.Port2.Link(R,Att,self)
        else:
            self.Port1.Link(R,Att,self)

    
class Divider:
    Name='Divider'
    def __init__(self,Id,sum=3,iso=36):
        self.Id=Id
        self.Name="Divider_"+str(Id+1)
        self.sum=sum
        self.iso=iso

        self.Port1=None
        self.PortS=None
        self.Port2=None

    def __str__(self):
        return f"{self.Port1.Name} <=> {self.Name} <=> {self.Port2.Name}\n{' '*(len(self.Port1.Name)+3)}||\n{' '*(len(self.Port1.Name))}{self.PortS.Name}"
        
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
            Attu_create(p_ref.TX_power,p_ref.RX_sen)
    
    if type(p_ref) == Divider:
        for i in range(n):
            Divider_create(p_ref.TX_power,p_ref.RX_sen)

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
        return ATTU[int(input('Enter Divider ID: ')) -1]
    
def Connect():
        p_ref=PRT_list()        
        t=PRT_list()
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

while True:
    op=int(input("1->Create Part\n2->Duplicate Part\n3->Connect Parts\n4->RUN\n5->check"))
    if op==1:
        Part_create()
    elif op==2:
        Part_duplicate()
    elif op==3:
        Connect()

    elif op==4:
        for i in RADIO:
            i.TX_link()
    else:
        check()

        
