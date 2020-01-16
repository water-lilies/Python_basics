# 조건문 1
# if 조건:
#   명령문

# 조건문 2
# if 조건:
#   명령문1
# else:
#   명령문2

# 조건문 3
# if 조건:
#   명령문1
# elif 조건:
#   명령문2
# else:
#   명령문3

# False 조건
'', None, False, 0

# True
# True, 1, 문자열

# if 0: # False
# if '참': # True
# if None: # False
if '': # False
    print('test 중...')
print('test 끝')

# 양수인지 음수인지 구별하기
status = -10;
if status>0 :
    print('양수')
else:
    print('음수')

print('양수음수 판독 끝')

# 홀수니 ? 짝수니?

# num = int(input('숫자를 입력해주세요... ? ... '))
# status2 = num%2
# print(' 나머지 : ' , status2)

# if status2 == 1:
# if status2:
#     print('홀수')
# else:
#     print('짝수')

# 다중 조건
# 0, 음수, 양수
status3 = 0

if status3>0 :
    print('양수')
    print('-'*10)
elif status3<0 :
    print('음수')
    print('*'*10)
else :
    print('0')
    print('#'*10)
print('다중 조건 테스트 끝')

# 띠 테스트
# 띠 = 태어난년도%12
# 원숭이, 닭, 개, 돼지, 쥐, 소, 범, 토끼, 용, 뱀, 말, 양
# (0  ........  11)
result = 2009%12
animalList = ['원숭이', '닭', '개', '돼지',
              '쥐', '소', '범',
              '토끼', '용', '뱀', '말', '양']
print(result, animalList[result])

print( '-'*10, '\n\n' )
'''
if .. elif .. else 퀴즈 
태어난 년도를 입력하세요 ...? 2009
-------------------
태어난 년도 : 2009
당신은 소띠입니다. 
오늘의 운세:
  오늘은 독서하기에 좋은 날이다. 

'''
print( '-'*10, '\n\n' )

birth = int(input('태어난 년도를 입력하세요 ...?  '))
animalList2 = ['원숭이띠', '닭띠', '개띠', '돼지띠',
              '쥐띠', '소띠', '범띠',
              '토끼띠', '용띠', '뱀띠', '말띠', '양띠']
animal = birth%12
print( '당신은', animalList2[animal], '입니다. ' )
print('오늘의 운세:')

if animal == 0:
    print('사소한 일에 신경 쓰지 말고 마음의 안정을 찾아라.')
elif animal == 1:
    print('아직 때가 아니니 좀 더 기다려야 한다. ')
elif animal == 2:
    print('바른 마음가짐을 가지고 분수를 알고 행동해라. ')
elif animal == 3:
    print('노력이 소망을 이루는 지름길이다.')
elif animal == 4:
    print('더 가지려 말고 현재 것을 잘 간수해라.')
elif animal == 5:
    print('오늘은 독서하기 좋은 날이다.')
elif animal == 6:
    print('주변에 휩싸이지 말지어다.')
elif animal == 7:
    print('칭찬이나 혹은 용돈을 받을 수 있다. ')
elif animal == 8:
    print('중심을 잡아라. 바른 길을 걸어가야 한다. ')
elif animal == 9:
    print('생각도 못했던 곳에서 경쟁자 나타나리라. 주의하면서 행동하라.')
elif animal == 10:
    print('외출이나 여행은 되도록이면 삼가는 것이 좋다. ')
elif animal == 11:
    print('공부에 대한 처음 열정이 매우 높아지는 하루다.')

















