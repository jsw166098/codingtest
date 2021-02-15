# 큰 수의 법칙

## 단순 풀이

# N, M, K를 공백으로 구분하여 입력받기
n,m,k = map(int, input().split())

# N 개의 수를 공백으로 구분하여 입력 받기
data = list(map(int, input().split()))

# 입력 받은 수들 정렬
data.sort()
first = data[n-1]
second = data[n-2]

result = 0

while True:
    # 가장 큰 수를 K 번 더한다.
    for i in range(k):
        if m == 0:  # m이 0이라면 반복문 탈출
            break
        result += first
        m -= 1  # 더할 때 마다 1씩 빼기
    if m == 0:  # m이 0이라면 반복문 탈출
        break
    result += second  # 두 번째로 큰 수를 한 번 더하기
    m -= 1  # 더할 때마다 1씩 빼기

print(result)  # 최종 답안 출력

## 수학적 아이디어 사용

# N, M, K를 공백으로 구분하여 입력받기
n,m,k = map(int, input().split())

# N 개의 수를 공백으로 구분하여 입력 받기
data = list(map(int, input().split()))

data.sort()  # 입력받은 수 정렬
first = data[n-1]  # 가장 큰 수
second = data[n-2]  # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(m/(k+1))*k
count += m%(k+1)

result = 0
result += (count)*first  # 가장 큰 수 더하기
result += (m-count)*second  # 두 번째로 큰 수 더하기

print(result)