f = open("blist.in", "r")
g = open("blist.out", "w")
length = int(f.readline())

buckets=[0 for i in range(1001)]

for i in range(length):
    start,stop,number=list(map(int,f.readline().split()))

    for i in range(start,stop+1):
        buckets[i]+=number


g.write(str(max(*buckets)))
g.close()
