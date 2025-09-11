a = int(input())

for i in range(a):
    for j in range(2 * i+1) :
        print("*", end ='')
    for k in range(i) :
        print("", end = ' ')
    print()