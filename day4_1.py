# 함수 정의 1
# 인자가 없다. return이 없다.
'''
# 함수 정의
def 함수명():
    명령문

# 호출시
함수명()

'''

# 3번 Hello world 출력하는 함수 정의
def helloWorld():
    print('Hello World')
    print('Hello World')
    print('Hello World')
    print('-'*30)

# 함수 호출
helloWorld()
helloWorld()

# 함수 정의 2
# 인자가 있다. return이 없다.
'''
# 호출
def 함수명(인자1,인자2..):
    인자가 있는 명령문
    
# 정의
함수명(인자1,인자2..)    
'''
def helloWorld2(word):
    print(word)
    print('Hello ', word)
    print('Hello ', word)
    print('Hello ', word)
    print('-'*30)

helloWorld2('Python')
helloWorld2('World')

# 두개의 값을 인자로 전달한 후
# 사칙연산과 나머지 결과값 출력
def cal(a, b):
    print(' a + b = ', a+b)
    print(' a - b = ', a-b)
    print(' a * b = ', a*b)
    print(' a / b = ', a/b)
    print(' a % b = ', a%b)
    print('-'*30)

cal(10, 3)
cal(100, 20)

# 퀴즈 :
# 위에서 정의한 cal() 함수의 결과값을
# 아래와 같이 출력되도록 한다.
# '%d 나 %.소숫점f'% (변수1, 변수2) 이용한다
# 결과 =>
# 10 + 3 =  13
# 10 - 3 =  7
# 10 * 3 =  30
# 10 / 3 =  3.33
# 10 % 3 =  1

def cal2(a, b):
    print(' %d + %d = %d '%(a,b,a+b))
    print(' %d - %d = %d '%(a,b,a-b))
    print(' %d * %d = %d '%(a,b,a*b))
    print(' %d / %d = %.2f'%(a,b,a/b))
    # %% 는 2번 입력
    print(' %d %% %d = %d '%(a,b,a%b))
    print('-'*30)

cal2(10, 3)
cal2(33, 5)

# 함수 정의 3
# 인자가 있다. return이 있다.
'''
# 호출
def 함수명(인자1,인자2..):
    인자가 있는 명령문
    return 변수/수식 

# 정의
함수명(인자1,인자2..)    
'''

def helloWorld3(word):
    # return 아래의 명령은 실행되지 않는다.
    # return
    print('-'*30)
    return print('Hello  '+word)

helloWorld3('Java')
helloWorld3('C')
helloWorld3('Python')

# 3수의 합을 return 하여라
def sumThree(n1, n2, n3):
    return n1+n2+n3

print('3수의 합 = ', sumThree(23,55,100))

print('-'*30, '\n\n')
# 1~100 까지의 합 구하기
resultSum = 0
for i in range(1,101):
    resultSum += i
print(resultSum)

print('-'*30, '\n\n')

# 1~ n 까지의 합 구하기 함수 정의
def sumN(n):
    resultSum2 = 0
    for i in range(1, n+1):
        resultSum2 += i
    return resultSum2

print('1 부터 {} 까지의 합 : {}'.format(50,sumN(50)))
print('1 부터 {} 까지의 합 : {}'.format(100,sumN(100)))

# 퀴즈 : 별찍기
# 함수로 정의한 후 호출하여라.
# for i in range(1,6):
#     print('* '*i)

'''
starPrint(5) 

결과 :
*
**
***
****
*****

starPrint(3) 

결과 :
*
**
***
'''
# 함수 사용전
for i in range(1,6):
    print('* '*i)

# 함수 정의
def starPrint(n):
    print('-'*30)
    for i in range(1, n+1):
        print('* ' * i)

starPrint(10)
starPrint(5)


# 퀴즈 :
# 리스트 각각 아이템을 출력하는 함수를 정의하여라
#
# 함수를 사용하지 않은 경우
# for 인덱스변수 in 리스트/튜플/집합/문자열:
#   print(인덱스변수)

# 함수 사용전
cnt = 0
for i in ['초밥', '햄버거', '스테이크', '떡국']:
    print(cnt, ' : ', i)
    cnt += 1

#
# 결과 =>
# printList(['초밥', '햄버거', '스테이크', '떡국'])
# 0  :  초밥
# 1  :  햄버거
# 2  :  스테이크
# 3  :  떡국

# 함수 정의
def printList(food):
    print('\n\n   Result   ')
    cnt = 1
    for i in food:
        print(cnt, ' : ', i)
        cnt += 1

# 함수 호출
printList(['라면', '빙수'])
printList(['모밀', '탕수육', '육계장'])









