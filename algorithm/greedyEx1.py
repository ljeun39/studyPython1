###
   # 각 자리가 숫자(0부터 9)로만 이루어진 문자열 S가 주어졌을때, 
   # 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 'X' 혹은 '+' 연산자를 넣어
   # 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램
   # 단, + 보다 X를 먼저 계산하는 일반적인 방식과 달리, 모든 연산은 왼쪽에서부터 순서대로 이루어진다.

   # 입력 조건
     # 첫째 줄에 여러 개의 숫자로 구성된 하나의 문자열 S가 주어짐 (1 <= S <= 20)
  # 출력 조건
    # 만들어질 수 있는 가장 큰 수 출력.
###

# 문자열 S 
# 엉망진창 와진창 이상한 코드.. 
# s = (input())
# result = 0

# for i in range(0,len(s)-1):
#   if int(s[i]) == 0 || int(s[i]) == 1:
#     result = int(s[i]) + int(s[i+1])
#   elif int(s[i]) != 0:
#     result = int(s[i]) * int(s[i+1])
#     print(result)

# print(result)

## 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다 더하기를 수행하는 것이 효율적
# 따라서 두 수에 대하여 연산을 수행할 때, 두 수 중에서 하나라도 1 이하인 경우에는 더하며, 두 수가 모두 2이상인 경우에는 곱하면 정답.

# 답안 예시
data = input()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):
    # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)