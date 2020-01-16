# csv
# Comma Seperate Value
# 콤마(,)로 데이타가 분리된 파일
# 엑셀양식의 데이터를
# 프로그램에 상관없이 쓰기 위한 데이터 형식

# csv 사용을 위한 임포트
import csv

# 작업폴더 위치 확인
import os
print(os.getcwd())

# csv 파일 읽기
# 파일변수 = open(csv파일경로, 'r', encoding='cp949/uft-8')
# csv 객체
# csv.reader(파일변수)
# for i in csv.reader(파일변수):
#   print(i)
# 파일변수.close()

f = open('data/data.csv', 'r', encoding='utf-8')
resultCSV = csv.reader(f)
print(resultCSV ) # _csv.reader object

# 한줄로 출력하기
# for i in resultCSV :
#     print(i)
#     print(type(i)) # <class 'list'>

print('-'*20)

# 리스트 구조로 변경하기
# 빈리스트를 생성하고 리스트요소로 추가하는 방식
resultList = []
for i in resultCSV:
    resultList.append(i)

# 리스트안에 리스트가 삽입된 구조
print(resultList)
print(len(resultList))
print(type(resultList))

# 첫번째 행
print(resultList[0])
# 첫번째 행의 두번째 열의 값
print(resultList[0][1])
# 마지막행의 마지막 열 값
print(resultList[-1][-1], type(resultList[-1][-1]))

# 퀴즈
# 첫번째 국어점수의 인덱스는? [1][2]
# 첫행은 제목행이므로 리스트에서 삭제
print(resultList)
resultList = resultList[1:]
print(resultList)

# 데이타값이 문자열이다. => float(), int() 숫자형으로 변경
# 국어점수만 리스트로 생성하기
# 모든 행에서 3번째(인덱스는 2)의 데이타만 추출
# 새로운 리스트에 정수형으로 변환하여 추가한다.
korList = []
for i in range(0, len(resultList)):
    korList.append(int(resultList[i][2]))
print('국어점수리스트 =>' , korList)

# 국어점수의 합계 구하기
print('국어점수 합계 =>', sum(korList))
# 국어점수의 평균 구하기
print('국어점수 평균 =>', sum(korList)/len(resultList))

# 파일 닫기
f.close()

print('-'*10)
# 퀴즈
# with 문으로 csv 파일 불러오기
# 가장 인구가 많은 주 ?
# 문자열에서 콤마 제거는? 문자열.replace(',','')
with open('data/population.csv', 'r', encoding='utf-8') as f:
    # resultCSV = csv.reader(f)
    # for i in csv.reader(f):
    #     print(i)
    # 빈 리스트 생성
    pList = []
    for i in csv.reader(f):
        pList.append(i)
    # 1행은 제거
    pList = pList[1:]
    print(pList)
    # 콤마가 있는 숫자 문자 => 정수형 => 데이타 교체
    for i in range(0,len(pList)):
        pList[i][1] = int(pList[i][1].replace(',',''))
    print(pList)
    # 첫번째 데이타를 초기값 지정
    maxCountry = pList[0][0]
    maxPopulation = pList[0][1]
    for i in range(0,len(pList)):
        if maxPopulation < pList[i][1]:
            maxCountry = pList[i][0]
            maxPopulation = pList[i][1]
    print('인구가 가장 많은 미국의 주는? ... ', maxCountry)
    print('인구가 가장 많은 미국의 주의 인구는? ... ', maxPopulation)







