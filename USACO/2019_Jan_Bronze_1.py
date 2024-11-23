f = open("shell.in", "r")
g = open("shell.out", "w")
length = int(f.readline())

counter=[0,0,0]
shells=[1,2,3]

for i in range(length):
    swap1,swap2,guess=list(map(int,f.readline().split()))
    temp=shells[swap1-1]
    shells[swap1-1]=shells[swap2-1]
    shells[swap2-1]=temp
    counter[shells[guess-1]-1]+=1

g.write(str(max(*counter)))
g.close()

