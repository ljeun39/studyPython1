### 입력을 위한 전형적인 소스코드 1)

# 데이터의 개수 입력
# n = int(input())

# print(n)

# 각 데이터를 공백을 기준으로 구분하여 입력
# data = input()
# data = input().split()
# 입력한 데이터를 정수형으로 바꾸어 리스트 저장
# data = list(map(int, input().split())) 

# print(data)

# a, b, c를 공백을 기준으로 구분하여 입력
# 들어오는 입력의 갯수가 정해져있을 때
# a, b, c = map(int, input().split())

# print(a, b, c)

### 빠르게 입력 받기
import sys

# 문자열 입력 받기
data = sys.stdin.readline().rstrip()
print(data)