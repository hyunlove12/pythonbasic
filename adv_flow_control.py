# 흐름 제어(Flow Control)
# 1. 조건문
# 2. 반복문
# 프로그램의 흐름을 변경

# if ~ else ~ else
def if_statement():
    # 금액을 입력받고
    # 10000원 이상이면 by taxi
    # 2000 ~ 10000이면 by bus
    # 그 미만이면 on foot을 출력
    money = int(input("얼마 가지고 있어?"))

    # 조건 판별
    message = "" # 출력 메시지
    """
    if money >= 10000: # 첫번째 조건의 판별
        message = "by taxi"
    elif money >= 2000: # 추가 조건 판별
        messgae = "by bus"
    else: # 위 조건 중 만족하는 것이 없을 때의 처리
        message = "on foot"
    """
    # 중첩 if : if문은 중첩할 수 있다.
    if money < 2000: # 1차 조건 판별
        message = "on foot"
    else:
        if money >= 10000:
            message = "by taxi"
        else:
            message = "by bus"

    print("이동 방법 :", message)

def if_expr():
    """
    조건 판별 식
    -> 조건 판별을 계산시 내부에서 수행하는 방법
    :return:
    """
    money = int(input("얼마 가지고 있어?"))
    message = "by taxi" if money >= 10000 else "by bus"\
                                            if money >= 2000 else "on foot"
    print("이동 방법 :", message)


def for_ex():
    """
    for 문 연습
    Systax : for 객체 in 순차형
    :return:
    """
    # 연습 1: 1 ~ 100 정수 합산
    result = 0
    for num in range(1, 101): # 1 ~ 100의 정수
        result += num
    else: # 루프 정상 종료 시 실행
        print("합산 완료")
    print("결과 :", result)

    # 연습 2: 구구단
    # 중첨 for
    for dan in range(2, 10): # 2 ~ 9
        print(dan, "단")
        for num in range(2, 10):
            print("{} * {} = {}".format(dan, num, dan * num))

    # 연습 3: 삼각형 그리기
    for num in range(1, 6):
        for i in range(1, num):
            print("*", end="")
        else:
            print()
    else:
        print()

    # 삼각형 그리기 풀이2
    for num in range(1, 6):
        print("*" * num)


def if_test():
    """
    조건 판별 식 테스트
    :return:
    """
    # money = int(input("얼마 가지고 있어?"))
    money = 10000
    message = "by taxi" if money >= 10000 else "by bus"
    print("이동 방법 :", message)
    num = [1, 2, 3, 4, 5]
    num2 = [i for i in num if i > 2]
    print(num2)


def list_comp():
    """
    리스트 내포
    Systax : [표현식 for 객체 in 순차형 if 추출 조건]
    :return:
    """
    nums = list(range(1, 11))
    print("nums :", nums)
    # nums 리스트의 각 요소를 제곱한 새로운 리스트를 생성
    result = []
    for num in nums:
        result.append(num ** 2)
    print("result :", result)

    # 내포방식
    result = [num ** 2 for num in nums]
    print("리스트 내포 방식의 result(comp) :", result)

    # 문자열 리스트
    words = ["a", "as", "bat", "cat", "dove", "python", "c"]
    # 문자열 리스트 중에서 길이가 3글자 이상인 단어만 별도 리스트로 생성
    result = [word.upper() for word in words if len(word) >= 3]
    print("words(comp) :", result)

    # 1 ~ 100 사이의 수열 중에서 짝수 리스트만 추출
    evens = [num for num in range(1, 100) if num % 2 == 0]
    print("Evens :", evens)

def set_comp():
    """
    SET 내포
    Syntax : {표현식 for 객체 in 순차형}
    :return:
    """
    words = ["a", "as", "bat", "cat", "dove", "python", "c"]
    # 문자열의 길이를 set으로 저장해 봅시다.
    # 단, 중복허용이 되지 않기 때문에 중복되지 않은 데이터만 저장
    lens = {len(word) for word in words}
    print("WORD의 길이 :", lens)


def dict_comp():
    """
    사전의 내포
    Syntax : {키 표현식:값 표현식 for 객체 in 순차형 if 조건}
    :return:
    """
    words = ["a", "as", "bat", "cat", "dove", "python", "c"]
    # 단어를 키로, 단어의 길이를 값으로 가지는 사전을 생성
    len_dict = {word:len(word) for word in words}
    print("length of Word :", len_dict)

def while_ex():
    """
    while 문 연습
    # 반복 조건을 확인하기 위한 변수 객체를 개발자가 직접 제어
    # 무한루프에 빠질 위험이 있으므로 주의
    # 의도적으로 무한루프를 만들기도 한다 -> ex) 서버 프로그램
    :return:
    """
    # 연습 1: 1 ~ 100까지 수의 합
    num, result = 1, 0
    while(num <= 100):
        result += num
        num += 1 # 주의 -> 잘못 제어하면 무한루프에 빠질 수 있다.
    else:
        print("합산 완료") # 루프 정상 종료되었을 때 실행
    print("합산결과 :", result)
    print("합산결과 :", result)

    # 연습 2: 구구단
    dan = 2
    while(dan <= 9):
        print(dan, "단")
        num = 2
        while(num <= 9):
            print("{} * {} = {}".format(dan, num, dan * num))
            num += 1

        dan += 1 # 반복 조건 변수 제어
    else:
        print("구구단 정상 완료")

    # 연습 3
    # 1 ~ 100까지 while 루프 -> 3의 배수만 출력
    num = 0
    while num <= 100:
        num += 1
        # 체크
        if num % 3 != 0: # 3의 배수가 아님
            continue # 남아있는 명령 수행하지  않고 다음번 루프
        print(num, "는 3의 배수")
    else:
        print("루푸 종료")

    # 연습 4
    # 13과 17로 동시에 나누어 떨어지는 가장 작은 수는 무엇인가?
    num = 1
    while True:
        if num % 13 == 0 and num % 17 == 0:
            break # break의 경우 else는 실행되지 않는다.
        num += 1
    else:
        print("그런 수 없어요")

    print("최소의 수 :", num)


if __name__ == "__main__":
    #if_statement()
    #if_expr()
    #for_ex()
    #if_test()
    #list_comp()
    #set_comp()
    #dict_comp()
    while_ex()