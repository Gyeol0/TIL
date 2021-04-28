# Graph

## 개념

* 그래프는 아이템(사물)들과 이들 사이의 연결 관계를 표현
* 정점들으 ㅣ집합과 이들을 연결하는 간선들의 집합으로 구성된 자료구조
  * V : 정점의 개수
  * E : 간선의 개수
  * 최대 V*(V-1)/2 간선 가능
* 선형 자료구조나 트리 자료구조로 표현하기 어려운 N:N 관계를 가지는 원소들을 표현하기 용이

### 유형

* 무향 그래프(Undirected Graph)
* 유향 그래프(Directed Graph)
* 가중치 그래프(Weighted Graph)
* 사이클 없는 방향 그래프(DAG, Directed Acyclic Graph)
* 완전 그래프
  * 정점들에 대해 가능한 모든 간선을 가진 그래프
* 부분 그래프
  * 일부의 정점이나 간선을 제외한 그래프

### 인접(Adjacency)

* 두개의 정점에 간선이 존재하면 서로 인접
* 완전 그래프의 모든 정점은 인접

### 경로

* 간선들을 순서대로 나열한 것
* **단순 경로** : 한 정점을 최대한 한 번만 지나는 경로
* **사이클(Cycle)** : 시작한 정점에서 끝나는 경로

### 

## 표현

* 간선의 정보를 저장하는 방식

### 인접행렬(Adjacent Matrix)

* V * V 크기의 2차원 배열을 이용해서 간선 정보를 저장
* 배열의 배열(포인터)
* 두 정점을 연결하는 간선의 유무를 행렬로 표현
* 행 번호, 열 번호를 정점에 대응
* 무향 그래프
  * i 번째 행의 합 = i 번째 열의 합 = Vi의 차수
* 유향 그래프
  * 행 i의 합 = Vi의 진출 차수
  * 열 i의 합 = Vi의 진입 차수

### 인접 리스트(Adjacent List)

* 각 정점마다 해당 정점으로 나가는 간선의 정보를 저장
* 각 정점에 대한 인접 정점들을 순자적으로 표현
* 하나의 정점에 대한 인접 정점들을 각각 노드로 하는 연결 리스트로 저장
* 무향 그래프
  * 노드 수 = 간선의 수 * 2
  * 각 정점의 노드 수 = 정점의 차수
* 유향 그래프
  * 노드 수 = 간선의 수
  * 각 정점의 노드 수 = 정점의 진출 차수

### 배열

* 간선(시작, 끝 정점)을 배열에 연속적으로 저장

## 그래프 순회(탐색)

* 모든 정점을 빠짐없이 탐색
* 깊이 우선 탐색(Depth First Search, DFS)
* 너비 우선 탐색(Breadth First Search, BFS)

### 깊이 우선 탐색(Depth First Search, DFS)

* 시작 정점의 한 방향으로 갈 수 있는 경로가 있는 곳까지 깊이 탐색, 갈 곳이 없게 되면 마지막 갈림길 정점으로 되돌아와서 탐색을 반복하여 모든 정점을 반복하는 순회방법
* 가장 마지막 갈림기르이 정점으로 되돌아가 반복해야 하므로 후입선출 구조의 스택 사용



#### 구현 - 재귀

```python
def dfs(G, V):
    visited[v] = True
    for W in adjacency(G, V):	# V에 인접인 모든 노드 w
        if visited[W] != True:
            dfs(G, W)
```

### 구현 - 반복

```python
def dfs(v):
    stack = []
	visited = []
    stack.append(v)
    visited.append(v)
    while stack:
        v = stack.pop()
        if v not in visited:	# visited를 [0]*E 만들어서 0, 1로 확인해도됨
            visited.append(v)
            for w in adjacency(v):
                if w not in visited:
                    stack.append(w)
```



### 너비 우선 탐색(Breadth First Search, BFS)

* 탐색 시작점의 인접한 정점들을 먼저 모두 차례로 방문한 후에, 방문했던 정점을 시작점으로 하여 다시 인접한 정점들을 차례로 방문
* 인접한 정점들에 대해 탐색을 한 후, 차례로 다시 너비 우선 탐색을 진행하야 하므로, 선입선출 형태의 큐 활용

```python
def BFS(G, V): # 그래프 G, 탐색 시작점 V
    visited = [0] * n # n : 정점의 개수
    queue = []
    queue.append(v)
    while queue:
        t = queue.pop(0) # front 반환
        if not visited[t]: # 방문하지 않은 곳이면
            visited[t] = True # 방문
        for i in G[t]: # t와 연결된 모든 선에 대해
            if not visited[i]:
                queue.append(i) # 방문하지 않은 곳이면 큐에 넣기
```



## 서로소 집합(Disjoint-sets)

* 서로소 또는 상호 배타 집합들은 서로 중복 포함된 원소가 없는 집합들이다.
* 교집합이 없다
* 집합에 속한 하나의 특정 멤버를 통해 각 집합들을 구분한다.
  * 대표자(representative)
* 상호배타 집합을 표현하는 방법
  * 연결 리스트
  * 트리
* 상호배타 집합 연산
  * Make-Set(x)
  * Find-set(x)
  * Union(x, y)

### 연결리스트

* 같은 집합의 원소들은 하나의 연결리스트로 관리
* 연결리스트의 맨 앞의 원소를 집합의 대표 원소로 삼는다
* 각 원소는 집합의 대표 원소를 가리키는 링크를 가짐



### 트리

* 하나의 집합을 하나의 트리로 표현
* 자식노드가 부모노드를 가리키며 루트노드가 대표자
* Make-Set(a) ~ Make-Set(f)
  * P[i] = i, 자기 자신이 대표
  * P[i] = i의 대표 원소
* Union(c, d), Union(e, f)
  * P[4] = 3, d의 대표원소를 c의 대표원소로 바꿔라
  * P[6] = 5, f의 대표원소를 e의 대표원소로 바꿔라
* Find-Set(d)
  * d의 대표원소 반환
  * c, 3 
* Make-Set(x) : 유일한 멤버 x를 포함하는 새로운 집합을 생성하는 연산

```python
def Make_Set(x):
    p[x] <- x
```

* Find-Set(x) : x를 포함하는 집합을 찾는 연산

```python
def Find_Set(x):
    if x == p[x]:
        return x
    else:
        return Find_Set(p[x])
```

```python
def Find_Set(x):
    while x != p[x]:
        x = p[x]
    return x
```

* Union(x, y) : x와 y를 포함하는 두 집합을 통합

```python
def Union(x, y):
    p[Find_Set(y)] = Find_set(x)
```

### 효율

* 연산의 효율을 높이는 방법
* Rank를 이용한 Union
  * 각 노드는 자신을 루트로 하는 subtree의 높이를 Rank라는 이름으로 저장
  * 두 집합을 합칠 때 Rank가 낮은 집합을 Rank가 높은 집합에 붙인다
  * 최대 높이가 늘어나지 않음
    * 두 Rank가 같을 때에는 최대 높이 1 증가
* Path compression
  * Find-Set을 행하는 과정에서 만나는 모든 노드들이 직접 root를 가리키도록 포인터를 바꾸어줌

* Make-Set(x) Rank

```python
# p[x] : 노드 x의 부모 저장
# rank[x] : 루트 노드가 x인 트리의 랭크 값 저장
def Make_Set(x):
    p[x] = x
    rank[x] = 0
```

* Union(x, y) Rank

```python
def Union(x, y):
    Link(Find_Set(x), Find_Set(y))
```

```python
def Link(x, y):
    if rank[x] > rank[y]:
        p[y] = x
    else:
        p[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1
```



## 최소 신장 트리(Minimum Spanning Tree)

* 그래프 최소 비용 문제
* 모든 정점을 연겨라는 간선들의 가중치의 합이 최소가 되는 트리
* 두 정점 사이의 최소 비용의 경로 찾기
* 신장 트리
  * n개의 정점으로 이루어진 무방향 그래프에서 n개의 정점과 n-1개의 간선으로 이루어진 트리
* 최소 신장트리
  * 무방향 가중치 그래프에서 신장 트리를 구성하는 간선들의 가중치의 합이 최소인 신장 트리

### Prim 알고리즘

* 하나의 정점에서 연결된 간선들 중에 하나씩 선택하면서 MST 만들어감, 그리디
  1. 임의 정점 하나 선택, 시작
  2. 선택한 정점과 인접한 정점들 중의 최소 비용의 간선이 존재하는 정점 선택
  3. 모든 정점이 선택될 때 까지 1, 2반복
* 서로소인 2개의 집합 정보 유지
  * 트리 정점들 : MST를 만들기 위해 선택된 정점들
  * 비트리 정점들 : 선택되지 않은 정점들

```python
def prim(start):
    INF = 999999999999
    visit = [0] * N
    distance = [INF] * N
    distance[start] = 0

    for _ in range(N):
        min_value = INF
        for i in range(N):		# 방문 안한 정점중 최소 가중치 정점 찾기
            if visit[i] == 0 and distance[i] < min_value:
                now = i
                min_value = distance[i]
        
        # 최소 가중치 정점 방문처리
        visit[now] = 1
        
        for i in range(N):
            if visit[i] == 0:
                # 가중치 갱신
                distance[i] = min(distance[i], arr[now][i])  # now부터 i까지의 거리
    # 최소 거리 합
    return sum(distance)
```



```python
from heapdict import heapdict

def prim(graph, first):
    mst = []
    keys = heapdict()
    previous = dict()   
    total_weight = 0

    #초기화
    # 자기 자신 선택하지 않도록
    for node in graph.keys():
        keys[node] = float('inf')
        previous[node] = None
    keys[first], previous[first] = 0, first

    while keys:
        current_node, current_key = keys.popitem()
        # MST에 추가
        mst.append([previous[current_node], current_node, current_key])
        total_weight += current_key
        # MST에 추가하고 MST와 다른 정점들과의 거리 갱신
        for adjacent, weight in graph[current_node].items():
            if adjacent in keys and weight < keys[adjacent]:
                keys[adjacent] = weight
                previous[adjacent] = current_node
    return mst, total_weight
```

* 단점 : 우선순위 큐를 사용하지 않으면 최솟값을 찾는데 오래 걸린다



### KRUSKAL 알고리즘

1. 최초, 모든 간선을 가중치에 다라 오름차순으로 정렬
2. 가중치가 가장 낮은 간선부터 선택하면서 트리를 증가
   * 사이클이 존재하면 다음으로 가중치가 낮은 간선 선택
   * 대표 원소를 비교한다. 대표원소가 같으면 싸이클이 생성
3. n-1개의 간선이 선택될 때까지 1, 2 반복

```python
vertices = [] # 정점들
p = dict()
rank = dict()
# edge는 입력 받아서 사용(간선)
def find(node):
    if p[node] != node:
        p[node] = find(p[node])
    return p[node]

def make_set(node):
    p[node] = node
    rank[node] = 0
   
def union(v, u):
    root1 = find(v)
    root2 = find(u)
    
    if rank[root1] > rank[root2]:
        p[root2] = root1
    else:
        p[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1
           
def kruskal(graph):
    mst = []
    # 초기화
    for node in vertices:
        make_set(node)
    
    # (node1, node2, weight)
    # 가중치 기준으로 정렬
    edge = sorted(edge, lambda x: x[2])
    
    for e in edge:
        node1, node2, weight = e
        # 대표 원소가 다른지 확인, 같으면 사이클
        if find(node1) != find(node2):
            union(node1, node2)
            mst.append(e)
    return mst
```



## 최단 경로

* 간선의 가중치가 있는 그래프에서 두 정점 사이의 경로들 중에 간선의 가중치의 합이 최소

* 하나의 시작 정점에서 끝 정점까지

  * 다익스트라(dijkstra) 알고리즘
    * 음의 가중치를 허용하지 않음
  * 벨만-포드(Bellman-Ford) 알고리즘
    * 음의 가중치 허용

* 모든 정점들에 대한 최단 경로

  * 플로이드-워샬(Floyd-Warshall) 알고리즘

  

### 다익스트라(dijkstra)

* 시작 정점에서 거리가 최소인 정점을 선택해 나가면서 최단 경로를 구하는 방식
* 시작 정점(s)에서 끝 정점(t)까지의 최단 경로에 정점x 가 존재
* 최단 경로는 s에서 x까지의 최단경로와 x에서 t까지의 최단경로로 구성
* 그리디 알고리즘

```python
# graph에는 정점 사이의 거리
#모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    #a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))
INF = int(1e9)
distance = [INF] * (n+1)
visit = [False] * (n+1)

# 최단 경로를 가진 방문하지 않은 노드 찾기    
def find_lowest_node(graph, start):
    low_cost = INF
    low_cost_node = 0
    for i in range(1, n+1):
        if distance[i] < low_cost and not visit[node]:	# 사용한 node인지, 최소인지 확인
            low_cost = distance[i]
            low_cost_node = i
   	return low_cost_node

def dijkstra(start):
    distance[start] = 0
    visit[start] = True
    current = start
    # start와 연결된 노드들
    for node, cost in graph[start]:
        distance[node] = cost
        
    # 현재 start를 제외하고 전체 n-1개의 노드 반복
    for i in range(n-1):
        cuerrent = find_lowest_node(graph, start)
        visit[current] = True
        for node, cost in graph[current]:
            new_cost = distance[current] + cost
            if new_cost < distance[node]:
                distance[node] = new_cost
                
dijkstra(start)
print(distance[end])
```

```python
import heapq
INF = int(1e9) 

#각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n + 1)]
#최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

#모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    #a번 노드에서 b번 노드로 가는 비용이 c
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    #시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 힙 푸시
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        #가장 최단 거리가 짧은 노드에 대한 정보 꺼내기(힙)
        dist, now = heapq.heappop(q)
        # 바로 가는게 더 빠르면 continue
        if distance[now] < dist:
            continue
        # 현재 노드(now)와 연결된 노드
        for node, cost in graph[now]:
            # 지금 i를 거쳐서 가는게 더 짧으면 distance 갱신하고 큐에 삽입
            if dist + cost < distance[node]:
                distance[node] = dist + cost
                heapq.heappush(q, (dist+cost, node))

dijkstra(start)
```

