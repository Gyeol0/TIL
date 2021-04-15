def reward(s, idx, count):
    global max_reward
    if idx == len(s):
        if count >= 0:
            if count % 2:
                s[-1], s[-2] = s[-2], s[-1]
            value = 0
            for i in range(len(s)):
                value += int(s[i]) * (10 **(len(s)-i-1))
            max_reward = max(max_reward, value)
            if count % 2:
                s[-1], s[-2] = s[-2], s[-1]
            return

    for k in range(idx, len(s)):
        s[idx], s[k] = s[k], s[idx]
        if idx == k:
            reward(s, idx+1, count)
        else:
            reward(s, idx+1, count-1)
        s[idx], s[k] = s[k], s[idx]

T = int(input())
for test in range(1, T+1):
    s, count = input().split()
    s = list(s)
    count = int(count)
    max_reward = 0
    reward(s, 0, count)
    print(f'#{test}', max_reward)