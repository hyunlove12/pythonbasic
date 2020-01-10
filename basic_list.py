# 리스트
# 순차 자료형 : Len, 인덱싱, 슬라이싱
# 순차 연산 : +(연결), *(반복), in, not in(포함 여부 확인)
# 가변 자료형 -> 내부 자료 변경될 수 있다

def define_list():
    """
    리스트 정의
    :return:
    """
    lst = [] # 빈 리스트
    lst2 = list() # list 함수 이용
    lst3 = [1, 2, "Python"] # 어떤 객체든 다 들어갈 수 있다.

    print(lst, type(lst))
    print(lst2, type(lst2))
    print(lst3, type(lst3))

    # 다른 순차 자료형을 리스트로 캐스팅
    s = "Python Programming"
    lst4 = list(s)
    print(s, lst4)

    syntax = "I like java, I like Python".replace(",", "").split()
    print(syntax)


def list_oper():
    """
    리스트의 연산
    :return:
    """
    lst = [1, 2, "Python"]

    # 길이의 확인
    print("Length of lst", len(lst))

    # 인덱싱
    print(lst[0], lst[1], lst[2]) # 정방향 인덱싱
    print(lst[-3], lst[-2], lst[-1]) # 역방향 인덱싱


    # 연결
    print(lst + [3, 4] == [1, 2, "Python", 3, 4])
    # 연결, 반복은 새 리스트를 만들어 낸다
    print(lst * 2 == [1, 2, "Python", 1, 2, "Python"])

    # 포함 여부 확인 : in, not in -> bool
    print("Python in lst? ", "Python" in lst)

    lst2 = [1, 2, 3, 4, 5, 6]
    print(lst2, "LENGTH :", len(lst2))

    # 슬라이싱
    print(lst2[2:4] == lst2[-4:-2])
    print(lst2[0:3] == lst2[:3]) # 시작 경계 생략하면 처음부터
    print(lst2[3:len(lst2)] == lst2[3:]) # 끝 경계 생락하면 끝까지
    print(lst2[::2]) # 처음부터 끝까지 간격 2
    print(lst2[::-1]) # 간격이 음수면 역방향

    print("ORIGINAL : ", lst2)
    # 슬라이싱을 이용한 삽입, 치환, 삭제
    # 삽입
    lst2[3:3] = [7, 8]
    print("슬라이싱을 이용한 삽입 :", lst2)
    # 치환
    lst2[3:5] = [9, 10]
    print("슬라이싱을 이용한 치환 :", lst2)
    # 삭제
    lst2[3:5] = [] # 빈 리스트로 교체 -> 삭제
    print("슬라이싱을 이용한 삭제 :", lst2)

    # 기초 산술 함수의 지원 : min, max, sum
    print("SUM of lst2 :", sum(lst2))
    print("MIN of lst2 :", min(lst2))
    print("MAX of lst2 :", max(lst2))
    print("평균 lst2 :", sum(lst2) / len(lst2))


def list_methods():
    """
    리스트의 메서드들
    :return:
    """
    lst = [1, 2, "Python"]

    # 객체의 복제 copy() 메서드
    cp = lst.copy()
    print("Data :", cp)

    # append vs extend
    # append : 개별 요소를 맨 뒤에 추가
    cp.append(["Java", True, 3.14159])
    print('Append :', cp)


    # 중첩되 리스트 내부 요소에 접근
    print(cp[3][0] == "Java")

    cp = lst.copy()
    print("Data : ", cp)
    # extend: 리스트를 맨 뒤에 연결(확장)
    cp.extend(["Java", True, 3.14159])
    print("EXTEND :", cp)
    # 연결(+) 연산이 새 리스트를 반환
    # extend는 내부 자료 자체를 변경하는 차이
    # 삽입 insert
    cp.insert(3, 3) # 3번 인덱스에 객체 3을 추가
    print("INSERT :", cp)
    # 삭제 remove
    cp.remove(3) # 내부에 있는 객체 3을 제거
    print("REMOVE :", cp)

    #cp.remove(3) # 없는 객체의 삭제 -> Error

    if 3 in cp: # 삭제 이전에 포함 여부 확인 -> 방저 코드
        cp.remove(3)
    else:
        print("3번 인덱스에는 값이 없습니다.")

    # 데이터의 추출 : pop
    print("pop:", cp.pop()) # 가장 마지막 요소를 추출 후 삭제
    print("Data:", cp)
    print("POP(index) :", cp.pop(3)) # 3번 요소를 추출 후 삭제
    print("Data :", cp)

    # 데이터 순서 반전 : reverse
    cp.reverse()
    print("REVERSE :", cp)

    # 객체의 인덱스 반환 : index
    print("INDEX of Python :", cp.index("Python"))
    if "Java" in cp:
        print("INDEX of JAVA :", cp.index("Java")) # 없는 객체 -> Error

    # 데이터의 정렬
    # sorted : 파이썬 문법의 정렬 함수 -> 특정 객체와 무관 -> 데이터 변경 없음
    # sort : 객체 내부의 정렬 메서드 -> 내부 데이터 변경 발생

    scores = [80, 90, 100, 20, 30, 60]
    print("Scores :", scores)

    print("SORTED ASC :", sorted(scores)) # scores 오름차순 정렬(낮은 점수 -> 높은 점수)
    print("원본 scores :", scores) # 원본 데이터는 변경되지 않는다.

    # 내림차순 정렬 : reverse 옵션 True
    print("SORTED DESC :", sorted(scores, reverse=True)) # 내림차순 변경

    # TODO : sorted, sort에 key옵션에 정렬 기준 정의 함수(키함수)를 부여하면
    #   정렬 기준을 바꿀 수 있다.

    print("Scores :", scores)
    scores.sort(reverse=True) # sort 메서드는 내부 데이터를 변경한다.
    print("SORT :", scores)


def stack_ex():
    """
    리스트를 활용한 Stack 자료형의 구현
    append로 input
    pop으로 output
    Last Input First Output(LIFO)
    :return:
    """
    stack = [] # 빈 스택
    print(stack, "LENGTH:", len(stack))
    stack.append(10)
    stack.append(20)
    stack.append(30)
    print("stack :", stack)

    # 데이터 추출 : POP
    print("POP :", stack.pop())
    print("stack :", stack)
    print("POP :", stack.pop())
    print("stack :", stack)
    print("POP :", stack.pop())
    print("stack :", stack)

    if len(stack): # 1이상이면 true(논리값이기 때문에 가능)
        print("POP :", stack.pop()) # Error -> empty리스트에서는 pop불가능


def queue_ex():
    """
    리스트를 활용한 큐 자료구조형의 구현
    Input : append
    Output : pop(0)
    First Input First Output(FIFO)
    :return:
    """
    queue = [] # 빈 큐
    print("QUEUE :", queue, "LENGHT :", len(queue))

    # INPUT
    queue.append(10)
    queue.append(20)
    queue.append(30)

    print("QUEUE :", queue)

    # OUTPUT : 가장 앞의 객체를 인출
    print("POP(0) :", queue.pop(0))
    print("POP(0) :", queue.pop(0))
    print("POP(0) :", queue.pop(0))
    print("QUEUE :", queue)


def loop():
    """
    리스트의 반복
    :return:
    """
    words = "Life is too short, You need Python".replace(",", "").split()
    print("WORDS :", words)

    # for 객체 in 순차형
    for word in words:
        print(word)

if __name__ == "__main__":
    #define_list()
    #list_oper()
    #list_methods()
    #stack_ex()
    #queue_ex()
    loop()