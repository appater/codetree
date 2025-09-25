n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
count = 0
while count < n :
    for i in range(1, len(arr)) :
        j = i -1
        key = arr[i]
        while j >= 0 and arr[j] > key :
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    count += 1

for i in range(len(arr)) :
    print(arr[i], end=' ')