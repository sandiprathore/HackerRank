if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    max_num = max(arr)
    while max(arr) == max_num:
        arr.remove(max_num)
    print(max(arr))