# 딕셔너리는 키와 값을 가지고 있다.
# 중괄호{}에 데이터를 넣는다.

# 쌍 추가

a = {1:'a'}
a[2] = 'b'
a['name'] = 'c'
print(a)

# 딕셔너리 요소 삭제하기
del a['name']
print(a)

# 딕셔너리에서 Key를 사용해 Value 얻기
print(a[1])

# 주의사항
# Key는 고유한 값이므로 중복되는 Key 값을 설정해 놓으면
# 하나를 제외한 나머지 것들이 모두 무시된다
# Key에 리스트는 사용할 수 없다.
# 딕셔너리는 순서가 없다.


# 딕셔너리 관련 함수

# 1. Key 리스트 만들기 - keys

a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(a.keys())
# 단, 리스트 고유의 append, insert, pop, remove, sort 함수는 수행할 수 없다.
# 반복문으로 키를 출력해 이용

# dict_keys 객체를 리스트로 변환
print(list(a.keys()))


# 2. Value 리스트 만들기
print(a.values())
print(list(a.values()))

# 3. Key, Value 쌍 얻기 - items
print(a.items())

# 4. Key: Value 쌍 모두 지우기
a.clear()
print(a)


# 5. Key로 Value 얻기 - get
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(a.get('name'))
print(a.get('phone'))

# 6. 해당 Key가 딕셔너리 안에 있는지 조사하기 - in
print('name' in a)
print('nmixx' in a)