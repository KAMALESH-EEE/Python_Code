def flames():   
    global i,fl,l
    while not(len(fl) == 1):
        j=1
        while (j<l):
            j+=1
            i+=1
            if(i == len(fl)):
                i=0
    
        fl.pop(i)
        if(i==len(fl)):
            i=0

m_n=input('Enter Boy Name: ')
f_n=input('Enter Girl Name: ')
m_n=m_n.lower()
f_n=f_n.lower()
st=m_n+'-'+f_n
re=open('learning/flames.txt','r')
li=re.readlines()
flag =True
for s in li:
    k=s.split('/')
    if(st == k[0]):
        flag=False
        print('Already Checked:')
        print('Result is',k[1])
re.close()
if(flag):
    m=[char for char in m_n]
    f=[char for char in f_n]
    com=[]
    i=0
    for ch in m:
        if(ch in f):
            com.append(ch)
            f.remove(ch)
    for ch in com:
        if(ch in m):
            m.remove(ch)

    l=len(m)+len(f)

    fl = ['Friend','Lover','Affection','Marriage','Enemy','Sister']

    flames()
    print(fl)
    print('your data is stored in flames.txt file !')
    
    re=open('learning/flames.txt','a')
    re.write(st+'/'+fl[0]+'\n')
