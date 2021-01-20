#### 반복문

### while문

## 1부터 9까지 모든 정수의 합 구하기 예제(while문)
# i = 1
# result = 0

# # i가 9보다 작거나 같을 때 반복 실행
# while i <= 9:
#     result += i
#     i += 1

# print(result)

## 1부터 9까지 홀수의 합 구하기 예제(while문)

# i = 1
# result = 0

# # i가 9보다 작거나 같을 때 반복 실행
# while i <= 9:
#     if i % 2 == 1:
#         result += i
#     i += 1

# print(result)

## 무한 루프 테스트
# x = 10

# while x > 5:
#     print(x)



### for문
# array = [9, 8, 7, 6, 5] # 리스트
# array = (1, 2, 3, 4, 5) # 튜플

# for x in array:
#     print(x)

## range() 함수 사용
# result = 0

# # i는 1부터 9까지의 모든 값을 순회
# for i in range(1, 10):
#     result += i

# print(result)

## 1부터 9까지의 홀수의 합을 구할 때 (continue 키워드 사용)
# result = 0

# for i in range(1, 10):
#     if i % 2 == 0:
#         continue
#     result += i

# print(result)

# 1부터 5까지의 정수를 차례대로 출력하고자 할 때(break 키워드 사용)
# i = 1

# while True:
#     print("현재 i의 값 : ", i)
#     if i == 5 :
#         break
#     i += 1

## 학생들의 합격 여부 판단 예제
## 점수가 80점만 넘으면 합격
# scores = [90, 85, 77, 65, 97]

# # for i in range(5):
# #     if scores[i] >= 80:
# #         print(i + 1, "번 학생은 합격입니다.")

# # 특정 번호의 학생은 제외하기
# cheating_student_list = {2, 4} # 부정행위를 저지른 학생

# for i in range(5):
#     if i + 1 in cheating_student_list:
#         continue
#     if scores[i] >= 80:
#         print(i + 1, "번 학생은 합격입니다.")

## 중첩된 반복문 < 구구단 > = 이중 반복문
for i in range(2, 10):
    for j in range(1, 10):
        print(i, " x ", j, " = ", i*j)
    print()

