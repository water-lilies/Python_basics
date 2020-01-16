# 정규표현식 ( Regular Expression)
# 유효성 검사
# 특정 문자열이 특정조건(패턴)에 맞는지 검사

# 파이썬에서 정규표현식 모듈 => re (내장모듈)
import re

# 관련 모듈함수
# re.findall()
# re.compile()
# 정규표현식패턴컴파일객체.match()
# group()

# 특정 글자를 포함하고 있는가?
# re.findall(문자열, 문자열대상) => 리스트로 리턴된다. (결과치가 리스트)
sampleTxt = 'It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout.'
print(re.findall('a',sampleTxt))

resultA = re.findall('a',sampleTxt)
print(type(resultA), 'a의 갯수 =>',len(resultA))

# 정규표현식 패턴 - 대문자, 소문자, 숫자, 한글
# [문자클래스스타일]   => 한글자씩
# [문자클래스스타일]+  => 단어단위
# [a~z] : 영어 소문자
# [A~Z] : 영어 대문자
# [0~9] : 숫자
# [가-힣] : 한글
# 영어소문자대문자 : [a-zA-Z]

print(re.findall('[a-z]','ab 1234 가나다 ABDJS abc가 123ab'))
print(re.findall('[a-z]+','ab 1234 가나다 ABDJS abc가 123ab'))

# 정규표현식 패턴 - 대문자, 소문자, 숫자, 한글 : \지원문자
# [\d] : 10진수
# [0-9]와 같음
# [\D] : 10진수 외 [^0-9]
# [\s] : 공백문자, [\t\n\r\f\v]
# [\S] : 공백문자 외, [ \t\n\r\f\v]
# [\w] : 영문자숫자, [a-zA-Z0-9]
# [\W] : 영문자숫자 외 , [^a-zA-Z0-9]

# 퀴즈 : 비밀번호 유효성 검사
# 조건 :
# 전체길이는 0~12
# 비밀번호는 특수문자는 제외, 영문자와 숫자로만 구성시켜라
# 비밀번호에 영어소문자, 영어대문자, 숫자가 꼭 1글자씩은 필요
'''
def pwdCheck(비밀번호)
    명령어

pwdCheck('123')
=> 비밀번호 길이가 적당하지 않습니다.

pwdCheck('#@12334')
=> 숫자와 영문자로만 구성되어야 합니다.

pwdCheck('cojhs1234')
=> 비밀번호로 적당하지 않습니다.    

pwdCheck('coJHs1234')
=> 비밀번호로 설정되었습니다.
'''
def pwdCheck(pwd):
    # 비밀번호 길이 체크
    if len(pwd) < 6 or len(pwd) > 12 :
        print('비밀번호 길이가 적당하지 않습니다.')
        # 함수에서 탈출
        return False
    # 숫자와 영문자 구성인자 체크
    if re.findall('[a-zA-Z0-9]+',pwd)[0] != pwd:
        print(pwd, '=> 숫자와 영문자로만 구성되어야 합니다.')
        return False
    # 소문자, 대문자, 숫자 모두 한글자씩 포함
    if len(re.findall('[a-z]',pwd)) == 0\
            or len(re.findall('[A-Z]',pwd)) == 0\
            or len(re.findall('[0-9]',pwd)) == 0:
        print(pwd, '=> 비밀번호로 적당하지 않습니다.')
        return False
    pass
    print(pwd, '=> 비밀번호로 설정되었습니다.')

# 실제함수 호출
pwdCheck('123')
pwdCheck('#@12334')
pwdCheck('cojhs1234')
pwdCheck('coJHs1234')

# re.compile(정규표현식패턴)
# 정규표현식을 컴파일한다. 객체로 생성

# 정규표현식패턴컴파일객체.match()
# re.compile(정규표현식패턴) 로 생성된 객체를 정규표현식과 맞는지 검사한다.
#       => re.Match 객체 / None

# p = re.compile(정규표현식패턴)
# m = p.match(대상문자열)

p = re.compile('[a-z]')
print(p,type(p))
print(p.match('fjjkf'))
print(p.match('123'))
print(p.match('DFSEF'))

# 데이터가 숫자면 => OK
# 데이터가 숫자가 아니면 => Fail

# if 조건 : => False
# 조건 => None, '', False, 0

def checkDigit(word):
    pattern = re.compile('[0-9]')
    m = pattern.match(word)
    if m:
        print(word,'OK')
    else:
        print(word, 'False')

checkDigit('dfdf')
checkDigit('9478')

# match객체.group()
#       => math()의 결과로 추출된 문자열 표시
# match객체.span()
#       => 튜플형태. 결과로 추출된 문자열의 인덱스 표시
# (start,end)

# 컴파일
pattern2 = re.compile('[0-9]')
# re.Match object, None
m1 = pattern2.match('1234ogjf')

print(m1.group())
print(m1.span())

# 정규표현식 메타문자
# + : 바로앞의 문자가 하나 이상 있음
# ^ : 문자열의 처음을 나타냄
# $ : 문자열의 끝
# . : 임의의 문자가 외도 됨
# * : 바로앞의 문자가 없거나 하나 이상 있음
# ? : 앞의 문자가 없거나 하나임

# 이메일 형식이면 True, False
p = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

emails = ['python@mail.example.com',
          'python+kr@example.com,'
          '@example.com',
          'python@example',
          'python@example-com']
# 정규패턴과 맞으면 True
# p.match(email) != Noen
for email in emails:
    print(email, p.match(email) != None)

# 위의 퀴즈를 참고해서 리스트에서 True 값인 이메일만 리스트 요소를 표시하여라

def chechEmail(emailList):
    # 패턴 컴파일
    p = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    print('결과 ===>')

    for i in emailList:
        # 이메일 형식이 아니라면 함수 탈출
        if p.match(i) == None:
            return False
        print(i)

chechEmail(emails)



