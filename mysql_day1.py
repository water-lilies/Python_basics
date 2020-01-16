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
cursor.execute('select userID, name, addr from usertbl;')

# 2차원 리스트에 저장하기
# 리스트이름 = 작업변수.fetchall() : 전체레코드
# 리스트이름 = 작업변수.fetchone() : 한개
# 리스트이름 = 작업변수.fetchmany(레코드갯수) : 레코드숫자만큼


result_list = cursor.fetchall()
print(result_list)
print('-'*20)
for i in result_list:
    print(i)
print('-'*20)
print(result_list[0]) # 1행
print(result_list[0][0]) # 1행1열

# 퀴즈 1:
# buytbl에서 1열만 출력하기
# 퀴즈 2:
# buytbl에서 마지막행만 출력하기
# 퀴즈 3:
# buyTbl에서 3행3열의 값 출력하기
# 퀴즈 4:
# userTbl에서 지역(addr)이 '서울'인 레코드만 표시하기
# 퀴즈 5:
# buyTbl에서 아이디(userID)값이 'KBS'인 레코드만 표시하기

print('퀴즈1','-'*20)
print(result_list[0])

print('퀴즈2','-'*20)
print(result_list[-1])

print('퀴즈3','-'*20)
print(result_list[2][2])

print('퀴즈4','-'*20)
cursor.execute("select * from usertbl WHERE addr='서울';")
list2 = cursor.fetchall()
for i in list2:
    print(i)

print('퀴즈5','-'*20)
cursor.execute("select * from buytbl WHERE userID='KBS';")
KBS = cursor.fetchall()
for i in KBS:
    print(i)

# DB 종료
conn.close()