## 리스트 ##

# # 직접 데이터를 넣어 초기화
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(a)

#네번째 원소만 출력
# print(a[3])

# #크기가 n이고, 모든 값이 0인 1차원 리스트 초기화
# n = 10
# a = [0] * n
# print(a)

## 인덱싱과 슬라이싱 ##

# # 인덱스 값 바꾸기
# a[4] = 4
# print(a)

# # 여덟 번째 원소만 출력
# print(a[7])

# # 뒤에서 첫번째 원소 출력
# print(a[-1])

# # 뒤에서 세번째 원소 출력
# print(a[-3])

# # 네번째 원소 값 변경
# a[3] = 7
# print(a)

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9] 

# # 네 번째 원소만 출력
# print(a[3])

# # 두 번째 원소부터 네 번째 원소까지
# print(a[1: 4])

# ##리스트 컴프리헨션
# a = [i for i in range(50)]

# print(a)

# # 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
# ## 리스트 컴프리헨션 사용
# array = [ i for i in range(20) if i %2 ==1]
# print(array)

# ## 일반적인 코드를 사용
# array = []
# for i in range(20):
#   if i%2 ==1:
#     array.append(i)

# print(array)

# #1부터 9까지의 수들의 제곱   값을 포함하는 리스트
# array = [ i*i for i in range(1,10)]
# print(array)

# # N x M 크기의 2차원 리스트 초기화
# n = 4
# m = 3
# array = [[0]*m for _ in range(n)]
# print(array)

# array[1][1] = 5
# print(array)

# a = [1, 4, 3]
# print("기본 리스트 : ", a)

# #리스트에 원소 삽입
# a.append(2)
# print("삽입 : ", a)

# # 오름차순 정렬
# a.sort()
# print("오름차순 정렬 : ", a)

# # 내림차순 정렬
# a.sort(reverse=True)
# print("내림차순 정렬 : ", a)

# a = [4, 3, 2, 1]
# print("기본 리스트 : ", a)

# #리스트 원소 뒤집기
# a.reverse()
# print("원소 뒤집기 : ", a)

# # 특정 인덱스에 데이터 추가
# a.insert(2, 3)
# print("인덱스2에 3추가 : ", a)

# # 특정 값인 데이터 개수 세기
# print("값이 3인 데이터 개수 : ", a.count(3))

# # 특정 값 데이터 삭제
# a.remove(1)
# print("값이 1인 데이터 삭제 : ", a)

# 특정 값을 가지는 원소 모두 제거하기
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5} # 집합 자료형

#remove_set에 포함되지 않은 값만을 저장
result = [i for i in a if i not in remove_set]
print(result)