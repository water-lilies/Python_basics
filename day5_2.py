# 현재 작업폴더 위치 확인하기
# python.exe 위치 , 현재 파이썬 파일 정보 출력
import os
print(os.getcwd())

# 파일입출력
# 파일읽기
# read() : 파일전체 문자열 구조
# readline() : 파일에서 첫줄만 읽기
# readlines() : 각행이 리스트 구조로 변경
# 파일변수 생성
# 파일변수  = open(파일경로, 'r')
f = open('data/Yesterday.txt', 'r')
# io 객체 출력
# <_io.TextIOWrapper name='data/Yesterday.txt' mode='r' encoding='cp949'>
print(f)
# 문서 전체가 출력
data = f.read()
print(data)
# <class 'str'> 문자열
print(type(data))
# 첫글자만 추출
print(data[0])
# 10글자만 추출
print(data[0:10])

# 문서는 몇개의 단어로 구성되어 있을까?
# 단어별로 구성해서 리스트 구조로 변경
# 문자열변수.split() => 공백기준으로 리스트로 변경
dataList = data.split()
# 10개만 출력
print(type(dataList))
print(dataList[:3])
print('단어 수? => ', len(dataList) )
# 파일 닫기 - 명령실행 뒤에 배치
f.close()

# 퀴즈
# 파일의 단어전체수와 3개의 단어가
# 표시되는 함수를 정의하여라
'''
>> 함수호출
printWord('data/sample.txt')
printWord('data/Yesterday.txt')

>> 결과값 
파일명 : data/sample.txt
단어 갯수 : 134
단어 3개 출력 
['Yesterday', 'All', 'my']
'''

# def printWord(fileUrl):
#     f = open(fileUrl, 'r')
#     data = f.read()
#     ?
#     f.close()

# printWord('data/sample.txt')
# printWord('data/Yesterday.txt')





