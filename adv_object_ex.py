# 객체의 이해

# 글로벌 영역 -> 내부에 있는 어디서든 접근할 수 있는 영역
g_a = 1
g_b = "Global"

# 객체 심볼 테이블의 영역
#   Local 영역
#   Enclosed 영역
#   Global 영역(해당 Py 모듈 내부)
#   Builtin 영역(파이썬 실행 환경)


def func():
    l_a = 2
    l_b = "Local"
    print(locals()) # 로컬 영역의 심볼 테이블 확인


def symbol_table():
    print("GLOBAL :", globals()) # 글로벌 영역의 심볼 테이블 확인
    print("Type of globals()", type(globals()))

    func()

    # symbol table은 dict
    print("g_a in global scope?", "g_a" in globals())

    # 각각의 영역별로 심볼 테이블을 별도 관리하고 있다는 점이 중요
    # 객체에 접근할 때 순서는 Local -> Enclosed -> Global -> Builtin 순으로
    # 검색을 한다(중요)


def object_id():
    # 불변형 자료 -> 값이 같으면 같은 객체다
    # 가변형 자료 -> 값이 같아도 다른 객체다
    x = 10
    y = 10

    print("x의 주소:", hex(id(x))) # id() 함수 -> 개체 주소 확인
    print("y의 주소:", hex(id(y)))

    # x의 주소와 y의 주소는 같은가?
    print("x의 주소는 y의 주소와 같은가?", id(x == id(y)))
    # 두 객체의 주소가 같다 -> 같은 객체

    # == vs is
    # == : 값의 비교 -> 동질성의 비교
    # is : 주소의 비교 -> 동일성의 비교
    print("x == y :", x == y) # 값의 비교
    print("x is y :", x is y) # 주소의 비교

    # 불변 자료형의 경우
    lst1 = [1, 2, 3]
    lst2 = [1, 2, 3]

    print("lst1 == lst2?", lst1 == lst2)
    print("lst1 == lst2?", lst1 is lst2)
    # lst1, lst2 -> 같은데이터를 가지고 있지만 다른 객체다
    # 불변자료형 -> 값이 같으면 같은 객체다
    # 가변 자료형 -> 값이 같아도 다른 객체일 수 있다.

    #####################################################################
    # 테스트 시작
    print(locals())
    print(globals())  # 심볼테이블

    # 참조 객체이기 때문에 값이 똑같이 나온다.
    a = [1, 2, 3]
    b = a
    print(a)
    print(b)
    a.append(4)
    print(b)

    # id() 객체의 주소 확인
    # 불변 자료형은 같은 객체를 참조
    # 가변 자료형은 값이 같아도 다른 객체를 참조
    a = 10
    b = 10
    print(id(a))
    print(id(b))

    a = [1, 2, 3]
    b = [1, 2, 3]
    c = b
    c[0] = 100
    print(id(a))
    print(id(b))
    print(id(c))
    print(id(b) == id(c))  # print( a is b )와 같음 -> 동일성 비교 // print( a == b ) -> 동질성의 비교
    print(hex(id(a)))
    print(b[0], c[0])
    c = b[:]  # 객체 전체를 복사하기 때문에 새로운 객체가 생성된다.
    print(id(b) == id(c))
    # 테스트 끝
    #####################################################################


# symbol_table()
# 가장 먼저 실행되는 범위
#object_id()

def object_copy():
    """
    객체의 복제
    -> 유의 : 특히 복합 객체의 경우
    :return:
    """
    a = [1, 2, 3]
    b = [4, 5, 6]
    x = [a, b, 100]

    # 레퍼런스 복제 -> 단순 주소를 복제
    y = x
    print("x의 주소 :", id(x))
    print("y의 주소 :", id(y))

    print("x is y?", x is y)

    # 얕은 복제
    # [:] -> 전체 -> 새로 할당
    # .copy 메서드
    # copy 모듈의 copy 메서드
    import copy # copy 모듈의 사용
    y = copy.copy(x)
    print("x is y?", x is y)

    print("x :", x)
    print("y :", y)

    # x와 y는 별개의 객체지만 내부의 자료 a, b는 동일 주소
    print("x[0] is y[0]", x[0] is y[0])
    # 복합 객체의 얕은 복제는 문제를 일으킬 수 있다
    y[0][0] = 100
    print("x :", x)

    # 복합 자료형의 경우는 내부 데이터도 복제해서 다시 할당해야 한다
    # 깊은 복제(중요)
    y= copy.deepcopy(x) # 깊은 복제
    print("x :", x)
    print("y :", y)

    y[1][0] = 100
    print("x :", x)
    print("y :", y)


if __name__ == "__main__":
    #symbol_table()
    object_copy()
