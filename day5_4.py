# 클래스 : 특별한 자료구조
# 관련 키워드 => OOP, 인스턴스=객체
# 기본자료형(숫자, 문자열, 불른)
# 콜렉션형 (리스트, 집합, 튜플, 딕셔너리)
# 클래스 ( 속성, 함수 ...) => 틀
# 인스턴스=객체=Object
#   => 클래스에 의해서 만들어진 산출물

# 클래스 생성 문법
# 클래스이름은 첫글자는 대문자로 지정
# class 클래스이름:
#   명령문

# 빈 클래스 생성하기
class Test:
    pass

# <class '__main__.Test'> <class 'type'>
print(Test, type(Test))

# 인스턴스 생성하기
# 인스턴스명은 첫글자는 소문자로 지정
# 인스턴스변수 = 클래스이름()
# isinstance(인스턴스변수, 클래스이름)
# 특정클래스에 의해서 생성된 인스턴스가 맞는지 출력
# True / False 로 출력
testObj1 = Test()
testList = []
# <__main__.Test object at 0x02C7BE90> <class '__main__.Test'>
print(testObj1, type(testObj1))
print(isinstance(testObj1, Test)) # True
print(isinstance(testList, Test)) # False

# 생성자 함수 (Constructor)
# => 속성값 정의
# 사각형에 관련된 클래스 속성 => 가로, 세로, 색상
# 사람에 대한 클래스 속성 => 이름, 성별, 키, 몸무게
# 붕어빵에 대한 클래스 속성 => 재료, 생산시간

# 생성자함수 문법
# class 클래스명:
#   def __init__(self, 인자):
#       self.인자 = 인자값
# 인스턴스 생성
# 인스턴스명 = 클래스이름(인자값,..)
# 실제 속성값 출력
# 인스턴스명.속성

# 사각형 도형의 클래스와 생성자 함수 정의
class Square:
    # 속성을 정의하는 생성자 함수
    def __init__(self, width, height):
        self.width = width
        self.height = height

# 인스턴스화
squareObj1 = Square(100,100);
squareObj2 = Square(40,80);

# 실제 속성값 출력
# 인스턴스명.속성
print('squareObj1 => ',\
      squareObj1.width, squareObj1.height)
print('squareObj2 => ',\
      squareObj2.width, squareObj2.height)

print('squareObj2 => 면적 ', squareObj2.width*squareObj2.height)

# Car 클래스 생성하기
# 클래스 메소드란?
# def 메소드이름(self,인자):
#   명령어
#   return 값
# 메소드 호출
# 인스턴스명.메소드이름(인자)

class Car:
    # 생성자함수 - 속성 정의
    def __init__(self, brand, name, color, year):
        self.brand = brand
        self.name = name
        self.color = color
        self.year = year
    # 메소드 정의
    def play(self, name):
        print(name , '자동차가 달린다.')
    def stop(self, name):
        print(name, '자동차가 멈춘다')


# 인스턴스 생성 후 속성 값 할당
car1 = Car('현대','스타렉스','회색','2010')
car2 = Car('기아','레이','검정','2017')
# 속성 출력
print('car1: %s, %s, %s, %s'% \
      (car1.brand, car1.name, car1.color, car1.year))
print('car2: %s, %s, %s, %s'% \
      (car2.brand, car2.name, car2.color, car2.year))
# 메소드 호출
car1.play('car1')
car2.stop('car2')

# 사각형 속성(가로, 세로),
# 속성 출력 메소드,
# 면적을 출력하는 메소드 정의

class Square2:
    # 속성을 정의하는 생성자 함수
    def __init__(self, width, height):
        self.width = width
        self.height = height
    # 속성을 출력하는 메소드 정의
    def info(self, width, height):
        print('가로 크기 - ', width)
        print('세로 크기 - ', height)
    # 면적을 출력하는 메소드 정의
    def area(self, width, height):
        print('사각형 면적 - ', width*height)

# 인스턴스화
squareA = Square2(50, 40)
squareB = Square2(70, 70)
print('-'*10,'\n')
squareA.info(50,40)
squareA.area(50,40)

'''
퀴즈 : 
    1. 타원 클래스 생성 
    2. 속성 : ?
    3. 속성을 출력하는 메소드 정의
    4. 타원의 면적을 출력하는 메소드 정의 : 3.14*반지름**2 
    5. 인스턴화 
    6. 속성과 면적 메소드 호출 
'''
class Circle:
    def __init__(self, objName, radius):
        self.objName = objName
        self.radius = radius
    def info(self,objName, radius):
        print('\n\n','-'*20)
        print('원의 이름 : ', objName)
        print('원의 반지름 : ',radius)
    def area(self,radius):
        print('원의 면적 : ',3.14*radius**2)

c1 = Circle('c1', 5)
c1.info('c1', 5)
c1.area(5)

c2 = Circle('c2',15)
c2.info('c2',15)
c2.area(15)

# 상속이란?
# 부모클래스의 속성이랑 메소드를 그대로 가진다.
# class 클래스이름(부모클래스1,부모클래스2...)

# 부모클래스1 - 아파트, 차
# 부모클래스2 - 오피스텔, 전동스쿠터
# 자식클래스 - 아파트, 차 , 오피스텔, 전동스쿠터

# 부모 클래스 정의
class Papa:
    def __init__(self):
        pass
    def info1(self):
        return '아파트, 차'

class Mama:
    def __init__(self):
        pass
    def info2(self):
        return '오피스텔, 전동스쿠터'

# 자식 클래스 정의
class Me(Papa, Mama):
    pass

# 자식 클래스의 객체화
m = Me()
print('상속 => ', m.info1(), m.info2())

# 퀴즈 : 계산기 만들기
# 2개의 숫자를 속성으로 가진 계산기 클래스 만들기
# 인스턴스화 시킨 후 다음과 같이 출력한다
#
# [ 출력형태 : ]
# 첫번째 숫자 : ?
# 두번째 숫자 : ?
# 더하기 : ?
# 빼기 : ?
# 곱하기 : ?
# 나누기 : ?

# 클래스 선언 -  Calculator
# 생성자함수를 이용하여 속성 정의
# 더하기 메소드 정의
# 빼기 메소드 정의
# 곱하기 메소드 정의
# 나누기 메소드 정의
# 클래스를 이용하여 인스턴스 생성
# 출력형태로 메소드 호출하여 출력


class Calculator:
    def __init__(self,n1,n2):
        self.n1 = n1
        self.n2 = n2
    def info(self,n1,n2):
        print('첫번째 숫자 : ', n1)
        print('두번째 숫자 : ', n2)
    def c_method1(self,n1,n2):
        print('더하기 : ', n1+n2)
    def c_method2(self,n1,n2):
        print('빼기 : ', n1-n2)
    def c_method3(self,n1,n2):
        print('곱하기 : ', n1*n2)
    def c_method4(self,n1,n2):
        print('나누기 : ', n1//n2)

print('-'*10, '\n 인스턴스화 결과 \n')
cObj= Calculator(10,20)
cObj.info(10,20)
cObj.c_method1(10,20)
cObj.c_method2(10,20)
cObj.c_method3(10,20)
cObj.c_method4(10,20)




