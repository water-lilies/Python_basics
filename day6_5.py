import csv

# 리스트 데이타를 csv 파일 쓰기
# 리스트는 2차원이어야 한다.
# [[1행...], [2행...] ]
# 파일변수 = open(csv파일경로, 'w', encoding='uft-8')
# csv변수 = csv.writer(파일변수)
# for i in 리스트:
#   csv변수.writerow(i)
# 파일변수.close()

myList = [['이름','주소','전화번호'],
          ['김영희','부산시','010-6374-90874'],
          ['홍길동','춘천시','010-5463-9403'],
          ['성은희','서울시','010-4646-9403']]
f = open('data/addr.csv','w', newline='', encoding='cp949')
csvline = csv.writer(f)
for i in myList:
    csvline.writerow(i)
print('파일쓰기가 완료되었습니다.')
f.close()

# with 문으로 교체
# 기존 파일에 데이타 추가
with open('data/addr2.csv','a', newline='', encoding='cp949') as f:
    csvline = csv.writer(f)
    for i in myList:
        csvline.writerow(i)
    print('파일쓰기가 완료되었습니다.')








