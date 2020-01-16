# 문자열 함수
# 샘플문자열 만들기 : https://www.lipsum.com/
# Lorem Ipsum 키워드 검색
sampleTxt = '''
It is a long established fact t
hat a reader will be distracted by the readable 
content of a page when looking at its layout. 
The point of using Lorem Ipsum is 
that it has a more-or-less normal distribution 
of letters, as opposed to using 'Content here, c
ontent here', making it look like readable English. 
Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, 
sometimes on purpose (injected humour and the like).
'''

# 특정 문자열의 갯수 출력
# 문자열.count(찾고자하는문자열)
print('t의 갯수 : ', sampleTxt.count('t'))
print('here의 갯수 : ', sampleTxt.count('here'))

# 특정글자의 위치값 반환
# 문자열.find(찾고자하는문자열)
# 문자열.index(찾고자하는문자열)
print(' f => ', sampleTxt.find('f'))
print(' f => ', sampleTxt.index('f'))
# 찾고자하는 문자열 없다면 -1
print(' 가 => ', sampleTxt.find('가'))
# 찾고자하는 문자열 없다면 ValueError 에러 발생
# print(' 가 => ', sampleTxt.index('가'))

# 문자열 교체
# 문자열변수.replace(문자열1, 문자열2)
sampleTxt2 = sampleTxt.replace('is','was')
print(sampleTxt2)
print('was 갯수 : ', sampleTxt2.count('was'))

# 대문자 upper(), 소문자 변환 lower()
print('-'*10)
print(sampleTxt.upper())
print('-'*10)

# 특정문자로 문자와 문자 사이 연결하기
# '연결문자'.join(문자열변수)
sampleWord = 'Python'
print('-'.join(sampleWord))

# 공백 제거하기
# 문자열변수.strip() / 문자열변수.rstrip() / 문자열변수.lstrip()
sampleTxt3 = '     hello python     '
print(sampleTxt3)
print('*',sampleTxt3.strip(),'*')
print('*',sampleTxt3.lstrip(),'*')

# 공백을 기준으로 리스트구조로 자료형 변환
# 문자열변수.split() , 문자열변수.split(구분문자)
sampleTxt4 = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec vestibulum ac velit eu posuere. Donec in erat purus. Maecenas tincidunt.'
print('-'*5)
print(sampleTxt4 )
print(type(sampleTxt4))
print('문자열 총 갯수 : ', len(sampleTxt4))

# 문자열 = > 리스트
result = sampleTxt4.split()
print(result)
print(type(result))
print('리스트 총 갯수 : ', len(result))












