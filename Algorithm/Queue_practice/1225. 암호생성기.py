def Password(arr):
    front = 0
    rear = 7
    c = 1
    while True:
        rear = (rear + 1) % 8
        arr[rear] = arr[front] - c
        front = (front + 1) % 8
        c += 1
        if c == 6:
            c = 1
        if arr[rear] <= 0:
            arr[rear] = 0
            break
    for _ in range(8):
        print(arr[front], end = ' ')
        front = (front + 1) % 8
    print()

for _ in range(10):
    test = int(input())
    arr = list(map(int, input().split()))
    print(f'#{test}', end = ' ')
    Password(arr)