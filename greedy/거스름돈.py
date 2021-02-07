# 거스름돈

n = 1260
count = 0

coin_type = [500, 100, 50, 10]

for coin in coin_type:
    n %= coin
    count += n

print(count)