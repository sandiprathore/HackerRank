n = input().split()
s = list(map(int,input().split()))
A = set(map(int,input().split()))
B = set(map(int,input().split()))
count = 0 
for i in s:
    if i in A:
        count = count + 1
    if i in B:
        count = count - 1 
print(count)