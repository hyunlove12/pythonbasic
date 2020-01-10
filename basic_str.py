# 문자열
# 시퀀스 자료형, 길이, 연결, 반복, 포함여부
# 인덱스, 슬라이싱
# 변경 불가 자료형 -> 내부자료는 변경할 수 없다.
def define_str():
    print("====문자열 생성 연습====")
    # 한 줄 문자열 쌍따옴표("), 홑따옴표(')
    s1 = "Hello Python"
    s2 = str(3.14159) # 타 타입을 문자열로 변환

    print(s1, "is", type(s1))
    print(s2, "is", type(s2))

    # \(역슬러시)는 문장이 끊나지 않았음을 알려준다
    # 여러 줄 문자열 : """, '''
    # """ -> 첫번째 줄 부터 시작하기 때문에 아무것도 적지 않으면 개행 문자로 인식된다.
    s3 = """\
    Life is too short, You need Python.
    파이썬을 쉬운 문법으로 널리 사용되고 있다. \
    이 문장은 여러 줄 문자열로 작성한 내용입니다.    
        """
    print(s3)

    """
    여러줄 문자열은 여러 줄 주석이 필요한 경우에도 사용
    함수 정의부 바로 아래 여러 줄 문자열로 도움말을 작성하면 help 명령어로 해당 함수의 사용법을 볼 수 있다. 
    docstring이라 한다.
    """

def string_oper():
    """
    문자열 연산 연습
    :return:
    """
    s1 = "First String"
    s2 = "Python"

    # 길이를 측정 : Len
    print(s1, "Length :", len(s1))
    # 인덱싱을 할 수 있다.
    print("INDEXING", s2[0], s2[1], s2[2], s2[3], s2[4], s2[5])
    # 역 인덱싱을 할 수 있다.
    print("INDEXING", s2[-6], s2[-5], s2[-4], s2[-3], s2[-2], s2[-1])

    # 불변 자료형이므로 내부 자료를 바꿀 수 었다.
    # s2[0] = 'p' # Error

    # 슬라이싱
    # [ 시작경계 : 끝 경계 : 간격 ]
    print(s2[1:4] == "yth")
    print(s2[-5:-2] == 'yth') # 역 인덱스를 이용한 슬라이싱

    print(s2[0:3] == "Pyt")
    print(s2[:3] == s2[0:3]) # 시작경계를 생략하면 처음부터
    print(s2[3:len(s2)] == "hon")
    print(s2[3:] == s2[3:len(s2)]) # 끝 경계를 생략하면 끝까지
    #print(s2[0:6])

    print(s2[:] == "Python") # 전체
    print(s2[::2] == "Pto") # 간격값의 재정의
    print(s2[::-1] == "nohtyP") # 간격값이 음수면 방향이 반대

    # 연결 + : 산술연산자가 아니다
    #print("python" + 3) # Error
    print("Hello" + " " + "Python") # 연산 기호

    # 반복 + 정수형
    print("Ha" * 5) # 5번 반복

    # 포함 여부 확인 : in, not in
    print("P is ins 2?", "P" in s2)
    print("r is not in s2?", "r" not in s2)


def search_methods():
    """
    문자열 검색 관련 메서드들
    :return:
    """
    s = "I Like Python, I Like Java"

    # 검색어의 개수 : count
    print("Count of Like : ", s.count("Like"))
    # 내부 검색어의 위치 확인 : find, index
    print("Find Like : ", s.find("Like")) # 첫번째 검색의 위치
    print("Find Like : ", s.find("Like", 3)) # 검색 범위의 제한
    print("Find LIke : ", s.find("Like", 18)) # 찾는 검색어가 없으면 -1

    # 역방향 검색 : rfind, rindex
    print("Reverse Find Like : ", s.rfind("Like")) # 결과 값은 정인덱스(역 인데스(음수)로 나오지 않는다)
    print("Reverse 2nd Find Like :", s.rfind("Like", 0, 17)) # 검색 범위 제한

    # index로 검색
    print("Index Like : ", s.index("Like"))
    # 검색어 범위 제한 등 다른 것들은 find와 동일
    # rindex는 rfind와 동일한 기능

    # Error방지를 위하여 in 검색 후 진행행
    if "JS" in s:
        print("Index JS :", s.index("JS")) # 없는 검색어의 index -> Error


def modify_replace_methods():
    """
    편집과 치환
    :return:
    """
    s = "    Alice and the Heart Queen   " # 좌우에 공백 문자
    print("LSTRIP : [", s.lstrip(), "]", sep="")  # 왼쪽 공백 제거
    print("RSTRIP : [", s.rstrip(), "]", sep="")  # 오른쪽 공백 제거
    print("STRIP : [", s.strip(), "]", sep="") # lstrip + rstrip

    s = "----ALICE and the Heart Queen----"
    # 공백 문자가 아닌 다른 문자를 strip
    print("STIRP -:[", s.strip("-"), "]", sep="") # 좌우의 - 문자를 제거

    s = "I Like Java"
    # 치환 : replace
    print("REPLACE Java -> Python : ", s.replace("Java", "Python"))

    # 원본 자체는 변경되지 않는다.
    print("ORIGINAL str : ", s)


def split_join_methods():
    """
    문자열의 분리와 결합
    :return:
    """
    s = "Ham and Cheese and Breads and Ketchup"
    # 구분자 and를 기준으로 문자열 분리
    ings = s.split(" and ") # split 기본 분리 문자는 공백문자
    print("Words : ", ings, type(ings))

    # s의 왼쪽 두 개 단어를 분리 -> and 2개를자른다는 의미인가?
    print("LSPLIT :", s.split(" and ", 2))
    # s의 오른쪽 두 개 단어를 분리
    print("RSPLIT :", s.rsplit(" and ", 2))

    # 합치기 : join -> 구분자가 먼저 나온다.
    print("재료 목록 :", ",".join(ings))

    lines = """\
JAVA Programming
Python Programming
HTML Coding
    """
    print("ORIGINAL :", lines)

    print("SPLIT lines :", lines.split()) # 공백기준으로 split
    print("SPLITLINES lines :", lines.strip().splitlines())  # 공백 제거 후 개행문자 기준으로 split
    print("SPLITLINES lines :", lines.splitlines()) # 개행문자 기준으로 split


def string_format():
    """
    문자열 포매팅 연습
    :return:
    """
    # C 스타일의 문자열 포맷
    # %s, %c, %d, %f, %o. %x, %n, %%(%를 그자체 문자로 사용)
    fmt = "%d개의 %s 중에서 %d개를 먹었다"
    print(fmt % (10, "사과", 3)) # 문자열 포맷과 실제 데이터의 포맷 및 순서가 일치해야 한다.

    fmt2 = "현재 이자율은 %f%% 입니다." # %% -> % 글자 표시
    print(fmt2 % 1.24)
    fmt3 = "현재 이자율은 %.2f%% 입니다." # %.2f -> 소숫점 2째 자리가지 출력
    print(fmt3 % 1.24)

    # named formatting
    fmt4 = "%(total)d개의 %(item)s 중에서 %(eat)d개를 먹었다"
    # 데이터의 전달 순서는 중요하지 않다. 필요한 데이터는 모두 전달해 줘야 함
    print(fmt4 % {"total" : 10, "eat" : 5, "item" : "오렌지"})

    # format 메서드
    fmt5 = "{}개의 {} 중에서 {}개를 먹었다" # {} -> placeholder
    print(fmt5.format(10, "사과", 3))

    # named Placeholder
    fmt6 = "{total}개의 {item} 중에서 {eat}개를 먹었다."
    print(fmt6.format(item="배", eat=3, total=10))

    # 사전을 이용한 데이터의 포매팅 -> format_map 메서드
    print(fmt6.format_map({
         "total" : 5
        ,"item" : "키위"
        ,"eat" : 2
    }))



if __name__ == "__main__":
    #define_str()
    #string_oper()
    #search_methods()
    #modify_replace_methods()
    #split_join_methods()
    string_format()
