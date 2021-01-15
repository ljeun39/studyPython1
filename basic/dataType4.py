### 사전 자료형, 집합 자료형

# ## 사전 자료형
# data = dict()
# data['사과'] = 'Apple'
# data['바나나'] = 'Banana'
# data['코코넛'] = 'Coconut'

# print(data)

# if '사과' in data:
#   print("'사과'를 키로 가지는 데이터가 존재합니다.")

# # 키 데이터만 담은 리스트
# key_list = data.keys()
# print(key_list)

# # 값 데이터만 담은 리스트
# value_list = data.values()
# print(value_list)

# # 각 키에 따른 값을 하나씩 출력
# for key in key_list:
#   print(data[key])

# # 사전 자료형 중괄호 초기화
# a = {
#   '국어' : 96,
#   '수학' : 90
# }
# print(a)

# # 키 데이터를 리스트로 형변환
# a_keys = list(a.keys())
# print(a_keys)

# # 특정 키의 값 출력
# print(a['국어'])

## 집합 자료형 

# # 초기화 방법 1
# data = set([1, 1, 2, 3, 4, 4, 5])
# print(data)

# # 초기화 방법 2
# data = {1, 1, 2, 3, 4, 4, 5}
# print(data)

# -> 중복된 값은 출력되지 않음

# # 집합 자료형의 연산
# a = set([1, 2, 3, 4, 5])
# b = set([3, 4, 5, 6, 7])

# # 합집합
# print(a|b)

# # 교집합
# print(a&b)

# # 차집합
# print(a-b)

# 집합 자료형 관련 함수
data = set([1, 2, 3])
print(data)

# 새로운 원소 추가
data.add(4)
print(data)

# 새로운 원소 여러 개 추가
data.update([5, 6])
print(data)

# 특정한 값을 갖는 원소 삭제
data.remove(3)
print(data)