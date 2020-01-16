# 스코프(Scope) ?
# 변수의 범위
#   - 함수안의 정의된 변수와 함수밖의 변수 범위
# 전역변수 : 파일 전체에서 사용되는 변수
# 지역변수 : 함수내에서 사용되는 변수
# global 변수 : 함수안에서 전역변수를 사용할 때 사용

# 전역변수 정의
v = 10
print( '테스트1 : v 값은?', v) # 10
# 함수내의 같은 변수값 테스트
def testScope():
    # 지역 변수
    v = 20
    print( '함수내의 v 값은?', v)

# 함수 호출
testScope() # 20

print('테스트2 : v 값은?', v) # 10

print('-'*20)

# 전역변수 정의
v1 = 10
print( '테스트1 : v1 값은?', v1) # 10
# 함수내의 같은 변수값 테스트
def testScope2():
    # 전역 변수 정의
    # global 변수명
    global v1

    print( '함수내의 v 값은?', v1) # 10

    # 전역 변수에 값 할당
    v1 = 20
    print( '함수내의 v 값은?', v1) # 20

# 함수 호출
testScope2() # 20

print('테스트2 : v1 값은?', v1) # 20

# 람다함수 정의
# lambda 함수 = 익명함수
# define 정의문이 없다.
# 한줄로 코딩한다.
# 축약형 함수
# lambda 함수로 정의
# 함수변수 = lambda 인자:명령문
# lambda 함수 호출
# 함수변수(인자)

# 인자를 출력하는 lambda 함수 정의
f1 = lambda x:x+x
# lambda 함수 호출
print(f1(10)) # 20
print(f1('Python / ')) # Python / Python /

# 세수의 합을 구하는 lambda 함수 정의
f2 = lambda x,y,z:x+y+z
# lambda 함수 호출
print(f2(10,20,40))
print(f2('알라딘 ', '로미오와 줄리엣 ', '기생충 '))






