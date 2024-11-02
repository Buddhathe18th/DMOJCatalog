streams=int(input())
flow=[]
for i in range(streams):
    flow.append(int(input()))

command=input()
while command!="77":
    if command=="99":
        index=int(input())
        percent=int(input())
        currentflow=flow[index-1]
        flow.insert(index-1, percent*currentflow/100)
        flow[index]=currentflow*(100-percent)/100
    elif command=="88":
        index = int(input())
        x=flow.pop(index-1)
        flow[index-1]=flow[index-1]+x
    command=input()

for i in flow:
    print(int(i),end=" ")