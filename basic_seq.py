# 순차형의 객체들
# range, enumerate, zip


def using_range():
    """
    range : 범위 객체
        실제 데이터는 없고, 필요할 때 하나씩 생성한다.
        그 자체가 순차 객체 -> 길이, 인덱싱, 슬라이싱, 포함여부 등을 확인
    :return:
    """

    # 인자값이 1개 -> 끝경계
    seq = range(10) # 0부터 9까지(주의 : 끝경계값은 포함되지 않는다.)
    print(seq, type(seq))
    # 실제 데이터 확인
    print("numbers in seq :", list(seq)) # list객체로 만들경우 데이터의 개수가 많으면 메모리를 많이 차지하는 문제 발생

    # 인자값이 2개 -> 시작, 끝경계
    seq2 = range(2, 10) # 2부터 9까지
    print(seq2, type(seq2))
    print("numbers in seq2 :", list(seq2))

    # 인자값이 3개 -> 시작, 끝경계, 간격
    seq3 = range(2, 10, 2)  # 2부터 9까지, 간격 2
    print(seq3, type(seq3))
    print("numbers in seq3 :", list(seq3))

    # 간격값이 음수면 큰 수 -> 작은 수
    seq4 = range(10, 2, -1) # 10부터 3까지 거꾸로
    print(seq4, type(seq4))
    print("numbers in seq4 :", list(seq4))

    # range를 이용하여 숫자 Loop를 돌릴 수 있다.
    for num in range(2, 10):
        print(num)


def using_enumerate():
    """
    순차 자료형 Loop시 객체와 함께 인덱스도 필요한 경우 enumerate로 묶음
    -> (인덱스, 객체) 튜플이 반환
    :return:
    """
    colors = ["red", "yellow", "blue", "green", "orange"]

    # 튜플의 언패킹 이용하여 받는다. 하나의 객체만 선언하면 튜플형으로 들어가 있다
    for i, color in enumerate(colors):
        print("{}번 색상 -> {}".format(i, color))

    nums = [3, 6, 1, 7, 4, 2, 9, 0]
    # 예 : nums 리스트 내부 객체를 모두 두 배
    for i, num in enumerate(nums):
        # 내부 데이터 접근
        nums[i] = num * 2
    print("RESULT :", nums)


def using_zip():
    """
    zip 객체
    -> 여러개의 순차형을 하나로 묶어서
        동일 위치의 요소들을 튜플로 묶음
    :return:
    """
    english = "SUN", "MON", "TUE", "WED"
    korean = '일요일', "월요일", "화요일", "수요일", "목요일"
    # 길이가 다르면 짧은 쪽을 기준으로 하나로 묶는다.
    engkor = zip(english, korean)
    print(engkor, type(engkor))

    # 기본적인 loop
    for pair in engkor:
        print(pair, type(pair))

    # zip은 1회 소비성 객체이다. -> 한번 반복문을 돌리면 소비되어 사라진다. 다시 zip객체를 생성해 주어야 한다.
    for eng, kor in engkor:
        print("영어 {} -> 한국어 {}".format(eng, kor))
    engkor = zip(english, korean)
    # 언패킹을 이용한 loop
    for eng, kor in engkor:
        print("영어 {} -> 한국어 {}".format(eng, kor))

    # 사전을 만들 때, zip 객체를 이용하기도 함
    engkor = zip(english, korean)
    dct = dict(engkor)
    print("영한사전 :", dct)


if __name__ == "__main__":
    #using_range()
    #using_enumerate()
    using_zip()
