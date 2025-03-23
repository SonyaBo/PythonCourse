"""
list2 = [x for x in range(5,101)]

list2 = [x for x in range(5,101) if x%2]

list2 = ["hi","bye","hello"]
list1 = [x[0] for x in list2]


print("".join(list1))


list1 = [x for x in list2 if x<0]

x = int(input("num1: "))
y = int(input("num2: "))

list2 = [x**2 for x in range(x,y+1)]
"""
list2 = [1,2,-4]


res = [x for x in list2 if x%2==0]
print(res)



