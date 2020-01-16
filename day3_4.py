# for 인덱스 in range(start, end , step)
# range(start, end , step)
# list( range(start, end , step) ) : 순차적으로 숫자로 구성된 리스트
# tuple( range(start, end , step) ) : 순차적으로 숫자로 구성된 튜플
# set( range(start, end , step) ) : 순차적으로 숫자로 구성된 집합

print(range(1, 11))
print(list(range(1, 11)))
print(tuple(range(1, 11)))
print(set(range(1, 11)))
# 1~20 사이의 짝수 또는 홀수로 구성된 리스트 생성하기
listEven = list(range(2,21,2))
listOdd = list(range(1,21,2))
print(listEven)
print(listOdd )

# for 인덱스 in range(start,end,step):
#   명령문

# 1~10까지 출력하기
for i in range(1,11):
    print(i)

# 1~100까지 합구하기
# for i in range() 사용하기
total = 0
for i in range(1,101):
    total += i
print('1~100까지 합 : ', total)

# 1~100까지 짝수합구하기
total1 = 0
for i in range(2,101,2):
    total1 += i
print('1~100까지 짝수 합 : ', total1)

# 1~100까지 홀수합구하기
total2 = 0
for i in range(1,101,2):
    total2 += i
print('1~100까지 홀수 합 : ', total2)

# 한줄에 1~25 까지 5개씩 출력하기
'''
1 2 3 4 5
6 7 8 9 10
..
21 22 23 24 25
'''
for i in range(1,26):
    print(i, end=' ')
    if i%5==0:
        print()

# 퀴즈 : 별찍기1
'''
*
**
***
****
*****
'''

# 퀴즈 : 별찍기2
'''
*****
****
***
**
*
'''
print('-'*10, '\n')
for i in range(1,6):
    print('* '*i)

print('-'*10, '\n')
for i in range(1,6):
    print('* '*(6-i))

# 다중 for문
for i in range(1,6):
    print('count - ', i)
    for j in range(1,4):
        print('     sub : ', j)

#  전체 구구단 출력
'''
2단 : 
    2 x 1 = 2
    ...
    
3단 : 
    3 x 1 = 3
    ...   
    
'''
print('\n\n\n')
for i in range(2,10):
    print('== ', i, '단 :')
    for j in range(1,10) :
        print('%d X %d = %d'% (i,j,i*j) )
    print('-'*20)

# 리스트 for
# 리스트이름 = [ 결과값 for ... ]
# 짝수로 구성된 리스트 생성
listA = [ i for i in range(2,21,2)]
print(listA, type(listA) )

# for i in range(2,21,2):
#     print(i)

# 숫자중 3의 배수에서 -1로 구성된 리스트 생성
listB = [ i*3-1 for i in range(1,51)]
print(listB, type(listB) )

# 구구단의 결과값으로 구성된 리스트 생성
listC = [ i*j for i in range(2,10) for j in range(1,10) ]
print(listC , type(listC) )

# p146 ~ 148 연습문제 풀기
























