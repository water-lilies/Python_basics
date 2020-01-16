# 제어문의 종류
# 조건문
# 반복문
# {} 사용하지 않고 탭1개 나 공백4칸으로 블록 지정
# switch 문이 없다
# elif 문이 있다

# 단순 조건문 - 참이면 실행
# if 조건식
#   수행명령

a = 10
b = 20
print ( a>b )
print ( a<=b )

if a <= b :
    print('a 가 b 보다 작다')        # 들여쓰기를 안하면 indentationError 발생

# 짝수인지 홀수인지 판단
myNum = 100
if myNum%2 == 0:
    print('짝수')

if myNum % 2 != 0:
    print('홀수')


# 퀴즈 1
# 숫자를 입력해서 숫자값이 3의 배수이면 3의배수이다.
# 그렇지 않으면 3의 배수가 아니다.
'''
숫자를 입력해주세요 ? ... 
3의 배수이다. 
3의 배수가 아니다.
'''

myNum2 = int(input('숫자를 입력하세요.'))
if myNum2 % 3 == 0:
    print('3의 배수 입니다.')

if myNum2 % 3 != 0:
    print('3의 배수가 아닙니다.')

# 퀴즈 2
# 나이를 입력받아서 나이에 따라 서로 다른 메세지 출력

# if 17 <= userAge <= 19            --> 파이썬에서는 다른 언어와 달리 이런 수식이 가능!
# if(userAge>=17) and (userAge<=19)

'''
당신의 나이를 입력해주세요? ...  
14 ~ 16 : 중학생 
17 ~ 19 : 고등학생 
20 ~ : 성인
'''

userAge = int(input('당신의 나이를 입력해주세요?...'))
if userAge >= 20:
    print('성인입니다.')
elif userAge >= 17:
    print('고등학생입니다.')
elif userAge >= 14:
    print('중학생입니다.')

