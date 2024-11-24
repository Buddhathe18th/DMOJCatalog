f = open("mixmilk.in", "r")
g = open("mixmilk.out", "w")
cap1,milk1= list(map(int,f.readline().split()))
cap2,milk2= list(map(int,f.readline().split()))
cap3,milk3= list(map(int,f.readline().split()))

for i in range(100):
    if i%3==0:
        # Pour 1 into 2
        milk2+=milk1
        milk1=0
        if milk2>cap2:
            milk1 = milk2 - cap2
            milk2=cap2


    elif i%3==1:
        # Pour 2 into 3
        milk3 += milk2
        milk2 = 0
        if milk3 > cap3:
            milk2 = milk3 - cap3
            milk3 = cap3

    else:
        # Pour 3 into 1
        milk1 += milk3
        milk3 = 0
        if milk1 > cap1:
            milk3 = milk1 - cap1
            milk1 = cap1


g.write(str(milk1)+"\n"+str(milk2)+"\n"+str(milk3)+"")
g.close()

