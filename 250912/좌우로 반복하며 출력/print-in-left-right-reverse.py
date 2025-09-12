a = int(input())
count = 1

for _ in range(a) :
    if count % 2 == 1 :
       for i in range(1, a+1) :
            print(i, end='')
    else :
        for i in range(a, 0, -1) :
            print(i, end='')
    print()
    count += 1