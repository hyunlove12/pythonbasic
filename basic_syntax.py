# 이것은 주석입니다. 이 부분은 인터프리터가 해석하지 않습니다.
# 비교연산자는 논리값 반환

def func():
    # 블록은 들여쓰기가 시작되는 곳에서 시작된다.
    pass # 블록은 비어있으면 안된다. 구현부가 없을 경우도 pass

# 산술 연산자
def arith_oper():
    print("====산술연산자====")
    # +, -, *, /
    print("7 나누기 5", 7 / 5)  # 나눗셈. 정수와 정수의 나눗셈도 소숫점까지 표시
    print("7 나누기 5의 몫", 7 //  5)  # 나눗셈의 몫
    print("7 나누기 5의 나머지", 7 % 5)  # 나눗셈의 나머지

    # divmod() -> 나눗셈의 몫과 나머지
    print("divmod() : 몫, 나머지", divmod(7,5))
    print("7나누기5의 몫:", divmod(7, 5)[0])
    print("7나누기5의 나머지:", divmod(7, 5)[1])

    # 제곱 : **
    print("2의 3승", 2 ** 3)
    print("pow(2, 3)", pow(2, 3))

# 비교 연산자
def rel_oper():
    print("====비교(관계)연산자====")
    # <, <=, >,>=
    # ==(같다), !=(같지않다)
    # 결과는 논리값(True or False)
    print("1 > 3?", 1 > 3)
    print("6 equals 9?", 6 == 9)
    print("6 not equals 9?", 6 != 9)

    # 복합 관계식
    a = 6
    # a가 0부터 ~ 10 사이에 위치하는가?
    # 조건 1 : a > 0
    # 조건 2 : a < 10
    print(a, "가 0 ~ 10 사이?", a > 0 and a < 10) # and -> &
    # 복합 관계식 표현
    print(a, "가 0 ~ 10 사이?", 0 < a < 10)


    # 수치 자료형 이외의 자료형의 대소 비교 -> 각각의 자리수끼리 비교
    print("문자열의 대소:", "abcd" < "abd")
    print("리스트의 대소:", [1, 2, 3] < [1, 2, 4])
    print("튜플의 대소:", (1, 2, 3) < (1, 2, 4))


# 블록의 끝은 들여쓰기가 끝나는 지점이다.
def func2():
    print("Hello", "PYTHON", sep=",", end="!\n")
    (3 - 4J).real
    (3 - 4J).imag
    (3 - 4J).conjugate()


def variable_ex():
    print("====변수의 할당====")
    # 변수 선언 작업은 없다
    # 문자, 숫자, _의  조합 -> 숫자로 시작하면 안됨
    # .py 파일의 이름도 변수 명명 규칙에 따라 작성 -> 파일이름이 모듈이름으로 사용되기 때문
    # 예약어는 사용 불가
    import keyword
    print("예약어 목록", keyword.kwlist)
    # 유니코드 기반이어서 변수명도 다국어로 사용할 수 있다
    가격 = 10000

    # 변수 치환문 (치환 연산자 = )
    a = 10

    # 여러 변수의 동시 할당(좌변, 우변의 개수가 같아야 한다)
    b, c = 20, 30
    print(b, c)

    # 같은 객체를 여러 변수에 동시 할당
    d = e = f = 40
    print(d, e, f)

    # 동적 타이핑
    g = 2020
    print("g:", g, type(g))

    g = "Python" # 다른 타입의 객체 재할당
    print("g:", g, type(g))

    # isinstance( 객체, 점검할 타입)
    if isinstance(g, str):
        print(g, "는 문자열")
    else:
        print(g, "는 문자열이 아님")

    # 여러 개의 타입 중 하나인지 확인
    h = 2020
    if isinstance(h, (int, float)): # int이거나 float인지
        print(h, "는 산술 계산이 가능함")
    else:
        print(h, "는 산술 연산 불가")


if __name__ == "__main__":
    #func()
    #func2()
    #arith_oper()
    rel_oper()
    variable_ex()