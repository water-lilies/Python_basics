#  in / not in 연산자
# 아이템 in 그룹(튜플, 리스트, 문자열) => True / False
# 아이템 not in 그룹(튜플, 리스트, 문자열) => True / False

groupA = [10, 20, 30]
groupB = (10, 20, 30)
groupC = 'abcdef'
groupD = set(['사과', '포도', '수박'] )

print( groupA, type(groupA))
print( groupB, type(groupB))
print( groupC, type(groupC))
print( groupD, type(groupD))

print(10 in groupA)
print(0 in groupB)
print('a' in groupC)
print('사과' in groupD)
print(10 not in groupA)
print(0 not in groupB)
print('a' not in groupC)
print('사과' not in groupD)

# if ... in
# if 아이템요소 in 그룹(문자열,튜플,집합,리스트):
#     명령문1
# elif 아이템요소 in 그룹(문자열,튜플,집합,리스트):
#    명령문2
# else:
#   명령문

t1 = ('바나나', '포도', '수박', '자두')
if '체리' in t1:
    print('바나나가 우리집 냉장고에 있다')
elif '포도' in t1:
    print('포도가 많이 우리집 냉장고에 있다')
else:
    print('냉장고에 과일이 없다')

# 집합구조 만들기
# set(리스트,튜플) , {아이템1, 아이템2 ...}
myClas = {'python','c','java', 'c++'}
print(myClas, type(myClas))
if '어셈블리' not in myClas:
    print('어셈블리 미수강')
if 'python' not in myClas:
    print('python 미수강')
else:
    print('python 수강')

# pass
print('-'*10)
if True:
    pass
print('pass Test end','-'*10)

myList = ['지페', '핸드폰', '카드']
print('집에 어떻게 갈까?...')
if '게임머니' in myList:
    pass
else:
    print('걸어가야 한다.')

# 반복문
# while 문
# for ... in
# for .. range()

# while 문 공식
# 초기값
# while 조건 :
#   명령문
#   조건이False?

# 1~10까지 출력하기
count = 1
while count < 11:
    print('count : ', count)
    # 빠져나가는 조건
    # count = count + 1
    count += 1

# 퀴즈 : 1~100 까지 합 구하기
total = 0
cnt = 1

while cnt <= 100:
    total += cnt
    # 빠져나가는 조건
    cnt += 1

print('1~100 까지 합은? ', total)

print('*'*10)
# * 증가해서 찍기
cnt2 = 1
while cnt2<11 :
    print('* '*cnt2 , cnt2 )
    # cnt2 증가
    cnt2 += 1

# * 감소해서 찍기
'''
*******
******
*****
****
***
**
*
'''
print('\n'*4)
cnt3 = 7
while cnt3>0  :
    print('* '*cnt3 , cnt3 )
    # cnt3 감소
    cnt3 -= 1

# 구구단 출력하기
'''
숫자 X 1 = ?
숫자 X 2 = ?
숫자 X 3 = ?
...
숫자 X 9 = ?

'''
guguNum = int(input('원하는 단을 입력하세요? ... '))
cnt4 = 1
while cnt4 < 10:
    print( '%d X %d = %d'%(guguNum, cnt4, guguNum*cnt4) )
    cnt4 += 1

# 무한루프와 if
# while True:
#   명령문
#   if 문으로 무한루프 제어 , break
# break 문은 제어문에서 빠져나갈때 사용

while True:
    ans = input('q를 입력하면 종료')
    if ans == 'q':
        break
print('무한루프 종료')

# 퀴즈
# 입력받은 값을 리스트에 추가한다.
# q 입력시 입력문 종료후 리스트 출력
# 빈 리스트 생성
resultList = []
while True:
    item = input('리스트에 추가할 요소를 입력하세요 ... (q:종료)')
    # ... 리스트 추가 명령어 append(), insert()
    resultList.append(item)
    if item == 'q':
        break
print('무한루프 종료')
print('리스트 출력', resultList)