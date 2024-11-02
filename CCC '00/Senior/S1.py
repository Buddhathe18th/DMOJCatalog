quarters=int(input())
plays1=int(input())
plays2=int(input())
plays3=int(input())

turns=0
while quarters>0:
    quarters=quarters-1

    if turns%3==0:
        plays1=plays1+1
        if plays1%35==0:
            plays1=0
            quarters=quarters+30
    elif turns%3==1:
        plays2=plays2+1
        if plays2%100==0:
            plays2=0
            quarters=quarters+60
    else:
        plays3 = plays3 + 1
        if plays3 % 10 == 0:
            plays3 = 0
            quarters = quarters + 9
    turns = turns + 1
print("Martha plays "+str(turns)+" times before going broke.")