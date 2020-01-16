# 오류?
# 오류의 종류
# NameError: 함수이름, 변수, 리스트 이름등이 잘못된 경우
# IndexError :  튜플,리스트의 잘못된 인덱스 접근
# ZeroDivisionError : 0으로 나눈 경우
# FileNotFoundError : 잘못된 파일 경로
# SyntaxError 제외 => 예외처리 try: ~ Except 구문에서 제외

# 예외처리(Exception) 란?
# 오류가 발생을 하면 메세지를 출력하거나
# 오류를 무시하는 기능

# 에러처리 문법 1
# try:
#   명령어
# except 에러코드 as e:
#   에러처리명령

# 0으로 나눈 경우

#  에러코드 출력
try:
    23/0
except ZeroDivisionError as e:
    print(e, '가 발생')

# 에러코드를 모르는 경우
try:
    23/0
except:
    print('오류 발생, 0으로 나누지 못함 ')

print('Hello Python')

# 에러처리 문법 2
# try:
#   명령어
# except 에러코드 as e:
#   에러처리명령
# else:
#   에러가 발생하기 않은 경우 명령어

myList = [1,2,3]
try:
    # print(myList[3])
    print(myList[0])
except IndexError as e:
    print(e, '가 발생')
else:
    print('정상적으로 접근이 가능합니다.')

# 에러처리 문법 3
# try:
#   명령어
# except 에러코드 as e:
#   에러처리명령
# else:
#   에러가 발생하기 않은 경우 명령어
# finally:
#   무조건 실행되는 명령어

try:
    # pint('dkdkk')
    print('dkdkk')
except NameError as e:
    print(e,'가 발생')
else:
    print('에러가 없습니다.')
finally:
    print('에러 처리 완료')

# 에러 무시 : pass 키워드 사용
# try:
#   명령어
# except:
#   pass

try:
    f = open('d.txt', 'r')
except:
    pass
print(' 명령 실행 끝')

# 퀴즈 1
# 2개의 데이타값을 입력받은 후 나누기 명령을 실행한다.
# 에러가 발생하면
#   에러 메세지 출력 : '데이타 오류 ...'
# 에러가 발생하지 않으면
#   결과 수행 : n1 / n2 = ?

a = int(input('숫자를 입력하세요?   ...'))
b = int(input('숫자를 입력하세요?   ...'))
try:
    a/b
except ZeroDivisionError:
    print('0 으로 나눌 수 없습니다')
else:
    print('{} / {} = {} '.format(a,b,a/b))
finally:
    print('명령을 완료했습니다.')

# 퀴즈 2
# data_eng.txt 파일을 파일 변수로 저장한다.
# data_eng.txt 파일이 없다면 (에러발생)
#   메세지 출력. => '파일없음'
# 파일이 있다면 (에러가발생하지 않는다면)
#   총합과 평균을 구하여 출력한다.

try:
    # f = open('data_eng.txt', 'r')
    f = open('data/data_eng.txt', 'r')
except:
    print('파일 없음')
else:
    resultList = f.readlines()
    print(resultList)
    total = 0
    for i in range(0,len(resultList)):
        total += int(resultList[i])
    print('총합계 : ', total)
    print('평균 : ', total/len(resultList))

# 모든 예외의 에러 메시지를 출력할 때는 Exception 키워드
# try:
#     명령
# except Exception as e:
#     print(e)

try:
    23/0
except Exception as e:
    print(e)





