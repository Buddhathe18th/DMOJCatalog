start,length=list(map(int,input().split()))

print("Sun Mon Tue Wed Thr Fri Sat")
lines=(start+length)/7
for i in range(start):
    print("    ",end="")
for i in range(start+1,start+length):
    print(f"{str(i-start) : >3}",end="")
    if i%7==0:
        print()
    else:
        print(" ",end="")

print(f"{str(length) : >3}",end="")