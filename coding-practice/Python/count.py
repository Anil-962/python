a = input().split(',')
c = (int(item) for item in a)
n = int(input())
count = 0
for i in c:
    if i == n:
        count +=1
print(count)