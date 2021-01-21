#### 함수

## 더하기 함수
# def add(a, b): # a, b 는 매개변수
#     return a + b # a + b 는 반환값

# print(add(3, 7)) # 함수 호출 시 넣는 값 : argument 혹은 인자

## 더하기 함수 2
# def add(a, b):
#     print('함수의 결과 : ', a + b)

# add(3, 7)

## 빼기 함수
# def subtract(a, b):
#   return a - b

# result = add(3, 7)
# print(result)

# result = subtract(3, 7)
# print(result)

### global 키워드
# a = 0

# def func():
#     global a
#     a += 1

# for i in range(10):
#     func()

# print(a)

# a = 10

# def func():
#     print(a + 20)

# func()

# 전역변수
# array = [1, 2, 3, 4, 5]

# def func():
#     # 지역변수 선언 시 지역변수가 우선시 됨
#     # 전역변수 값을 가져와서 변경하려면 global 키워드를 이용 후 변경해야함.
#     global array
#     array = [3, 4, 5]
#     array.append(6)
#     print(array)

# func()
# print(array)

### 여러 개의 반환값
def operator(a, b):
  add_var = a + b
  subtract_var = a - b
  multiply_var = a * b
  divide_var = a / b
  return add_var, subtract_var, multiply_var, divide_var

a, b, c, d = operator(7, 3)
print(a, b, c, d)