# 다이나믹프로그래밍 DP

[toc]

## 다이나믹프로그래밍(DP)

> [출처 : 다이나믹 프로그래밍(DP)](https://infinitt.tistory.com/246)

- 개념 : 문제를 더 작은 단위로 쪼개어 해결하는 알고리즘. **(분할 정복 알고리즘과 비슷하다.)**
- 핵심은, **그 작은 단위의 문제들이 반복해서 일어나기 때문에, 그값들을 저장해놓는 식으로 해결해나가는 알고리즘**
- **(다이나믹이라는 이름에는 아무 뜻도 없다고 한다.)** 



### **다이나믹 프로그래밍을 사용하기 위한 조건**

**1. 부분 문제들이 겹치는가 (반복 되는가)**  

  ex ) 피보나치 수 : **N번째 항**(큰 문제) = **N-1번째 항**(작은 문제) + **N-2 번째 항**(작은 문제)

- 피보나치의 특성을 잘 살펴보면 Fibo(10)을 구할때는 `Fibo(9)+Fibo(8)....Fibo(1)` 까지 모두 필요함
-  이때 메모이제이션을 통해 배열에 저장해놓는다면, Fibo(12)를 구할때는 , 1~10번째 항까지 이미 메모가 되어있으므로, 11번째 항만 연산하면 되므로 효율적

> *** 재귀함수로 구현한 피보나치 (Python)**

```python
def fibonacci(n):
	if n<=1 :
		return n
	
	else : return fibonacci(n-1) + fibonacci(n-2)
```

 

> **다이나믹 프로그래밍으로 구현한 피보나치 (memoization)**
>
> **한번 거쳤던 항들은 모두 memo에 저장된다. **
>
> **따라서, 다음에 구할때는 연산없이 리턴이 가능하다.**

```python
memo = [0 for i in range(100)]
def fibonacci(n):
	if n<=1 :
		return n
	
	else :
		if memo[n] > 0 :
			return memo[n] 
		memo[n] = fibonacci(n-1) + fibonacci(n-2)
		return memo[n]
```

​    



**2. 최적 부분 구조** 

> 문제의 정답을 작은 문제의 정답으로부터 구할 수 있는가

- ex ) 최단경로 구하기 :

> **A에서 C**로 가는 최단경로 (큰 문제) = **A에서 B**로가는 최단경로(작은 문제) + **B에서 C**로가는 최단경로(작은 문제)

- 따라서, **정답을 한번 구했으면 Memoization** 하여, 반복연산을 없애는 과정이 중요하다.

 

### 다이나믹 프로그래밍 구현



#### 1. **Top - down : 위에서 아래로 해결한다. (ex : 재귀함수)**

1. **문제를 쪼갠다.**
2. **작은 문제를 푼다.**
3. **작은 문제의 정답으로 큰 문제를 해결한다.**



#### 2. **bottom - up : 아래에서 위로 (ex : 반복문)**

1. **작은 문제부터 풀어나간다.**
2. **문제의 크기를 점점 크게 만들어 푼다.**
3. **작은 문제들을 해결했기 때문에, 한단계 위의 큰 문제를 풀 수 있다.**
4. **최종적인 문제를 해결한다.**

  

**시간복잡도는 비슷한 수준이며, *문제에 따라 구현하기 편한것을 선택*하여 풀면 된다. (즉, 어떤것으로 풀어도 큰 상관은 없다) 다만 파이썬 같은경우는 재귀로 풀게되면 메모리초과가 날 가능성이 타 언어보다 높기 때문에, 반복문(bottom_up)으로 푸는게 낫다고 한다.**



### **문제를 해결할때**

- **점화식**을 정의한다.
- 문제를 어떠한식으로 쪼갤지 (작게 만들지) 생각한다.
- 작은 문제의 답을 통해 어떻게 최종적인 문제를 해결할 수 있을지 생각한다.

 

## BAEKJOON_DP 관련 문제

### 1463_1로 만들기

> [1463_1로만들기](https://www.acmicpc.net/problem/1463)문제
>
> 풀다가....결국 구글링 😂😂 찾아보니 점화식, bfs로 푼 플이들을 찾았다.

#### 1. 점화식으로 풀기

- N이라는 수는 N//3을 연산전으로 돌리면, 즉 +1을 하면 만들 수 있다.
- N이라는 수는 N//2을 연산전으로 돌리면, 즉 +1을 하면 만들 수 있다.
- N이라는 수는 N-1을 연산전으로 돌리면, 즉 +1을 하면 만들 수 있다.

따라서 !!! **점화식 : dp(N) = min ( dp(N//3) +1, dp(N//2)+1 , dp(N-1)+1 )**

```python
n = int(input())

#n+1개만큼의 0으로 이루어진 배열을 만들어줌
dp = [0 for _ in range(n+1)]

#dp라는 배열의 index는 문제의 입력nr과 대응하고, index의 값은 연산최솟값(문제의 출력)에 대응
for i in range(2, n+1):
    #1.
    dp[i] = dp[i-1] + 1  
    
    #2.
    if i%2 == 0 and dp[i] > dp[i//2] + 1 :
        dp[i] = dp[i//2]+1
        
    if i%3 == 0 and dp[i] > dp[i//3] + 1 :
        dp[i] = dp[i//3] + 1
        
print(dp[n])
```

**#1.**

dp[i] 현재 값의 배열에 들어갈 수는 현재값에서 1을 뺀 수의 배열값에 1을 더한 수

WHY??

dp배열의 현재 index에 앞으로 할 행동(1빼기)을 한 뒤의 index dp배열값에  +1(연산추가:행동을 했기 때문!)을 한 값을 넣어줌!

n에서부터 시작하는 것이 아니라 작은수부터 n으로  for문을 돌면서 연산 수를 셀것이기 때문



**#2.**

만약 2로 나누어떨어지는데 

`dp[i] > dp[i//2] + 1` 이 조건이 True라면,

dp[i] 자리에 넣을 더 작은 값을 찾았다는 뜻!

그럼 그 배열의 값을 더 작은 값으로 갱신해줌!

3으로 나눠떨어지는 것도 마찬가지!





**+ 시간복잡도**

배열의 크기 * O(1)이다. (배열 하나당 O(1)의 시간복잡도를 가지므로)

배열은 n+1이므로 **시간복잡도는 O(n)**

 

#### 2. BFS로 풀기

> [출처:poorman.tistory](https://poorman.tistory.com/421)

1. 너비우선탐색(BFS) 알고리즘을 이용하여 N 값이 1이 될때까지 탐색한다.

2. FIFO 큐를 사용하기 위해서 collections.deque를 이용하여 popleft로 값을 꺼낸 후에 새로운 노드를 append한다.

3. 노드 값은 [value, count] 형태로 사용하고 너비 우선 탐색이므로 value가 1이 되는 순간의 count를 리턴한다.

```python
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

def BFS(x):
    cnt = 0
    Q = deque([(x,cnt)])
    while(Q):
        x,cnt = Q.popleft()
        if x == 1:
            return cnt
        if x % 3 == 0:
            Q.append([x//3,cnt+1])
        if x % 2 == 0:
            Q.append([x//2,cnt+1])
        Q.append([x-1,cnt+1])
    return -1

print(BFS(N))
```

수행시간 : 2372ms



* 여기서 궁금한점!

cnt가 최소인지는...bfs라서 아는걸까....bfs는 최솟값을 구하는데 쓰기 때문에...





#### 3. DFS

> [출처:poorman.tistory](https://poorman.tistory.com/421)

1. 깊이우선탐색(DFS) 알고리즘을 이용하여 N 값이 1이 될때까지 탐색한다.

2. LIFO 스택을 사용하여 pop으로 값을 꺼낸 후에 새로운 노드를 append한다.

3. 노드 값은 [value, count] 형태로 사용하고 value 값이 1이 되는 순간의 count값으로 min_count의 최소 값을 갱신한다.

4. 최소 count 값만 구하면 되기 때문에 min_count보다는 더 깊게 탐색하지 않는다.

5. 깊이 우선 탐색이 모두 끝났을 때 min_count값을 리턴한다.

```python
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
def DFS(x):
    min_cnt = x
    cnt = 0
    Q = deque([(x,cnt)])
    while(Q):
        x,cnt = Q.pop()
        if cnt >= min_cnt:
            continue
        if x == 1:
            min_cnt = min(min_cnt, cnt)
        Q.append([x-1,cnt+1])
        if x % 2 == 0:
            Q.append([x//2,cnt+1])
        if x % 3 == 0:
            Q.append([x//3,cnt+1])
    return min_cnt

print(DFS(N))
```

수행시간 : 1272ms

*** 해당 문제는 BFS/DFS의 탐색에 시간이 많이 소요되어 비효율적이다.**



#### 4. 재귀함수

1. 재귀함수를 이용하여 현재 위치에 도달하는 최소 코스트를 리턴한다.

2. 현재 위치의 최소 코스트에 도달하기 위해서는 2,3으로 나누어 떨어지는 거리(x//2,x//3) + 나머지 거리(x%2,x%3) + 1이다. f(x) = min( f(x//3) + x%3 + 1, f(x//2) + x%2 + 1)

3. 거리가 1일때는 0, 거리가 2,3일때는 1의 코스트가 든다. f(1) = 0, f(2) = 1, f(3) = 1

```python
import sys
input = sys.stdin.readline

N = int(input())
def fnc(x):
    if x == 1:
        return 0
    elif x <= 3:
        return 1
    return min(fnc(x//3) + x%3 + 1, fnc(x//2) + x%2 + 1)
print(fnc(N))
```

수행시간 : 72ms





## Reference

[출처 : 다이나믹 프로그래밍(DP)](https://infinitt.tistory.com/246)

[출처: [poorman]]( https://poorman.tistory.com/421)