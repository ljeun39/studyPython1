### 그리디 알고리즘
# ## 거스름돈 예시
# n = 1260
# count = 0

# # 큰 단위의 화폐부터 차례대로 확인
# array = [500, 100, 50, 10]

# for coin in array:
#     count += n // coin # 해당 화폐로 거슬로 줄 수 있는 동전의 개수 세기
#     n %= coin

# print(count)

## 1이 될 때까지
# n = int(input())
# k = int(input())
# 한 줄에 공백으로 입력받기
import time
start_time = time.time() # 측정시작
n, k = map(int, input().split())
count = 0

## 내가 한 거 : 시간 약 2.237초
# while True:
#     if n % k == 0:
#         n /= k
#     elif n == 1:
#         break
#     else:
#         n -=1

#     count +=1

## 답안 1 : 시간 약 1.729초
# n이 k 이상이라면 k로 계속 나누기
# while n >= k :
#     while n % k != 0:
#         n -= 1
#         count += 1

#     n //= k
#     count += 1

# # 마지막으로 남은 수에 대하여 1씩 빼기
# while n > 1:
#     n -= 1
#     count += 1

## 답안 2 : 시간 약 1.679초
while True:
    # (n == k로 나누어 떨어지는 수)가 될 때까지 1씩 빼기
    target = (n // k) * k
    count += (n - target)
    n = target
    # n이 k보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # k로 나누기
    count += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
count += (n - 1)

print("연산 횟수 : ", count)

end_time = time.time() # 측정 종료
print("time : ", end_time - start_time)