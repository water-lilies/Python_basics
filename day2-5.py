# 제어문의 종류
# 조건문
# 반복문
# {} 사용하지 않고 탭1개 나 공백4칸 으로 블록 지정
# switch 문이 없다
# elif 문이 있다

# 단순 조건문
# if 조건식:
#     수행명령

a = 10
b = 20
print( a>b ) # False
print( a<=b ) # True

if a<=b :
# if a > b :
# IndentationError: 에러 발생
# print('a 가 b 보다 작다')
    print('a 가 b 보다 작다')

# 짝수인지 홀수인지 판단 ?
myNum = 45
if myNum%2 == 0:
    print('짝수')
if myNum%2 != 0:
    print('홀수')

# 퀴즈1 :
# 숫자를 입력받아서
# 숫자값이 3의 배수이면 3의 배수이다.
# 그렇지 않으면 3의 배수가 아니다.
'''
숫자를 입력해주세요 ? ... 
3의 배수이다. 
3의 배수가 아니다.
'''

# 퀴즈2 :
# 나이를 입력받아서
# 나이에 따라서 서로다른 메세지 출력
'''
당신의 나이를 입력해주세요? ...  
14 ~ 16 : 중학생 
17 ~ 19 : 고등학생 
20 ~ : 성인
'''
userAge = int(input('당신의 나이를 입력해주세요 ? ... '))
if userAge>19 :
    print('성인')

if 17 <= userAge <= 19 :
# if (userAge >= 17) and (userAge <= 19) :
    print('고등학생')

if 14 <= userAge <= 16 :
    print('중학생')