"""
numbers = [1,2,3,4,5,6,7,8,9,10]
sum = 0
for i in numbers:
    sum += i
    print(i**2)
print(sum)


for j in text:
    print(j)

text = "hello world"

print(text[:5])
print(text[-5:])
list = []

for k in range(20):
    list.append(k+1)
    if (k+1)%3==0:
        print(k+1)

count = 0
sum = 0
while count<=100:
    sum +=count
    count += 1
print(sum)



while True:
    var = input("Number: ")
    if var == "0" or var == "exit":
        break
    try:
        print(int(var)**2)
    except ValueError as e:
        print(f"Number pls. {e}")

words = ["cat","dog","duck","cow","cat","dog"]
unique = []
for word in words:
    if word in unique:
        continue
    unique.append(word)
print(unique)


wordik = input("Gimme word:")
count = 0
lett = ["a","i","e","o","u"]
for i in lett:
    count += wordik.count(i)

print(count)



sen = "Python is a great language."
print(sen)
word = input("Which word u wanna change: ")

print(sen.replace(word,"horrible"))




list = [1,2,3,4,1]
changed = []

for l in list:
    if l in changed:
        continue
    changed.append(l)

min = list[0]
max = list[0]

for i in list:
    if i < min:
        min = i
    if i > max:
        max = i



n = 60
count = 1

while count<=n:
    if count%5==0 and count%3==0:
        print("FizzBuzz")
    elif count%3==0:
        print("Fizz")
    elif count%5==0:
        print("Buzz")
    else:
        print(count)
    count +=1
"""
#6-2-5
#6-3-4
#6-4-3

#8-2-7
#8-3-6
 #Facebook 1.0
list = [1,10,3,5,4,6]
result = []
count = 0
min = list[0]

while count<=len(list):
    for i in range(3):

        if min>list[i]:
            min = list[i]
    result.append(min)
    count+=1
print(result)

"""


#Facebook 2.0
list = [1,2,1,4,0,3]
result = [] #2,4,4,-1,3,-1
count = 0

while count<len(list):
    for i in list:
        if list[count]<i:
            result.append(i)
            break
        elif i == list[-1]:
            result.append(-1)
        else:
            continue
    count+=1

print(result)
"""