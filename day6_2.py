# 사용자정의 모듈
# step1 - 같은 폴더에 모듈명.py 생성
# step2 - 모듈명.py에 모듈함수(인자)를 정의


# 같은 폴더에 test.py 파일 생성
'''
def test():
    return 'test Module'
'''

# test.py 안의 함수를 사용할 수 있도록
# 모듈로 임포트
# import 모듈파일명
import test

# 모듈명.함수로 호출
print(test.test())
print(test.sumPrint(10,40))

# 퀴즈 - gugu.py 파일을 생성한 후
# gugu.py 파일안에 구구단을 호출하는
# 모듈함수 guguPrint(숫자) 를 정의하여라
# 현재파일에서
# gugu 모듈을 임포트한 후
# 모듈 함수 guguPrint(숫자)를 호출하여라
'''
import gugu 

gugu.guguPrint(7)
'''

import gugu
gugu.guguPrint(7)



