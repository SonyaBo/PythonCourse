"""
def factorial(x: int) -> int:
    res = 1
    for i in range(1,x+1):
        res = res * i
    return res

print(factorial(2))

def average(*args: tuple[int]) -> float:
    sum = 0
    for i in args:
        sum += i
    return sum/len(args)

print(average(2,10))

def format_string(template,**kwargs):
    text = template.format(**kwargs)
    print(text)
format_string("hi {neco}",neco="hi")


def merge_dicts(*dicts):
    res = {}
    for i in range(len(dicts)):
        res.update(dicts[i])
    return res

print(merge_dicts({"k1":1},{"k2":2}))


def even_odd(*nums: tuple[int]) -> tuple[list[int], list[int]]:
    odd = []
    even = []
    for i in nums:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    return odd,even

"""
def filter_list(nums: list[int],p: int) -> list[int]:
    res = []
    for num in nums:
        if num > p:
            res.append(num)
    return res

def filter_list_2(nums: list[int],p: int) -> list[int]:
    return list(filter(lambda x: x>p,nums))


print(filter_list([2,5,4,6,3,5,45,6,2],3))

def calculator(x: int, y: int, op: str) -> int:
    pass

def something(dicts,keys):
    used = {}
    res = []
    for i in dicts:
        list_key = []
        for k in keys:
            list_key.append(i[k])
        key = tuple(list_key)
        if k not in used:
            used.dd(key)
            res.append(i)

"""for i in range(1,len(banknotes)):
    if sum(banknotes[:i] * amaount_of_bank) > amount:
        used_banknotes = banknotes[:i]
        break 

res = dict.fromkeys(used_banknotes,0)
while amount:
    curr_bank = used_bank[-1]
    res[curr_bank] += 1
    amount -= curr_bank
    if amount <= sum(used_bank[:-1]* amount_of_bank)
        used_bank = used_bank[:-1]
"""
