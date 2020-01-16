# 함수 정의 4
# return 결과값이 다중인 함수
'''
# 정의
def 함수명(인자1,인자2..):
    인자가 있는 명령문
    return 결과1, 결과2 ...

# 호출
함수명(인자1,인자2..)
'''

# 두개의 숫자값을 인자로 전달해서
# 합과 차를 return 한다.
def sumAndDef(n1, n2):
    return n1+n2, n1-n2

print('두수의 합과 차 ' , sumAndDef(100, 50))
print('두수의 합과 차 ' , sumAndDef(55, -20))

# 함수 정의 5
# 인자에 초기값이 있다
'''
# 정의
def 함수명(인자1=초기값1, 인자2=초기값2):
    인자가 있는 명령문
    return 결과

# 호출
함수명()
함수명(인자1,인자2..)
'''

# 하나의 인자값을 받아서 출력한다.
# 인자값이 없으면 '없다' 로 출력
def printWord(word='없다'):
    print('오늘의 키워드 --- ', word)

# 인자가 있는 경우에는 인자값으로 출력
printWord('함수')
# 인자가 없다면 초기값이 출력
printWord()

# 두개의 인자값을 받아서 더한다
# 두개 모두 인자의 초기값을 지정한 경우
def sumTwo(n1=0, n2=5):
    return n1+n2

print(sumTwo(10,20))  # 30
print(sumTwo(20)) # 25
print(sumTwo()) # 5

#
# 두개의 인자중 하나만 초기값을 지정한 경우
# 주의 사항1  : 마지막 인자 부터 초기값을 지정한다.
# 주의 사항2
# : 인자가 모두 없는 경우에는 오류 발생
# : 초기값을 지정한 외의 인자는 값을 전달해야한다.
def sumTwo2(n1, n2=0):
    return n1+n2

print(sumTwo2(10,20))  # 30
print(sumTwo2(20)) # 20
# 오류 발생
# print(sumTwo2())

# 퀴즈 :
# 세수의 곱을 출력한다.
# 출력 양식
# ? X ? X ? = 20

# def multiTest(n1=?, n2=?, n3=?):
# 명령어

# def multiTest()
# def multiTest(20)
# def multiTest(30,20)
# def multiTest(30,20,70)










