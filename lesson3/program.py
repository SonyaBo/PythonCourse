"""
list = [1,2,3,4,5,6,7,8,5,2,3]

print(min(list))
print(max(list))

print(sum(list)/len(list))

print(sorted(list,reverse=True)[1])

if list == sorted(list):
    print("yes")
else:
    print("no")
"""
x= 1
y= 4
"""
for i in range(x,y, 2):
    print(i)

print(sum(range(x+1,y)))

print(sorted(range(x,y+1),reverse=True))

num = 10
fib = [0,1]

for i in range(2,num+1):
    fib.append(fib[-2]+fib[-1])

print(fib[-1])
"""
