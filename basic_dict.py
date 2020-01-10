# 사전(dict)
# 매핑형, 변경 가능 자료
# 순서 없다 -> 인덱싱, 슬라이싱 모두 불가
# 길이(len), 포함 여부(in or not in)
# 사전의 기본적인 연산의 대상은 키의 목록(dict_keys)


def define_dict():
    """
    사전의 정의
    :return:
    """
    dct = dict() # 빈 사전
    print(dct, type(dct))

    # Literal을 이용한 생성
    dct = {"basketball" : 5, "baseball" : 9}

    # 새로운 키-값을 할당
    dct["soccer"] = 10 # 새 키가 만들어 진다
    # 사전의 키는 불변 자료형이어야 하며, 중복될 수 없기 때문에
    # 이미 있는 키에 새 데이터를 하당하면 내부 데이터가 변경
    print(dct)
    dct['soccer'] = 11 # 기존 키에 매핑된 데이터를 갱싱
    print(dct)

    # 길이의 확인
    print("Length of dct :", len(dct)) # key를 대상으로 확인

    # 포함 여부의 확인 : in, not in -> key기준
    print("baseball in dct?", "baseball" in dct)
    print("baseball in dct?", "baseball" in dct.keys()) # 위의 문장과 같음

    # 값의 검색
    print("10 in dct value?", 10 in dct.values()) # 검색 대상을 값으로 변경

    # 키의 목록, 값의 목록, 키-값 쌍튜플의 목록
    print("KEYS of dct :", dct.keys())
    print("VALUES of dct :", dct.values())
    print("ITEMS of dct :", dct.items()) # dict_items : (키, 값) 튜플의 리스트

    # 키워드 인자를 이용한 사전의 생성
    d1 = dict(key1="value1", key2="value2")
    print(d1, type(d1))

    # (키, 값) 튜플 리스트로 사전 생성
    d2 = dict([("key1", "value1"), ("key2", "value2")])
    print(d2, type(d2))

    # 키의 목록과 값의 목록이 별도록 있을 때
    keys = ("one", "two", "three", "four")
    values = (1, 2, 3, 4)
    # zip 객체로 키의 목록과 값의 목록을 하나로 묶어서 dict 전달

    print(zip(keys, values)) # zip 오브젝트
    print(zip(keys, values))  # zip 오브젝트

    d3 = dict(zip(keys, values))
    print(d3, type(d3))


def using_dict():
    """
    사전의 사용법
    :return:
    """
    phones = { "홍길동" : "010-1234-5678"
             , "장길산" : "010-1111-2222"
             , "임꺽정" : "010-3333-4444"}
    print(phones)

    # 키의 목록 : keys()
    keys = phones.keys()
    print("KEYS of phones : ", keys)
    # dict_keys는 순차 자료형이기 떄문에 List, set 변환 가능
    lst_keys = list(keys)
    # 길이, 연결, 반복, 인덱싱 슬라이싱 모두 가능
    # 값의 목록 : values()
    values = phones.values() # dict_values
    print("VALUES of phones :", values)
    # 키-값 튜플의 리스트
    items = phones.items() # dict_items
    print("ITEMS of phones :", items)

    # 새 요소의 추가
    phones["일지매"] = "010-7777-8888"
    print(phones)

    # 요소에 접근
    print("홍길동의 전화번호 :", phones["홍길동"])
    # 키에 없는 요소의 접근 -> KeyError
    if "고길동" in phones:
        print("고길동의 전화번호 :", phones["고길동"]) # 키에 없을 경우 에러 발생

    # 키에 없는 요소에 접근 : get
    print("고길동의 전화번호 :", phones.get("고길동")) # None은 자바의 null과 비슷
    # 키가 없을 때에도 기본값을 얻어오고자 하는 경우
    # 두 번째 인자는 기본값
    print("고길동의 전화번호 :", phones.get("고길동", "없는이름입니다?"))

    # 삭제 : 키를 이용 객체를 얻어온 이후 -> del
    del phones["홍길동"]
    print(phones)

    # pop : 값을 가져오면서 객체 삭제
    data = phones.pop("일지매")
    print(data)
    print(phones)

    # popitem : 키-값 튜플을 가져오고 삭제
    item = phones.popitem()
    print("item : key = {}, value = {}".format(item[0], item[1]))
    print(phones)


def loop():
    """
    사전의 순회
    :return:
    """
    phones = { "홍길동": "010-1234-5678"
             , "장길산": "010-1111-2222"
             , "임꺽정": "010-3333-4444"}
    print(phones)

    # 기본적인 반복
    for k in phones: # 키의 목록을 대상으로 한다.
        print("KEY = {} -> Values = {}".format(k, phones.get(k))) # 객체에 2번 접근(key 추출 후 다시 value추출) -> 비효율적인 방법

    # items() -> 키-값 튜플의 리스트
    for item in phones.items():
        print("{} -> {}".format(item[0], item[1]))

    # 튜플의 언패킹을 이용
    for key, value in phones.items():
        print("{} -> {}".format(key, value))


if __name__ == "__main__":
    #define_dict()
    #using_dict()
    loop()