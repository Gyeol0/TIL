N = 20 # 사탕 개수

queue = [(1, 0)] # 처음 초기화

#(0, 0) [0] : 사람 번호, [1] : 직전 까지 받았던 마이쮸의 개수

new_people = 1
last_people = 0

while N > 0:
    num, cnt = queue.pop(0) # 받으러온 사람, 저번까지 받은 개수

    last_people = num # 마지막으로 받으러 온 사람
    cnt += 1 # 저번 보다는 한 개 더 챙겨야함

    N -= cnt # num이라는 친구가 cnt 개수만큼 가져감
    new_people += 1
    queue.append((num, cnt))# 맨뒤로 가서 다시 줄을 섬
    queue.append((new_people, 0))