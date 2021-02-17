def itoa(num):
    num_str = ''
    while num:
        num_str = chr(num % 10 + 48) + num_str
        num //= 10
    return num_str
num = 1234
num_str = itoa(num)
print(num_str, type(num_str)) # 1234 <class 'str'>