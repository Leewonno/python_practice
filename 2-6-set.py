# 집합
# 집합 자료형은 set 키워드를 이용해 만든다.

s1 = set([1, 2, 3])
print(s1)

s2 = set("Hello")
print(s2)

# 집합 자료형의 특징
# 1. 중복을 허용하지 않는다.
# 2. 순서가 없다(Unordered).

# 데이터의 중복을 제거하기 위한 필터로 종종 사용
# set 자료형에 저장된 값을 인덱싱으로 접근하려면
# 리스트나 튜플로 변환한 후에 해야 한다.

# 교집합, 합집합, 차집합 구하기

# 1. 교집합
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print(s1 & s2)
print(s1.intersection(s2)) # 위와 동일하다.

# 2. 합집합
print(s1 | s2)
print(s1.union(s2))

# 3. 차집합
print(s1 - s2)
print(s1.difference(s2))
print(s2 - s1)
print(s2.difference(s1))



# 집합 자료형 관련 함수

# 1. 값 1개 추가하기 - add
s1 = set([1, 2, 3])
s1.add(4)
print(s1)

# 2. 값 여러 개 추가하기 - update
s1 = set([1, 2, 3])
s1.update([4, 5, 6])
print(s1)

# 3. 특정 값 제거하기 - remove
s1 = set([1, 2, 3])
s1.remove(2)
print(s1)