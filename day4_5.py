# 내장함수
# 수학관련 함수
# 절대값 출력 : abs(숫자)
print('-1 =>', abs(-1))
print('10 =>', abs(10))

# 리스트의 최대값과 최소값 출력하기
# max(리스트/튜플/집합...)
# min(리스트/튜플/집합...)
print('[20, 40, 56, 100]' )
print('최대값 =>', max([20, 40, 56, 100]))
print('최소값 =>', min([20, 40, 56, 100]))

print('(20, 40, 56, 100)' )
print('최대값 =>', max((20, 40, 56, 100)))
print('최소값 =>', min((20, 40, 56, 100)))

# 나누기 연산자 /, //
# 나머지 연산자 %
# divmod(n1,n2) => 몫과 나머지 값을 구한다. => 튜플
print(10/3.2) # 3.125
print(10//3.2) # 3.0
result = divmod(100,20)
print(result, type(result) ) # (5, 0) <class 'tuple'>
# 튜플 인덱싱
print(result[0])
print(result[1])
# 값 1개씩 출력
for i in result:
    print(i)

# 5개의 값을 입력문을 이용하여 리스트로 저장한 후
# 최대값과 최소값을 출력한다.
# 빈 리스트 생성

# result = []
# for i in range(0,5):
#     # 정수 데이터로 변환
#     data = int(input('숫자를 입력해주세요 ... '))
#     result.append(data)
# print('전체 리스트 => ', result)
# print('최대 값 => ', max(result) )
# print('최소 값 => ', min(result) )

# eval(문자열계산식)
# 입력받은 수식을 계산하여라
# result = input('수식을 입력하세요? ... ')
# print(result, ' = ', eval(result))

# enumerate(리스트/튜플/문자열 , 인덱스숫자 )
# 인덱스숫자로 구성된 리스트/튜플/문자열
# => enumerate 객체 생성
# => for .. in 하나씩아이템 출력 가능
# => 각각 튜플아이템으로 생성 (인덱스, 값)
listA = ['a','b','c']
enumResult = enumerate(listA, 5)
print(enumResult, type(enumResult))
for i in enumResult:
    print(i) # (인덱스번호, 값)

# 한개씩 출력하기
for i, v in enumerate(listA, 5):
    print(i, ' => ', v)

# 문자열 변환
for i, v in enumerate('abcd', 1):
    print(i, ' => ', v)

# map() 함수

# 제곱을 구하는 함수 정의
def doubleMulti(x):
    return x**2

print(doubleMulti(3)) # 9
print(doubleMulti(-10)) # -10
print(doubleMulti(5)) # 25
print(doubleMulti(7)) # 49

# map() 사용
mapResult = map(doubleMulti, [3,-10,5,7])
print(mapResult, type(mapResult))
# <map object at 0x00A4FA10> <class 'map'>

# 한개씩 값 출력하기
for i in map(doubleMulti, [3,-10,5,7]):
    print(i, end=' ')

print('\n\n')
# 리스트화
print(list(map(doubleMulti, [3,-10,5,7])))




