# bool( 논리형 )
def bool_ex():
    print("==== bool 연습 ====")
    # True or False
    # 내부적으로는 정수의 변형 : False == 0, 나머지는 True
    # bool의 판정
    print(bool(0), bool(10))

    print("True는 bool?", isinstance(True, bool))
    print("True는 int?", isinstance(True, int))

    # 논리 연산자
    # or 연산자 : 두 논리값 중 하나만 True면 True
    # and 연산자 : 두 논리값 모두 True여야 True
    # not 연산자 : True <-> False
    # a != '' and b != ''

    # 1번 영역 0 ~ 10
    #     조건 1 : a > 0
    #     조건 2 : a < 10
    # 2번 영역 : 1번 영역 이외의 영역
    #     조건 1 : a <= 0
    #     조건 2 : a >= 10

    a = 5 # 1번 영역에 속한 값
    print(a, "는 0 ~ 10 사이의 값?", 0 < a < 10)
    print(a, "는 0 ~ 10 사이의 값?", a > 0 and a < 10)

    # 2번 영역 : or 연산자
    print(a, "는 2번 영역?", a <= 0 or a >= 10)
    # 2번 영역 : not 연산자
    print(a, "는 2번 영역?", not (0 < a < 10))

    # bool 캐스팅
    # 객체의 값이 비어있다 -> False
    # 객체의 값이 비어있지 않다 -> True
    print("int : ", bool(0), bool(2020))
    print("int : ", bool(""), bool("Python")) # 빈 문자열은 False
    print("list : ", bool([]), bool([1, 2, 3])) # 빈 리스트는 False


# 정수형(int)
def int_ex():
    print("====정수형 연습====")
    a = 2020
    b = int("2020") # 타 데이터 타입을 정수형으로 변환(캐스팅)
    print(a, type(a))
    print(b, type(b))

    # 2진, 8진, 16진 정수 표기
    b = 0b1010 # 2진수
    o = 0o23 # 8진수
    x = 0xFF # 16진수
    print(b, o, x)

    # Python 3.x Long, int 형을 구분하지 않음
    # Long 데이터 타입 8byte를 초과하는 정수도 처리
    i = 123456789012345678901234567890
    print(i)
    print("i의 비트 수 : ", i.bit_length())

    # 진법 변환 함수 : 정수형을 진법 변환 -> str
    print("42 -> 2진수", bin(42))
    print("42 -> 8진수", oct(42))
    print("42 -> 16진수", hex(42))


def float_ex():
    print("====실수형 연습====")
    # 소숫점을 포함하거나 지수 표기법으로 된 실수 데이터
    a = 3.14159
    b = float("3.14159") # 타 데이터 타입을 실수형으로 캐스팅

    print(a, "is", type(a))
    print(b, "is", type(b))

    # 주의)타입 캐스팅 시, 변환할 데이터가 실수형으로 변환될 수 있는 형태여야 한다.
    #c = float("a3.235235")

    c = 3.0
    # 형태 판별 : is_integer()
    print(a, "is", type(a))
    print(a, "는 정수 형태?", a.is_integer()) # 형태 판별, 타입 판별이 아님
    print(c, "is", type(c))
    print(c, "는 정수 형태?", c.is_integer())


def complex_ex():
    print("====복소수 연습====")
    # 실수부 + 허수부J
    # 산술 연산 가능
    a = 4 +5J
    print(a, "is", type(a))
    b = complex(7, -2) # 복소수 생성
    print(b, "is", type(b))

    # 산술 연산
    print(a + b)
    # 실수부와 허수부 확인
    print(a, "의  실수부 : ", a.real)
    print(a, "의 허수부 : ",a.imag)
    print(a, "의 켤레 복소수 : ", a.conjugate())


def internal_math():
    print("====내장 수치 함수====")
    print(abs(-3)) # 절대값
    print(divmod(5, 3)) # 나눗셈의 몫과 나머지
    print("5를 3으로 나눈 몫:", divmod(5, 3)[0])
    print("5를 3으로 나눈 나머지:", divmod(5, 3)[1])

    print(pow(2, 10)) # 2의 10제곱곱

if __name__ == "__main__":
    #bool_ex()
    #int_ex()
    #float_ex()
    #complex_ex()
    internal_math()