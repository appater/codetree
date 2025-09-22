N = int(input())

command = []
num = []
count = 0

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push_back" :
        num.append(int(line[1]))
    else:
        num.append(0)

# Please write your code here.
    if line[0] == 'get' :
        print(num[int(line[1])-1])
    
    if line[0] == 'size' :
        for i in range(len(num)) :
            if num[i] != 0 :
                count += 1
        print(count)

    if line[0] == 'pop_back' :
        for j in range(len(num)-1, 0, -1):
            if num[j] != 0 :
                num.pop(j)
    
    count = 0