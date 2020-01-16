# mySQL 연동을 위한 모듈 임포트
import pymysql

# DB 연결변수 설정
conn = pymysql.connect(host='localhost',
                       port=3306, user='root',
                       passwd = 'pyclass',
                       db = 'sqldb',
                       charset = 'utf8')
# 커서 생성
cursor = conn.cursor()

# 작업변수 커서 실행
# 작업변수.execute(sql 명령)
# 전체 레코드
# cursor.execute('select * from usertbl;')
# 특정 컬럼명으로 추출
# cursor.execute('select userID, name, addr from usertbl;')

# 2차원 리스트에 저장하기
# 리스트이름 = 작업변수.fetchall() : 전체레코드
# 리스트이름 = 작업변수.fetchone() : 한개
# 리스트이름 = 작업변수.fetchmany(레코드갯수) : 레코드숫자만큼

# -------------- 테이블 생성
# 테이블 sql
# cursor.execute('''
#               CREATE TABLE IF NOT EXISTS bookTBL (
#                     	id	INT(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
#                     	title	VARCHAR(20) NOT NULL,
# 	                    writer  TEXT NOT NULL,
# 	                    page	INT(5) NOT NULL,
# 	                    price	INT(5) NOT NULL
#             );
#             ''')

# ---------------- 레코드 삽입 1 - 컬럼명 지정 없음
# INSERT INTO 테이블명 VALUES(값1, 값2 ... );
# cursor.execute(''' INSERT INTO bookTBL
#                         VALUES(NULL, '파이썬1', '박응용', 300, 25000
#                 ''')

# ---------------- 레코드 삽입 2 - ? 방식
# sql = " INSERT INTO book1(title, writer, page, price) VALUES(?, ?, ?, ?); "
# cursor.execute(sql, ('C 언어', '김C', 450, 4500))


# ---------------- 레코드 삽입 - % 방식
# sql변수 = 'INSERT INTO 테이블명(컬럼명1, 컬럼명2 ...)
#               VALUES(%s, %s, %s, %s);"
# cursor.execute(sql변수, (값1, 값2 ... ))

# -------------- 여러 레코드 삽입 - % 방식
data = (
        ('자바','김C',550,5500),
        ('포토샵','이몽룡',700,3500),
        ('일러스트레이터','김홍도',800,2500))
sql = '''
        INSERT INTO bookTBL(title, writer, page, price)
            VALUES(%s,%s,%s,%s)
        '''
cursor.executemany(sql,data);

# ----------- 레코드 수정 -% 방식

# sql = '''
#         UPDATE 테이블명
#             SET 컬럼명1 %s
#             WHERE 컬럼명2 = %s
#       '''
# cursor.execute(sql, (컬럼명1값,컬럼명2값))


# ----------- 레코드 삭제 -% 방식

# sql = '''
#         DELETE 테이블명
#             WHERE 컬럼명 = %s
#       '''
# cursor.execute(sql, (값))


# db에 테이블 생성 반영
conn.commit()

# 레코드 삽입
# def insertBook():
#     print('-'*10)
#     print('INSERT DATA')
#     title = input(" 책 이름 => ")
#     writer = input(" 지은이 => ")
#     page = int(input(" 페이지 수 => "))
#     price = int(input(" 가격 => "))
#     # title, writer, page, price
#     sql = '''INSERT INTO bookTBL(title, writer, page, price)
#               VALUES(%s, %s, %s, %s);
#       '''
#     cursor.execute(sql, (title, writer, page, price))
#     conn.commit()
#
# insertBook()
showBook()


# 레코드 삭제
'''
삭제할 책 번호는?
데이타가 삭제되었습니다.
책목록 모두 표시
'''

# DB 종료
conn.close()

def end():
    # DB 종료
    conn.close()

def update():
    # 수정할 책 번호는?
    # 선택? (1. 책제목 2.저자 3.페이지수 4.가격)
    # 1
    # 변경내용 => 파이썬
    # 내용이 수정되었습니다.
    pass

# 선택에 따라서 함수가 호출되도록 무한루프 작성
while(True):
    choice = int(input('1.목록보기 2.추가 3.수정 4.삭제 0.종료 \n => '))
    if choice == 1:
        showBook()
    elif choice == 2:
        insertBook()
    elif choice == 3:
        pass
    elif choice == 4:
        deletebook()
    elif choice == 0:
        end()
        break