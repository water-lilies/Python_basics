# 패키지(Package)
# 특정 모듈 파일을 저장하는 폴더 개념
# 패키지 폴더의 경우에는
# __init__.py 파일이 폴더안에 저장되어 있어야 한다.
# 파이참 에디터에서는 프로젝트 폴더에서
# 마우스 우측 -> Python Package 명령을 실행하면
# 자동으로 __init__.py 파일이 생성된다.
# 패키지안의 모듈 임포트
# import 패키지명.모듈
# 모듈함수 호출은?
# 패키지명.모듈.모듈함수(인자)

# import 패키지명.모듈 as 별칭
# 모듈함수 호출은?
# 별칭.모듈함수(인자)

# from 패키지명.모듈 import 모듈함수
# 모듈함수 호출은?
# 모듈함수(인자)

# 패키지 테스트
# AAA : 패키지 폴더
# AAA/a.py : 모듈 파일

# import AAA.a
# print(AAA.a.test_a())

import AAA.a as aM
print(aM.test_a())

# 퀴즈
# AAA 패키지안의 BBB 패키지안의 모듈 b 임포트
# test_b()를 호출

# import AAA.BBB.b as bb
# print(bb.test_b())

from AAA.BBB.b import test_b
print(test_b())

# 퀴즈 :
# 로또번호가 생성되는 lottoNum 모듈을
# lotto 패키지로 구성해서 작성한 후
# 모듈 함수를 호출하여라
# 모듈 파일 위치 : lotto/lottoNum.py
# lottoNumPrint() : 모듈 함수명
'''
import lotto.lottoNum

lottoNumPrint()
'''



