# 주소록 : addrDb
#
# 테이블스키마
# 테이블 이름 : addr1
# 필드와 자료형
#     아이디 id int => 기본키, 필수항목, 자동숫자증감
#     이름   name text => 필수항목
#     핸드폰 phone text => 필수항목
#     주소   address text => 필수항목
#     이메일 email text => 필수항목

# 모든 레코드를 출력하는 함수
#   - printData()

# 데이터를 입력받아서 레코드에 삽입하기
#   - 주의사항
#       : 데이터형
#       : 공백은 모두 삭제하고 문자만 삽입
#         문자열변수.strip()


import sqlite3

conn = sqlite3.connect('data/addrDb.db')

cursor = conn.cursor()

cursor.execute('''
                CREATE TABLE IF NOT EXISTS addr1 (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    phone TEXT NOT NULL,
                    address TEXT NOT NULL,
                    email TEXT NOT NULL
                );
              ''')
# db에 테이블 생성 반영
conn.commit()

def printAddr():
    cursor.execute('SELECT * FROM addr1')
    resultList = cursor.fetchall()
    print('-'*30)
    print('레코드 갯수 : ', len(resultList))
    print('id\tname\tphone\taddress\t\temail')
    print('-'*50)
    # 한 행씩 출력
    for i in resultList:
        print('-'*50)
        print(i)

# ------------------
# 데이터 입력을 종료 하시겠습니까?
# y 입력시 데이터 입력 종료
# 문자열변수.strip() => 공백제거



# -----------------
#
def inputData():
    while True:
    # 데이터 입력
        print('-'*50)
        print(' 주소 추가 \n')
        print('-' * 50)

        inName = input('이름 =>')
        inPhone = input('전화번호 =>')
        inAddress = input('주소 =>')
        inEmail = input('이메일 =>')
        sql = " INSERT INTO addr1(name,phone,address,email) VALUES(?,?,?,?);"
        # 공백제거후 데이터 삽입
        cursor.execute(sql, (inName.strip(), inPhone.strip(), inAddress.strip(), inEmail.strip()))
        # db에 테이블 생성 반영
        conn.commit()
        print('1개의 데이터가 추가되었습니다.')
    # 입력 종료
        qSign = input('데이터 입력을 종료 하시겠습니까?')
        if qSign.strip() =='y':
            break

# ------------------
# 데이터 삭제 함수
def delData():
    # 데이터 출력
    # 삭제할 데이터의 아이디를 입력해주세요? ...
    # 해댱 아이디의 레코드 삭제
    # 데이터 출력
    # 데이터 삭제를 종료하시겠습니까?
    while True:
        d = input('삭제할 데이터의 아이디를 입력해주세요? ...')
        sql3 = 'DELETE FROM addr1 WHERE id=?'
        cursor.execute(sql3, [d])

        # db에 테이블 생성 반영
        conn.commit()
        print('1개의 데이터가 삭제되었습니다.')
    # 입력 종료
        qSign = input('데이터 삭제를 종료 하시겠습니까?(y)...')
        if qSign.strip() =='y':
            break

    pass

# ------------------
# 메뉴선택
while True:
    print(' = 주소록 = ')
    print('1. 주소 입력')
    print('2. 주소 출력')
    print('3. 주소 삭제')
    print('4. 종료')
    choice = int(input('메뉴를 선택해주세요?.... => '))
    if choice == 1:
        # 주소입력함수 호출
        inputData()
    elif choice == 2:
        # 출력함수 호출
        printAddr()
    elif choice == 3:
        delData()
    elif choice ==4:
        break




# 출력함수 호출
printAddr()


# Db 종료
conn.close()