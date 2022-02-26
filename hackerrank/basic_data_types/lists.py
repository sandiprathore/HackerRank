if __name__ == '__main__':
    n = int(input())
    Output_list = []
    for i in range(0,n):
        input_list = input().split()
        if input_list[0] == "print":
            print(Output_list)
        elif input_list[0] == "insert":
            Output_list.insert(int(input_list[1]),int(input_list[2]))
        elif input_list[0] == "remove":
            Output_list.remove(int(input_list[1]))
        elif input_list[0] == "pop":
            Output_list.pop()
        elif input_list[0] == "append":
            Output_list.append(int(input_list[1]))
        elif input_list[0] == "sort":
            Output_list.sort()
        else:
            Output_list.reverse()
