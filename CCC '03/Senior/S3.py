flooringAvailible=int(input())

rows=int(input())
cols=int(input())

floor=[]
for i in range(rows):
    lines = []
    x = input()
    for k in x:
        lines.append(k)
    floor.append(lines)

rooms=[]

def roomsLeft(floor):
    for i in range(len(floor)):
        for j in range(len(floor[i])):
            if floor[i][j]==".":
                return (i,j)
    return False


def searchFloor(row,col,floor,neighboors):
    floor[row][col] = "A"
    neighboors.append((row,col))
    try:
        if floor[row+1][col]==".":
            neighboors=searchFloor(row+1,col,floor,neighboors)
    except:
        print(end="")

    try:
        if floor[row-1][col]==".":
            neighboors=searchFloor(row-1,col,floor, neighboors)
    except:
        print(end="")
    try:
        if floor[row][col+1]==".":
            neighboors=searchFloor(row,col+1,floor,neighboors)

    except:
        print(end="")

    try:
        if floor[row][col-1]==".":
            neighboors=searchFloor(row,col+-1,floor, neighboors)
    except:
        print(end="")

    return neighboors

while roomsLeft(floor)!=False:
    row, col = roomsLeft(floor)
    room=searchFloor(row,col,floor,[])
    rooms.append(len(room))



print(rooms)
rooms.sort(reverse=True)

sum=0
i=0
while sum+rooms[i]<=flooringAvailible:
    sum=sum+rooms[i]
    i=i+1


print(i)
print(flooringAvailible-sum)