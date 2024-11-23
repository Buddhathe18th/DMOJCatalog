f = open("herding.in", "r")

cow=list(map(int,f.readline().split()))
cow=sorted(cow)

g = open("herding.out", "w")

# minimum
if (cow[0]+1==cow[1]) and (cow[1]+1==cow[2]):
    g.write("0\n")
elif (cow[0]+2==cow[1]) or (cow[1]+2==cow[2]):
    g.write("1\n")
else:
    g.write("2\n")

# maximum
g.write(str(max(cow[1]-cow[0],cow[2]-cow[1])-1))
# counter=0
# while not ((cow[0]+1==cow[1]) and (cow[1]+1==cow[2])):
#     if cow[2]-cow[1]>=cow[1]-cow[0]:
#         cow[0]=cow[2]-1
#     else:
#         cow[2]=cow[0]+1
#     counter += 1
#     cow=sorted(cow)
#
# g.write(str(counter))
g.close()

