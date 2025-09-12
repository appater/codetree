start, end = map(int, input().split())

# Please write your code here.
endcount = 0
for i in range(start, end+1) :
    count = 0
    for j in range(1, i+1) :
        if i % j == 0 :
            count += 1
    if count == 3 :
        endcount += 1
print(endcount)