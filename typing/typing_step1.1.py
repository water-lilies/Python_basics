# 5 단계
'''
Ready? Press Enter Key!!!!
게임시작
.....
게임종료
.....
정답수 : ?
( 추가 과정 =>
데이터베이스 생성 : id(int) / count(int) / date(text)
아이디, 정답수, 오늘날짜를 데이타에 저장
오늘날짜 생성 : datetime 모듈 이용
)
게임을 종료하시겠습니까?(y) .....
'''
import sqlite3
import winsound
import random
import datetime



now = datetime.datetime.now()

# 오늘날짜, 현재시분초
print(now)
print(now.month)
print(now.hour)




with open('resource/word.txt','r') as f:

input('Ready? Press Enter Key!!!!')

word = f
random.shuffle(word)
print(word)
# 맞는 갯수 카운팅
cnt = 0
for i in word:
    sample = i.strip().split()
    print('\n', sample,'\n')
    inDate = input('단어 입력 : .....')
    if inDate.strip() == sample:
        winsound.PlaySound('sound/good.wav', winsound.SND_FILENAME)
        print(' Pass ')
        # 정답수 증가
        cnt += 1
    else:
        winsound.PlaySound('sound/bad.wav', winsound.SND_FILENAME)
        print(' Fail ')

print('정답 갯수 : ', cnt)




conn = sqlite3.connect('data/typingQuizDb.db')

cursor = conn.cursor()

cursor.execute('''
                CREATE TABLE IF NOT EXISTS quiz (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    count INTEGER NOT NULL,
                    date TEXT NOT NULL,
                );
              ''')

sql = " INSERT INTO quiz(count, date) VALUES(?, ?); "

cursor.execute(sql, (cnt, 4500))