# 함수의 종류
# 사용자정의 함수
# - def 명령으로 함수명 정의
# - lambda 함수 : 익명함수
# 외장함수 : import 외장모듈이나 패키지
# 내장함수 : import 명령없이 사용할 수 있는 함수
# abs(), max(), min(), divmod()
# eval()
# enumerate(), map()

# sorted(리스트/튜플/집합..)
# : 데이타 정렬
# : 결과값을 리턴한다. => print()로 바로 출력
# 리스트이름.sort() : 리스트정렬
# 리스트이름.reverse() : 리스트 역정렬
myList= ['b', 'a','c','x']
print(myList.sort()) # None
myList.sort()
print(myList) # ['a', 'b', 'c', 'x']
myList.reverse()
print(myList) # ['x', 'c', 'b', 'a']

# 바로 출력 가능
print(sorted(['b', 'a','c','x'])) # ['a', 'b', 'c', 'x']

# 유효성 검사?
# 데이터(숫자, 문자...)가 조건에 맞는지 검사하는 기능
# 문자열변수.isalpha() : 모두 문자인가? 숫자문자제외 , True/Fasle
# 문자열변수.isdigit() : 모두 숫자문자인가?  , True/Fasle
str1 = 'fkfkfk'
str2 = '12345'
str3 = '1fdkjfsl2345'
print(str1.isalpha()) # True
print(str2.isalpha()) # False
print(str3.isdigit()) # False
print(str1.isdigit()) # False
print(str2.isdigit()) # True

# 퀴즈
# 빈 리스트를 생성한다.
# 입력문이 실행된다.
# 입력값이 숫자이면 리스트에 추가한다.
# 입력값이 숫자가 아니면 다시 입력문이 실행된다.
# 리스트의 전체길이가 5이면 입력을 종료한다.
# 리스트를 출력한다.

# resultList = []
# print(resultList, type(resultList)) # [] <class 'list'>
# # 입력값을 받을 수 있게 while 문 생성
# while True:
#     data = input('데이타를 입력해주세요?....')
#     # # 입력 데이타를 리스트에 추가한다.
#     # resultList.append(data)
#     # 숫자이면 리스트 추가
#     if data.isdigit():
#         resultList.append(data)
#         print('리스트가 추가되었습니다.')
#     else:
#         print('숫자가 아닙니다. 다시 입력해주세요 ')
#     # 탈출 조건
#     if len(resultList) == 5:
#         break
# # 리스트 출력
# print(resultList)

# 퀴즈 : 문자열에서 숫자와 숫자가아닌문자의 갯수를 출력하여라
# testWord = 'Python1234Java4774'
'''
결과 >>
숫자 갯수 : ? 
문자 갯수 : ?
'''
# 문자열변수 정의
# 숫자갯수를 저장할 변수 정의 : cnt
# 반복문 생성 : 문자열에서 숫자라면 : cnt += 1 값을 증가시킨다.
# 숫자갯수 출력
# 문자갯수는? len(문자열변수)-cnt

testWord = 'Python1234Java4774'
cnt = 0
for i in testWord:
    if i.isdigit():
        cnt += 1
print( '숫자갯수 : ', cnt)
print( '문자갯수 : ', len(testWord)-cnt)

# zip(리스트1, 리스트2 .. )
# : 리스트의 각 아이템요소를 튜플화 구조로 묶어준다.
# : [(아이템1,아이템2) ...]
# zip(*zip객체)
# : zip으로 묶어준 객체를 원래대로 풀어준다.
p1 = ['길동', '동미', '미영', '영철']
p1Gender= ['남','여','여','남']
# zip 객체로 출력
print(zip(p1, p1Gender))
# 하나씩 출력
for i in zip(p1, p1Gender):
    print(i)

# 각각 구분자로 분리해서 출력
for i, j in zip(p1, p1Gender):
    print(i, '-', j)
# 리스트화
print(list(zip(p1, p1Gender)))

# zip으로 리스트안의 튜플구조 해제하기 - unzip
# 변수1, 변수2 = zip(*리스트튜플이름)
# 결과물은 같은 인덱스의 값만 튜플로 다시 생성
myList2 = [('a','apple'),('b','banana'),('c','cat')]
print(myList2, type(myList2))
x,y = zip(*myList2)
print(x) # ('a', 'b', 'c')
print(y) # ('apple', 'banana', 'cat')

# filter()
# filter(함수명, 리스트) => 참인조건의 리스트만 출력
# 사용할 함수는 결과값이 True/False

# 양수인지 판독하는 함수 정의
def positive(x):
    return x>0
print(positive(-10)) # False
print(positive(10)) #True

numlist = [10, -30, 20, 5, -100]
# 객체 출력 : <filter object at 0x01DAFB30>
print(filter(positive, numlist))
# 리스트화 : 양수만 추출
print(list(filter(positive, numlist)))
# for .. in 으로 출력
for i in filter(positive, numlist):
    print(i)

# 리스트 중 짝수만 출력하기 = filter() 함수 이용
# 짝수인지 판독하는 함수 정의
# 리스트 정의
# filter() 함수 적용 => filter 객체
# filter 객체를 리스트화

print('-'*30)
def evenJudge(x):
    return x % 2 == 0
numList2 = [12, 5, 30, 44, 33]
print(list(filter(evenJudge, numList2)))
for i in filter(evenJudge, numList2):
    print(i)










