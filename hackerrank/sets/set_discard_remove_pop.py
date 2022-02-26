n = int(input())
s = set(map(int,input().split()))
num = int(input())
for i in range(num):
    opration = input().split()
    if opration[0]=="remove":
        s.remove(int(opration[1]))
    elif opration[0]=="discard":
        s.discard(int(opration[1]))
    else :
        s.pop()
print(sum(list(s)))