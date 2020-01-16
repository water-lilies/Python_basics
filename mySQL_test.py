# https://dev.mysql.com/downloads/file/?id=486089
# No thanks, just start my download. 클릭후 다운로드
# 다운로드 파일명 :
# mysql-installer-community-8.0.16.0.msi

# MySQL 설치후 아래 파일로 DB 연결되는지 테스트

# pymysql 설치
# pip install pymysql
# pip list

import pymysql

# 1) mySQL 워크벤치 실행
# 2) 파이참에서
#   [File]-[Settings]
# 3) Project ~ 카테고리 클릭
# 4) [Project Interpreter] 클릭
# 5) [+] 클릭
#    PyMySQL 검색후 설치
# 6) 공유폴더에서 mySQL_test.py
#   다운로드후 작업폴더에 붙이기
#   실행해서 데이타가 잘 나오는지 확인


# DB 연결
# password='루트계정비번'
# world는 MySQL 설치시 샘플 DB이므로 자동 설치됨

conn = pymysql.connect(host='localhost',
    port=3306, user='root',
    passwd='12345678',
    db='world',
    charset='utf8')
print('연결완료')

# 커서 생성
cursor = conn.cursor()

# 테이블조회
cursor.execute('select * from city;')
result_list = cursor.fetchall()
print(result_list[:10])