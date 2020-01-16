# sqlite3 모듈 임포트 => 내부모듈
import sqlite3

# SQLITE3 파이썬 모듈 버전
print(sqlite3.version) #2.6.0

# 데이타베이스 연결
# 연결변수(conn) = sqlite3.connect(데이타베이스경로)

conn = sqlite3.connect('data/chinook.db')
print('data/chinook.db 로 연결되었습니다.')

# 작업변수(cursor) = 연결번수.cursor()
cursor = conn.cursor()

# 연결된 DB에서 특정 테이블의 레코드 조회하기
# 작업변수(cursor).execute(레코드조회sql명령문)
cursor.execute('SELECT * FROM CUSTOMERS;')


# 파이썬의 리스트 구조로 저장하기
# 한개만 레코드 저장
# 리스트이름 = 작업변수(cursor).fetchone()
# 특정갯수 레코드 저장
# 리스트이름 = 작업변수(cursor).fetchmany(레코드수)
# 전체 레코드 저장
# 리스트이름 = 작업변수(cursor).fetchall()

resultList1 = cursor.fetchone()
print(resultList1)

resultList2 = cursor.fetchmany(10)
print(resultList2)

resultList3 = cursor.fetchall()
print(resultList3)


cursor.execute('SELECT CustomerId, FirstName, LastName FROM CUSTOMERS limit 10;')
resultList4 = cursor.fetchall()
print(resultList4)
print('Id', '\t', 'FirstName', '\t', 'LastName')
for i in resultList4:
    print('-'*30)
    # 각 데이터값 접근시에는 인덱스변수[컬럼인덱스]...
    print(i[0], '\t',i[1],'\t',i[2])
    # 각 행의 레코드는 튜플구조
    # (데이터값1, 데이터값2 ...)
    # print(i)

# 퀴즈) students 테이블의 레코드의 모든 데이터 표시하기. 한줄에 하나씩
# for i in 리스트:
#   print(i)



# 퀴즈 :
# albums 테이블의 전체 레코드 개수는?

# employees 테이블에서 title 컬럼명이 'IT Staff'인 레코드만 추출하여 표시하여라

# Albums 테이블에서 AlbumId가 5보다 크고 ArtistId가 12보다 한행 씩 작은 레코드만 표시하여라

# albums 테이블에서 마지막 레코드의 마지막컬럼의 데이터값을 표시하여라


# end DB
conn.close()