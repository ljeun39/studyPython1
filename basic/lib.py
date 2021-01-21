### 자주 사용되는 표준 라이브러리

# ## 자주 사용되는 내장 함수
# # sum()
# result = sum([1, 2, 3, 4, 5])
# print(result)

# # min(), max()
# min_result = min(7, 3, 5, 2)
# max_result = max(7, 3, 5, 2)
# print(min_result, max_result)

# # eval() : 수식으로 표현된 식을 계산한 결과를 반환해주는 함수
# result = eval("(3+5)*7")
# print(result)

# # sorted()
# result = sorted([9, 1, 8, 5, 4]) # 오름차순
# reverse_result = sorted([9, 1, 8, 5, 4], reverse = True) # 내림차순
# print(result)
# print(reverse_result)

# # sorted() with key
# array = [('홍길동', 35), ('이순신', 75), ('아무개', 50)]
# result = sorted(array, key = lambda x: x[1], reverse = True)
# print(result)

## 순열과 조합
# # 순열
# from itertools import permutations

# data = ['A', 'B', 'C'] # 데이터 준비

# result = list(permutations(data, 3)) # 모든 순열 구하기
# print(result)

# # 조합
# from itertools import combinations

# data = ['A', 'B', 'C'] # 데이터 준비

# result = list(combinations(data, 2)) # 2개를 뽑는 모든 조합 구하기
# print(result)

# # 중복 순열
# from itertools import product

# data = ['A', 'B', 'C'] # 데이터 준비

# result = list(product(data, repeat=2)) # 2개를 뽑는 모든 순열 구하기 (중복 허용)
# print(result)

# # 중복 조합
# from itertools import combinations_with_replacement

# data = ['A', 'B', 'C'] # 데이터 준비

# result = list(combinations_with_replacement(data, 2)) # 2개를 뽑는 모든 조합 구하기 (중복 허용)
# print(result)

## 최대 공약수와 최소 공배수
import math

def lcm(a, b):
    return a * b // math.gcd(a, b) 

a = 21
b = 14

print(math.gcd(a, b))
print(lcm(a, b))