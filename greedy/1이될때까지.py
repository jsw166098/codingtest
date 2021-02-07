# 1이 될 때까지

# 1. 내 풀이
N, K = map(int, input().split())

result = N
count = 0

while True:
    if result % K == 0:
        result //= K
        count += 1
    else:
        result -= 1
        count += 1

    if result == 1:
        break

# if result % K == 0:
#     result = result // K
#     count += 1

print(count)

# 2. 단순 풀이
n, k = map(int, input().split())
result = 0

# N이 K이상이면 K로 계속 나누기
while n >= k:
    # N이 K로 나누어 떨어지지 않는다면 N에서 1씩 빼기
    while n % k != 0:
        n -= 1
        result += 1
    # K로 나누기
    n //= k
    result += 1

# 마지막으로 남은 수에 대하여 1씩 빼기
while n>1:
    n -= 1
    result += 1

print(result)

# 3. 수학적 아이디어 적용
n, k = map(int, input().split())
result = 0

while True:
    # (N==K로 나누어떨어지는 수)가 될 때까지 1씩 빼기
    target = (n//k)*k
    result += (n-target)
    n = target

    # N이 K 보다 작을 때(더 이상 나눌 수 없을 때 ) 반복문 탈출
    if n < k:
        break

    # K로 나누기
    result += 1
    n //k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n-1)
print(result)
