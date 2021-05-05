def printGraph(data):
    out=[]
    for i in data:
         t = []
         out.append(t)
         for x in range(i):
            print('x',end ='')
            t.extend('x')
         print()
    return out
data = [1,2,3]
output = printGraph(data)
# x
# xx
# xxx
print(output) # [['x'], ['x', 'x'], ['x', 'x', 'x']]