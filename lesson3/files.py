"""
with open("sample.txt","r") as f:
    print(f.read())

lines = []
while True:
    data = input("Write something: ")
    lines.append(data)
    con = input("u done? y/n")
    if con != "n":
        break
with open("output.txt","w") as f:
    for i in range(len(lines)):
        f.write(lines[i]+"\n")

data = ''
with open("source.txt","r") as f:
    data = f.read()

with open("destination.txt","w") as f:
    f.write(data)
"""
with open("numbers.txt","r") as f:
    neco = f.read().split("\n")
    print(max([int(x) for x in neco if x.isdigit()]))



with open("temp.txt","r") as f_c, open("temp_fahr.txt","w") as f_f:
    neco = f_c.read().split("\n")
    for i in neco:
        if i.isdigit():
            x = int(i)* 9/5 +32
            f_f.write(str(x)+"\n")

with open("words.txt","r") as f_r:
    f_r.read().split("")





