n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
count = 0
while count < 7:
    for i in range(0, len(arr)-1) :
        if arr[i] > arr[i+1] :
            tmp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = tmp
    count += 1

for i in range(len(arr)) :
    print(arr[i], end = ' ')