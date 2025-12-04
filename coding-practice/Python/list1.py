# 10,20,30,40,50,20,30

inp = input().split(',')
l = [int(item) for item in inp]
#remove duplicates
#newl = []
#for i in l:
#    if i in newl:
#        continue
#    else:
#        newl.append(i)
#print(newl)
s = set(l)
newl = list(s)
print(s)