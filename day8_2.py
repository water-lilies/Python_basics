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


Step3. 레코드 삽입 Insert
# sql 명령 실행
작업변수.execute(레코드 삽입 sql)
...
못
적
음 확인하기



Step end. Db 종료
'''

# sqlite 임포트
import sqlite3

# 데이터베이스 연결
# 연결변수(conn) = sqlite3.connect(데이터베이스경로)

# Db 연결
# Db가 없으면 지정한 경로에 새로 생성
conn = sqlite3.connect('data/book.db')

# Db

# 작업변수(cursor) 생성
cursor = conn.cursor()

# --------- 테이블 생성
# 테이블 sql
cursor.execute('''
              CREATE TABLE IF NOT EXISTS book1 (
	id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	title	TEXT NOT NULL,
	writer  TEXT NOT NULL,
	page	INTEGER NOT NULL,
	price	INTEGER NOT NULL
);

''')

# ---- 레코드 삽입1
# INSERT INTO 테이블명 VALUES(값1, 값2 ...);
# cursor.execute(''' INSERT INTO book1
#                         VALUES(2, '파이썬1', '박응용', 300, 25000);
#                         ''')

# ---- 레코드 삽입 2 - 컬럼명 있음
# INSERT INTO 테이블명(컬럼명1, 컬럼명2 ...) VALUES(값1, 값2 ...);
# id 값 없이 지정
# cursor.execute(''' INSERT INTO book1 (title, writer, page, price)
#                         VALUES('파이썬1', '박응용', 300, 25000);
#                         ''')

# ---- 레코드 삽입 3 - ? 방식
# sql변수 = " INSERT INTO 테이블명(컬럼명1, 컬럼명2 ...) VALUES(?, ?, ? ...); "
# cursor.execute(sql변수, (값1, 값2 ...))    --> 값들이 물음표 안으로 들어간다.
# sql = " INSERT INTO book1(title, writer, page, price) VALUES(?, ?, ?, ?); "
# cursor.execute(sql, ('C 언어', '김C', 450, 4500))

# ---- 레코드 삽입 4 - 리스트, executemany()
# sql변수 = " INSERT INTO 테이블명(컬럼명1, 컬럼명2 ...) VALUES(?, ?, ? ...); "
# 2차원 리스트 정의
# 리스트변수 = [ (값1, 값2 ... )...]
# cursor.executemany(sql, 리스트변수)
sql = " INSERT INTO book1(title, writer, page, price) VALUES(?, ?, ?, ?); "
dataList = [('몽고DB', '박씨', 450, 4500),
            ('플라스크', '신씨', 450, 3400),
            ('HTML', '이씨', 450, 2300)]
cursor.executemany(sql, dataList)


# db에 테이블 생성 반영
conn.commit()


# ------ 테이블 출력
# 테이블의 레코드를 리스트로 저장한 후 출력
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
    print(i)

# Db
