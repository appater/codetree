a = int(input())

for i in range(a,0,-1) :
    for k in range(i) :
        print("*", end=' ')
    for j in range(a-i):
        print("",end=' ')
    print("")