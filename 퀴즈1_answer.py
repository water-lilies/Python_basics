# 퀴즈 1:
# 아래와 같이 3줄로 글자를 출력하는 4가지 방법은?
'''
파이썬
파이썬
파이썬
'''

# 방법1
print('파이썬')
print('파이썬')
print('파이썬')
print('*'*30)

# 방법2
print('파이썬\n'*3)
print('*'*30)

# 방법3
print('파이썬\n파이썬\n파이썬')
print('*'*30)
# 방법4
multiLine = '''
파이썬
파이썬
파이썬
'''
print(multiLine)
print('*'*30)



# 퀴즈 2
# 변수 a,b를 입력문을 이용하여 데이터를 저장한다.
# is 연산자나 == 을 이용하여 a,b 가 같은지 True, False 로 출력하여라
'''
a ? 10
b ? 10
True
'''
a = input('a ? ')
b = input('b ? ')
print(a == b)
print('*'*30)

# 퀴즈 3
# 2개의 숫자를 입력받아
# 사칙연산의 결과물을 출력하여라
# 출력시 % 포맷 형식 이용

'''
첫번째 숫자를 입력하세요? 34
두번째 숫자를 입력하세요? 56

결과 :
34 + 56 = 
34 - 56 =
34 * 56 =
34 / 56 =

'''

n1 = int(input('첫번째 숫자를 입력하세요?'))
n2 = int(input('두번째 숫자를 입력하세요?'))

print('\n\n결과 : ')
print('%d + %d = %d' % (n1,n2,n1+n2))
print('%d - %d = %d' % (n1,n2,n1-n2))
print('%d * %d = %d' % (n1,n2,n1*n2))
print('%d / %d = %f' % (n1,n2,n1/n2))

print('*'*30)

# 퀴즈 4
# 홍길동씨의 주민등록번호는 881120-1068234
# 연월일과 숫자 부분을 나누어서 출력하여라.
'''
연월일 : 881120
숫자 : 1068234
'''
print('*'*30)

pin = '881120-1068234'
yyyymmdd = pin[0:6]
num = pin[7:]
print('연월일 : ',yyyymmdd)
print('숫자 : ',num)

print('*'*30)

# 퀴즈 5
# 2개의 변수를 정의하고 아래와 같이 출력한다.
# format 이용

'''
movie1 = '알라딘'
movie2 = '스파이더맨'

--------------
스파이더맨      :        알라딘
+++   알라딘    +++

'''

movie1 = '알라딘'
movie2 = '스파이더맨'
print("{1:<10} : {0:>10}".format(movie1,movie2)) #스파이더맨      :        알라딘
print("+++{:^10}+++".format(movie1)) #+++   알라딘    +++

print('-'*30)

# 퀴즈 6
# 다음과 같이 교체한다.
# replace() 이용

'''
좋아하는 꽃 - 장미 

좋아하는 꽃 - 백합 

좋아하는 flower - 백합 
'''
quizTxt = '좋아하는 꽃 - 장미 '
print(quizTxt)
quizTxt2 = quizTxt.replace('장미','백합')
print(quizTxt2)
quizTxt3 = quizTxt2.replace('꽃','flower')
print(quizTxt3)



# 퀴즈 7
# 다음과 같이 문자열 변수를 정의하고 결과값이 출력되도록 한다.
'''
Let thy speech be short, comprehending much in few words.

첫번째 t의 위치 : 3
첫번째 m의 위치 : 28
s 의 갯수 : 3

= 으로 연결 : 
 L=e=t= =t=h=y= =s=p=e=e=c=h= =b=e= =s=h=o=r=t=,= =c=o=m=p=r=e=h=e=n=d=i=n=g= =m=u=c=h= =i=n= =f=e=w= =w=o=r=d=s=.

대문자로 변경 : 
LET THY SPEECH BE SHORT, COMPREHENDING MUCH IN FEW WORDS.
'''

message = 'Let thy speech be short, comprehending much in few words.'
print(message)
print('첫번째 t의 위치 : ', message.find('t')+1)
print('첫번째 m의 위치 : ', message.find('m')+1)
print('s 의 갯수 : ', message.count('s'))
print('\n= 으로 연결 : \n')
print('='.join(message))
print('\n대문자로 변경 :  \n')
print(message.upper())
