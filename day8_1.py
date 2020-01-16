'''
Step0.sqlite3 모듈 연동

Step1. Db 연결
=> 연결변수(conn) 생성
=> 작업변수(cursor) 생성

Step2. 테이블 생성
# sql 명령 실행
작업변수.execute(테이블 생성 sql)
...
# 실제 DB의 테이블에 반영
연결변수(conn).commit()

테이블 스키마
테이블이름 : book1
필드와 자료형
  아이디  id int => 기본키, 필수항목, 자동숫자증감
  책제목  title text => 필수항목
  출판사  writer text => 필수항목
  페이지수 page int => 필수항목
  가격    price int => 필수항목
  CREATE TABLE book1 (
	id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	title	TEXT, NOT NULL,
	writer	TEXT, NOT NULL,
	page	INTEGER, NOT NULL,
	price	INTEGER, NOT NULL
);
'''

# sqlite 임포트
import sqlite3

# 데이터베이스 연결
# 연결변수(conn) = sqlite3.connect(데이터베이스경로)

# Db 연결
# Db가 없으면 지정한 경로에 새로 생성
conn = sqlite3.connect('data/book.db')

# Db

# 작업변수(cusor) 생성
cursor = conn.cursor()

# --------- 테이블 생성
# 테이블 sql
cursor.execute('''  CREATE TABLE IF NOT EXISTS book1 (
	id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	title	TEXT, NOT NULL,
	writer	TEXT, NOT NULL,
	page	INTEGER, NOT NULL,
	price	INTEGER, NOT NULL
);
''')

# db에 테이블 생성 반영
conn.commit()


# ------ 테이블 출력
# 테이블의 레코드 모두 확인
# 작업변수(cursor).execute(select sql 명령)
# 리스트 변수 = 작업변수(cursor).fetchall()
# 리스트 변수 = 작업변수(cursor).fetchone()
# 리스트 변수 = 작업변수(cursor).fetchmany(레코드갯수)

cursor.execute('SELECT * FROM book1')
resultList = cursor.fetchall()
print('-'*30)
print('레코드 갯수 : ', len(resultList))
# 한 행씩 출력
for i in resultList:
    print('-'*30)

# Db

