a = int(input())

for i in range(a) :
    for j in range(a) :
        if j % 2 == 0 :
            print(i+1, end='')
        else :
            print(a-i, end='')
    print()