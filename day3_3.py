# for 인덱스 in 리스트,문자열,튜플:
#   명령문
# 리스트 요소 순차적으로 출력
# 인덱스 : 리스트아이템
foodList = ['초밥', '햄버거', '스테이크', '떡국']
# print('0 : ', foodList[0])
cnt = 0
for i in foodList:
    print(cnt, ' : ', i)
    cnt += 1

# 튜플목록 출력
t1 = (10,100,300,400,20)
for i in t1:
    print(i, end=' ')

# 문자열 출력
str1 = 'abcdefg'
for i in str1:
    print(i)

print('-'*10)

# 딕셔너리 요소 출력
# for key in 딕셔너리이름:
#   print(key, 딕셔너리이름[key])

dict1 = {'a':'apple', 'b':'banana', 'd':'dress'}
for key in dict1:
    # 키값이 출력
    # print(key)
    print( key , ' : ', dict1[key])

# 리스트에서 최대값, 최소값 출력하기
# for 문과 if 문 사용하기
numList = [100, 31, -5, 133, 156, 77, 67]
# 리스트의 첫번째 값이 최대값 초기값으로 지정
maxNum = numList[0]
for i in numList:
    # 최대값 교체
    if i > maxNum:
        maxNum = i
print('최대값은? ', maxNum)

'''
리스트의 최소값 ? ... ?
리스트의 합계 ?  ...  ?
리스트의 평균 ?  ... ?
'''
numList2 = [100, 31, -5, 133, 156, 77, 67]
minNum = numList2[0]
listSum = 0
for i in numList2:
    # 리스트 합계
    listSum += i
    # 최소값 교체
    if i < minNum:
        minNum = i
print('리스트의 최소값 ? ', minNum)
print('리스트의 합계 ? ', listSum)
print('리스트의 평균 ?  %.2f' % (listSum/len(numList2)))

# 학생점수 리스트에서 60점 이상일때 합격,
# 그렇지않으면 불합격
stList = [80, 45, 66, 23, 100, 90, 40]
'''
1번 학생 합격
2번 학생 불합격
...

'''
stNum = 1
for i in stList:
    # print(stNum, '번 학생 : ', i)
    if i >= 60:
        print(stNum, '번 학생 : 합격 ')
    else:
        print(stNum, '번 학생 : 불합격 ')
    stNum += 1

# continue : 현재 단계만 패스. 하단 명령은 실행되지 않는다.
numList = [1,2,3,4,5,6,7,8,9,10]
# 홀수값만 출력
for i in numList:
    if i%2 == 0:
        continue
        # break
    print(i)

# 아래의 학생 점수 리스트에서 60점이상인 학생만
# 번호와 함께 합격을 축하합니다. 메세지 출력
# for .. in list, continue, if 사용
'''
1 번 학생 축하합니다.
3 번 학생 축하합니다. 
...
 
'''
print( '\n\n - 합격 메세지 출력하기 - ')
stList2 = [80, 45, 66, 23, 100, 90, 40]
stNum2 = 0
for i in stList2:
    stNum2 += 1
    if i < 60:
        continue
    print(stNum2, '번 학생 합격을 축하합니다. ')

print('-'*10)
# 2차원 리스트 출력하기
listMulti = [[1,2,3],
             ['a','b','c'],
             ['홍길동','춘향이','이몽룡']]
print(listMulti)
print(listMulti[0]) # [1,2,3]
print(listMulti[1][1]) # b
print(listMulti[-1][-1]) # 이몽룡

# for (인덱스1, 인덱스2 ...) in 리스트이름:
#   print( 인덱스1, 인덱스2 ...)

for (i, j, k) in listMulti:
    # 각 행별로 출력
    print( i, j, k)

listMulti2 = [[1,2],
             ['a','b'],
             ['홍길동','춘향이']]

for (i, j) in listMulti2:
    # 각 행별로 출력
    print( i, j)

# 퀴즈 : 학생이름, 국어, 영어, 수학 으로 구성된
# 2차원 리스트를 생성한다.
# 출력형식은 아래와 같이 한다.
'''
학생이름  국어  영어  수학  합계  평균   
김태희     30   40   100   ?     ?
...

'''
stGradeList = [['김태희', 30, 50, 55 ],
               ['신민아', 50, 90, 80 ],
               ['박지민', 50, 90, 40 ],
               ['김소희', 60, 50, 56 ],
               ['윤준희', 90, 88, 66 ] ]

print ('학생이름  국어  영어  수학   합계   평균 ')
print( '-'*50)
for (name, i, j, k) in stGradeList:
    # print(name, i, j, k, (i+j+k), ((i+j+k)/3))
    print(' %s   %d   %d    %d   %d    %.2f' % (name, i, j, k, (i+j+k), ((i+j+k)/3)))






