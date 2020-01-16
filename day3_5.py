# 현재 년,월,일,시,분,초 출력하기
# time 객체를 이용한 모듈 임포트
import datetime

# 현재 시간을 기준으로 년,월,일,시,분,초 변수 생성
now = datetime.datetime.now()
print(now)
print(' 년도 : ', now.year)
print(' 월 : ', now.month)
print(' 날짜 : ', now.day)
print(' 시간 : ', now.hour)

# 오전과 오후 출력하기
if now.hour > 12:
    print('오후 : ', now.hour-12, '시', now.minute, '분')
else:
    print('오전 : ', now.hour)

# 월에 따라 메세지 출력하기
# 달에 따라 봄, 여름, 가을 ,겨울 메세지 출력
# 12, 1,2 : 겨울
# 3~5 : 봄
# 6~8 : 여름
# 9~11 : 가을
# print( now.month)
# if 3 <= now.month <= 5:
#   print('봄 메세지')












