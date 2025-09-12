arr = [list(map(int, input().split())) for _ in range(4)]
num = 1
total = 0
for i in range(4) :
    for j in range(num) :
        total += arr[i][j]
    num += 1

print(total)