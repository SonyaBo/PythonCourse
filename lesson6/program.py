def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(5)
print(result) #120
def fibonacci(num):
    if num==0 or num ==1:
        return num
    else:
        return fibonacci(num-1)+fibonacci(num-2)

print(fibonacci(10)) #55

def polyndrom(t):
    if t == t[::-1]:
        return True
    else:
        return False

def polyndrom_re(t):
    """
    if len(t) == 1 or len(t) == 0:
        return True
    else:
        if t[0]==t[-1]:
            return polyndrom(t[1:len(t)-1])
        else:
            return False
    """
    if len(t) <2:
        return True
    if t[0] == t[-1]:
        return polyndrom_re(t[1:-1])
    else:
        return False


nu = [3,2,6,2,1,0,3]
nu2 = [2,3]
def jumping(nums):
    if len(nums) == 0 or len[0] >= len(nums):
        return True
    if nums[0] == 0:
        return False
    return jumping(nums[nums[0]:])

print(jumping(nu,3))