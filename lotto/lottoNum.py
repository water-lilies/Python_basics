def lottoNum():
    lottoNum = []
    while True:
        # 탈출조건 : 번호 6개인지 확인
        if len(lottoNum) >= 6:
            break
        else:
            # 로또번호 생성
            data = random.randint(1, 46)
            # 로또번호가 리스트에 있는지 없는지 확인
            if data not in lottoNum:
                lottoNum.append(data)
    return lottoNum


 if __name__ == "__main__":
     print('main으로 실행')