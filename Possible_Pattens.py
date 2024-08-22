N=int(input('Enter number: '))

class Point:
    res=[[1],[2],[3],[4],[5],[6],[7],[8],[9]]
   
    def __init__(self,a,b):
        self.point=a
        self.next=b[:]
        
    def move(self,a):
        results =[]
        for i in self.next:
            t=a[:]
            if i not in t:
                t.append(i)
                results.append(t)
        return results
    
points=[]
points.append(Point(1,[2,4,5,6,8]))
points.append(Point(2,[1,3,4,5,6,7,9])) 
points.append(Point(3,[2,4,5,6,8]))
points.append(Point(4,[1,2,3,5,7,8,9]))
points.append(Point(5,[1,2,3,4,6,7,8,9]))
points.append(Point(6,[1,2,3,5,7,8,9]))
points.append(Point(7,[2,4,5,6,8]))
points.append(Point(8,[1,3,4,5,6,7,9]))
points.append(Point(9,[2,4,5,6,8]))

def Print(a):
    for i in a:
        print(i,end='->')
    print('')
res=Point.res[:]
for n in range(N):
    t=[]
    for i in res:
        t+=points[i[-1]-1].move(i)[:]
    res=t[:]

# for i in res:
#     Print(i)
print('No.of.possible outcome: ',len(res))
 
'''
1 2 3
4 5 6
7 8 9

By RK
'''
