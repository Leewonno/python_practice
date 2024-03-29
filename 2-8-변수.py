a = [1, 2, 3]
b = a

print(id(a))
print(id(b))
# 이렇게 하면 동일한 객체를 가리킨다.
# = a를 변경하면, b도 변경된다.
print(a is b)

# 다른 주소를 가리키며 복사하기

# 1. [:] 이용하기

a = [1, 2, 3]
b = a[:]
a[1] = 4
print(a)
print(b)

# 2. copy 모듈 이용하기
from copy import copy
a = [1, 2, 3]
b = copy(a)
print(b is a) # False

# 리스트 자료형 자체함수 copy를 이용하는것도 가능하다.
a = [1, 2, 3]
b = a.copy()
print(b is a) # False


# 변수를 만드는 여러 가지 방법

# 튜플로 대입
# 튜플은 괄호 생략 가능
a, b = ('python', 'life')
(a, b) = 'python', 'life'

# 리스트를 변수로 만들기
[a, b] = ['python', 'life']

# 여러 개 변수에 같은 값 대입
a = b = 'python'

# 위 방법을 이용한 간단히 값 바꾸기
a = 1
b = 2
a, b = b, a
print(a)
print(b)