"""
#INTRO
print('Hello world!')
a = int(input("Number 1:"))
b = int(input("Number 2:"))
print(a+b)
print(a-b)
print(a*b)
print(a/b)

text = input("Write python:")
#print(text*3)

name = input("Whats your name: ")


print(f"Hi I'm {name} and I'm {age} y.o.")

print((5+3)*2**2)

print(text+str(3))

# BOOLEAN
print(bool(-10))
print(bool(0))

print(bool(""))
print(bool("sadsd"))


"""

age = int(input("how old are you: "))
name = input("whats your name: ")
gender = input("male or female m/f")
"""
if 'a' in name:
    print("hell nah")
    quit()

if age>100:
    print("bullshit")
elif age>18:
    print("youre adult")
else:
    print("a minoor")

if age % 2==0:
    print("even age")
    if 'v' in name or 'V' in name:
        print("Congrats, you've won")
else:
    print("odd age")
    print("Sorry, u didn't win anything")
"""
"""
if age<15:
    print("go play tenis")
elif age>15:
    if "c" in name or "t" in name:
        print("dont play anything")
    else:
        if gender == "f":
            print("go play basketball")
        elif gender == "m":
            print("go play football")
"""
if age<15:
    print("go play tenis")
elif age>15:
    if "c" not in name and "t" not in name:
        if gender == "f":
            print("go play basketball")
        elif gender == "m":
            print("go play football")
    else:
        print("dont play anything")







