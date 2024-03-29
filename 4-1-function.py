# 매개변수 : 함수에 입력으로 전달된 값을 받는 '변수'
# 인수 : 함수를 호출할 때 전달하는 '입력값'

# 입력값이 몇 개가 될지 모를 때는 어떻게 해야 할까?

def add_many(*args):
    result = 0
    for i in args:
        result += i

    return result

print(add_many(1, 2, 3, 4, 5))


# 키워드 매개변수, kwargs

def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)
# 딕셔너리가 된다 {'a' : 1}

# 초깃값이 없는 매개변수(age)는
# 초깃값이 있는 매개변수(man) 뒤에 사용할 수 없다.
# (name, age, man=True) -> O
# (name, man=True, age) -> X

a = 1
def adding():
    # global을 붙여줘야 전역변수 사용이 가능하다.
    global a
    a += 1

adding() 
print(a)


# lambda 예약어
# lambda는 함수를 생성할 때 사용하는 예약어로, def와 동일한 역할을 한다.

sub = lambda a, b: a-b
result = sub(5, 2)
print(result)


