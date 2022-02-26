n = int(input())
s = set(map(int,input().split()))
num = int(input())
for i in range(num):
    operation = input().split()
    if operation[0] == 'intersection_update':
        s.intersection_update(set(map(int,input().split())))
    elif operation[0] == 'update':
        s.update(set(map(int, input().split())))
    elif operation[0] == 'symmetric_difference_update':
        s.symmetric_difference_update(set(map(int, input().split())))
    elif  operation[0] == 'difference_update':
        s.difference_update(set(map(int, input().split())))
print(sum(list(s)))