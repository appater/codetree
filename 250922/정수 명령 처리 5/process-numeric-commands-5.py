N = int(input())

command = []
num = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push_back" or line[0] == "get":
        num.append(int(line[1]))
    else:
        num.append(0)

# Please write your code here.
dynamic_array = []

for i in range(N) :
    current_command = command[i]

    if current_command == "push_back" :
        dynamic_array.append(num[i])

    elif current_command == "pop_back" :
        if dynamic_array :
            dynamic_array.pop()
    
    elif current_command == "size" :
        print(len(dynamic_array))

    elif current_command == "get" :
        k = num[i]
        print(dynamic_array[k-1])