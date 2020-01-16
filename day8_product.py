# 퀴즈 :
# 테이블 생성 및 CRUD 실습

# 0) productDb 생성
# 1) productTable 테이블 생성
#    모든 필드는 필수항묵 Not Null

#  제품코드(pCode) : Text, Primary Key
#  제품명(pName) : Text
#  가격(price) : int
#  재고수량(amount) : int

# 2) 데이터 삽입
#       5개 정도의 데이터 임의로 삽입
# 3) 모든 데이터 출력
# 4) 데이터 수정
#       p001의 가격(price)를 220으로 변경
# 5) 모든 데이터 출력
# 6) 데이터 삭제
#       마지막 레코드에 해당하는 데이터 삭제
# 7) 모든 데이터 출력

import sqlite3
conn = sqlite3.connect('data/productDb.db')
cursor = conn.cursor()

cursor.execute('''  CREATE TABLE IF NOT EXISTS productTable (
	pCode	TEXT NOT NULL PRIMARY KEY ,
	pName	TEXT NOT NULL,
	price	INTEGER NOT NULL,
	amount	INTEGER NOT NULL
);
''')

conn.commit()



sql = " INSERT INTO productTable(pCode, pName, price, amount) VALUES(?, ?, ?, ?); "
dataList = [('abcd', 'LCD', 450, 100),
            ('efcd', '너트', 360, 50),
            ('hijk', '볼트', 800, 3),
            ('lmno', 'ESS', 600, 10),
            ('pqrs', 'OLED', 950, 250)]
cursor.executemany(sql, dataList)


cursor.execute('SELECT * FROM productTable')
resultList = cursor.fetchall()
for i in resultList:
    print('-'*30)
    print(i)



