def Memory(bit):
    count = 0
    current = '0'
    other = '1'
    for i in bit:
        if i != current:
            current, other = other, current
            count += 1
    return count

T = int(input())
for test in range(1, T+1):
    bit = input()
    print(f'#{test}', Memory(bit))