f = open("billboard.in", "r")
g = open("billboard.out", "w")

lawnx1,lawny1,lawnx2,lawny2 =list(map(int,f.readline().split()))
foodx1,foody1,foodx2,foody2 =list(map(int,f.readline().split()))

if foodx1<=lawnx1 and foodx2>=lawnx2 and foody1<=lawny1 and foody2>=lawny2:
    g.write("0")
elif ((foodx1<=lawnx1 and foodx2<=lawnx2 and foody1<=lawny1 and foody2>=lawny2)):
    g.write(str((lawny2 - lawny1) * (lawnx1 - foodx1)))
elif ((foodx1>=lawnx1 and foodx2>=lawnx2 and foody1<=lawny1 and foody2>=lawny2)):
    g.write(str((lawny2-lawny1)*(foodx2-lawnx2)))
elif ((foody1<=lawny1 and foody2<=lawny2 and foodx1<=lawnx1 and foodx2>=lawnx2)):
    g.write(str((lawnx2 - lawnx1) * (lawny2 - foody2)))
elif ((foody1>=lawny1 and foody2>=lawny2 and foodx1<=lawnx1 and foodx2>=lawnx2)):
    g.write(str((lawnx2-lawnx1)*(foody1-lawny1)))
else:
    g.write(str((lawny2-lawny1)*(lawnx2-lawnx1)))
g.close()

