numcows,candy = list(map(int,input().split()))
cows=list(map(int,input().split()))
candy=list(map(int,input().split()))

for i in candy:
    temp=[0,i]
    for j in range(len(cows)):
        if cows[j]>temp[0]:
            if cows[j]>temp[1]:
                cows[j]=cows[j]+temp[1]-temp[0]
                break
            else:
                k=cows[j]
                cows[j]=cows[j]+cows[j]-temp[0]

                temp[0]=k


for i in cows:
    print(i)
