class HW_COM:

    def __init__(self):
        pass

    def Send(self,A):
        print(A)
    
    def Receive(self):
        return input()

class COM_FIFO:
    com = HW_COM()
    OP_COUNT = 0
    SD_BUFFER = []
    HD_BUFFER = []
    FIFO = {}
    IM_FLAG = False

    def __init__(self,SD='',HD=''):
    
        self.SD = SD
        self.HD = HD
    
        COM_FIFO.OP_COUNT += 1
        self.ID = COM_FIFO.OP_COUNT
        self.Sorce = 'H' if self.SD == '' else 'S'
        self.Response_Status = False
        self.TX_Status = False
        COM_FIFO.FIFO.update({self.ID:self})

    def check():
        IN = COM_FIFO.com.Receive()
        t = IN.split('][')
        t.pop()
        for i in t:
            try:
                td = i.split('|:|')
                id = int(td[0])
                data = td[1]

                if id in COM_FIFO.FIFO.keys():
                    tg = COM_FIFO.FIFO[id]
                    tg.HD = data
                    tg.Response_Status = True
                    tg.TX_Status = False
                    COM_FIFO.HD_BUFFER.append(data)

                else:
                    COM_FIFO(HD=data)
                    
            except:
                print('Error While ID Map')
        if COM_FIFO.IM_FLAG:
            COM_FIFO.RESPOND()
            COM_FIFO.TRANSMITE()
            COM_FIFO.IM_FLAG = False
            return


        for i in COM_FIFO.SD_BUFFER:
            COM_FIFO(SD=i)
        COM_FIFO.TRANSMITE()
                        

    def TRANSMITE ():
        for i in COM_FIFO.FIFO.items():
            id,tg = i
            if tg.TX_Status == False:
                data = f'{id}|:|{tg.SD}]['
                tg.TX_Status = True
                COM_FIFO.com.Send(data)

    def RESPOND ():
        pass
        


class RK_COM:
    
    def __init__(self):
        
        RK_COM.com.Send('KAMALESH')
        print(self.com.Receive())


RK_COM()