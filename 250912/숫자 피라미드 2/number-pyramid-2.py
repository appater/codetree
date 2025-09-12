a = int(input())
num = 1

for i in range(a):
    for j in range(i+1) :
        print(num, end = ' ')
        num += 1
    print()