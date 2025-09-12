a = int(input())
num = 0

for _ in range(a):
    b, c = map(int, input().split())
    for i in range(b, c+1):
        if i % 2 == 0 :
            num += i
    print(num)
    num = 0