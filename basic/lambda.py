#### 람다 표현식

# # 일반 함수
# def add(a, b):
#     return a + b
# print(add(3, 7))

# # 람다 표현식으로 구현한 add() 메서드
# print((lambda a, b: a + b)(3, 7))

# ## 내장 함수에서 자주 사용되는 람다 함수
# array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]

# def my_key(x):
#     return x[1]

# print(sorted(array, key = my_key))
# print(sorted(array, key = lambda x: x[1]))

## 여러 개의 리스트에 적용
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

# map 함수 : 각각의 원소에 함수를 적용하고자 할 때 사용
result = map(lambda a, b: a + b, list1, list2)

print(list(result))