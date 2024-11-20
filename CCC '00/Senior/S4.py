import math

distance=int(input())

numberOfClubs=int(input())
clubs=[]
for i in range(numberOfClubs):
    clubs.append(int(input()))

clubs.sort(reverse=True)


swings=1000000001
def solve(distance,clubs,counter):
    global swings
    if counter>=swings:
        return

    if distance == 0:
        return

    for i in clubs:
        if distance>i:
            solve(distance-i,clubs,counter+1)

        elif distance==i:

            swings=min(swings,counter+1)
        else:
            clubs=clubs[1:]


    if clubs!=[]:
        solve(distance, clubs[1:], counter)

if distance%math.gcd(*clubs)!=0:
    print("Roberta acknowledges defeat.")
else:
    solve(distance,clubs,0)
    if swings == 1000000001:
        print("Roberta acknowledges defeat.")
    else:
        print("Roberta wins in " + str(swings) + " strokes.")


