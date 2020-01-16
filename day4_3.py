# 함수 정의 6
# 가변인자를 이용한 함수 정의
# 인자가 정해지지 않은 함수
# 결과값은 튜플
'''
# 정의
def 함수명(*args):
    인자 args 있는 명령문
    return 결과

# 호출
함수명(인자)
함수명(인자1,인자2..)
함수명(인자1,인자2,인자3)
'''

# 가변인자를 받아서 출력한다.
def printM(*args):
    print(args)
    print(type(args))
    # 한개씩 출력
    for i in args:
        print(i)

printM(100)
printM('함수', '제어문', '클래스')

# 가변인자를 이용해서 n개의 합 구하기
def sumArgs(*args):
    result = 0
    for i in args:
        result += i
    return result

print(sumArgs(10, 20, 30))
print(sumArgs(10, 20))
print(sumArgs(10, 20, 100, 300, -20))

# 함수 정의 7
# 인자와 가변인자가 함께 정의된 경우
# 가변인자가 마지막에 정의되어야 한다.
'''
# 정의
def 함수명(인자, *args):
    인자가 있는 명령문 
    인자 args 있는 명령문
    return 결과

# 호출
함수명(인자, 가변인자)
함수명(인자, 가변인자1, 가변인자2 ...)
'''

def printTest( symbol, *args) :
    print('인자 = ' , symbol)
    print('가변인자 = ', args)
    print('-'*30)

printTest( '*', 10)
printTest( '-', 10, '가나다')
printTest( '+', '파이썬', '자바', '자바스크립트')

# 퀴즈
# 다음 함수를 호출하면 계산 결과가 출력되도록
# 가변인자와 인자를 정의하여라

# def calChoice(계산기호인자, *args) :
#     if 계산기호인자 == *:
#           명령문1
#     elif 계산기호인자 == +:
#           명령문2
#     else:
#           명령문3

# calChoice('*', 20,30)
# 계산결과 : 곱 : 600
# calChoice('+', 20,30,50)
# 계산결과 : 합 : 100
















