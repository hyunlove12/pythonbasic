def handling_exception():
    """
    예외처리 연습
    :return:
    """
    lst = []

    try:
        # lst[3] = 1 # TODO : 예외처리
        int("2")
        4 / 2
    except IndexError as e:
        print("인덱스 접근 예외 발생 : IndexError", type(e))
    except ValueError as e:
        print("타입 캐스팅 실패 : ValueError", type(e))
    except ZeroDivisionError as e:
        print("0으로는 나눌 수 없어요", type(e))
    except Exception as e: # Exception객체는 모든 예외를 처리할 수 있는 예외 객체
        # Exception 객체로 예외처리는 가장 마지막에 워치하도록
        print("예외 발생 :", e)
        print("예외 타입 :", type(e))
    else:
        print("오류를 발견하지 못함!")
    finally:
        # 예외 유무에 상관없이 가장 마지막에실행
        # 예외가 있을 경우 try -> except -> finally 순서
        # 예외가 없을 경우 try -> else -> finally 순서
        print("try 블록 종료")

    print("코드진행") # try except가 없으면 진행되지 못한다.


def raise_exception():
    """
    강제 예외 발생
    # 함수 내부에서 완벽하게 예외처리를 해낼 수 없다면
    # 함수를 호출한 측에 예외를 강제로 호출하면
    # 호출한 측에서 함수 내부에서 발생한 예외를 대신처리할 수 있다.
    :return:
    """

    def beware_dog(animal):
        # 이 함수는 animal로 dog가 돌아오면 예외 발생
        # 아니면 어서오세요를 출력
        if animal.lower() == 'dog':
            # 예외 발생
            # 예외 발생한 것을 밖의 try에서 처리하는 구조 -> try가 없으면 완벽하게 처리되지 않는다.
            raise RuntimeError("강아지는 출입을 제한합니다.")
        print("어서오세요 :", animal)
    try:
        beware_dog("cow")
        beware_dog("cat")
        beware_dog("dog")
    except Exception as e:
        print(e, type(e))


if __name__ == "__main__":
    #handling_exception()
    raise_exception()