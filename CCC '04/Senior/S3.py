import re

table=[]
for i in range(10):
    lines=[]
    list=input().split(" ")
    for k in list:
        if re.match("\d+",k):
            lines.append(int(k))
        else:
            lines.append(k.split("+"))
    table.append(lines)


print(table)





