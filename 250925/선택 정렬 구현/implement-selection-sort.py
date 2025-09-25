n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
count = 0
while count < n :
    for i in range(len(arr)-1) :
        min = i 
        for j in range(i+1, len(arr)) :
            if arr[j] < arr[min] :
                min = j
                tmp = arr[i]
                arr[i] = arr[min]
                arr[min] = tmp
    count += 1

for i in range(len(arr)) :
    print(arr[i], end = ' ')