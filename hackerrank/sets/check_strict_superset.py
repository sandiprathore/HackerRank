set_s = set(map(int,(input().split())))
count = 0
n = int(input())
for i in range(n):
    test_set = set(map(int,(input().split())))
    if (set_s.issuperset(test_set)):
        count = count + 1 
print(count==n)