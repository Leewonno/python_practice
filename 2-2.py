print("Hello World")
print('Python is fun')
print("""Life is too short, You need python""")
print('''Life is too short, You need python''')

# 문자열에 작은 따옴표 포함
food = "Python's favorite food is perl"

# 문자열에 큰 따옴표 포함
say = '"Python is very easy." he says.'

# 역슬래시 사용해 작은 따옴표, 큰 따옴표 포함하기
food = 'Python\'s favorite food is perl'
say = "\"Python is very easy.\" he says."

# 줄 바꾸기 위해 이스케이프 코드 \n 삽입하기
multiline = "Life is too short\nYou need python"

# 연속된 작은따옴표 3개 또는 큰따옴표 3개 사용하기
multiline='''
Life is too short
You need python2
'''
print(multiline)

# 문자열 연산하기
# 더하기
head = "Python"
tail = " is fun!"
sum = head + tail
print(sum)

# 곱하기
head = "python"
print (head * 2)


# 문자열 길이 구하기
a = "Life is too short"
print(len(a))

# 문자열 인덱싱
a = "Life is too short, You need Python"
print(a[3])
print(a[-2]) # 뒤에서부터 2번째 문자

# 문자열 슬라이싱 
print(a[0:4]) # 0 <= a < 4
print(a[1:])
print(a[:17])

# 문자열의 요솟값은 바꿀 수 없다
# a[1] = "y" -> 오류 발생
# Pithon 을 Python으로 바꾸려면
a = "Pithon"
print(a[:1] + "y" + a[2:])


# 문자열 포매팅
print("I eat %d apples" % 3)
print("I eat %s apples" % "five")
print("I ate %d appels. so I was sick for %s days" % (3, "three"))

# 포매팅 연산자 %d와 %를 같이 쓸 때는 %%를 쓴다
print('Error is %d%%.' % 98)

# 정렬과 공백
print("%10s" % "hi") # 전체 길이가 10인 문자열 공간에서 대입되는 값을 오른쪽 정렬하고 그 앞의 나머지는 공백으로 둬라
print("%-10sjane." % 'hi') # 전체길이는 10 + jane 의 길이, hi는 왼쪽 정렬하고 jane은 10개 이후에 출력해라

# 소수점 표현하기
print("%0.4f" % 3.42134234) # 소수점 4번째 자리까지만
print("%10.4f" % 3.42134234) # 전체길이가 10개인 공간에서 오른쪽 배치


# format 함수를 사용한 포매팅
print("I eat {0} apples, so I sick {1} days".format(3, 5))
print("I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3))
print("I ate {0} apples. so I was sick for {day} days.".format(10, day=3))
# 왼쪽정렬
print("{0:<10}".format("hi"))
# 오른쪽 정렬
print("{0:>10}".format("hi"))
# 가운데 정렬
print("{0:^10}".format("hi"))

#공백채우기
print("{0:=<10}".format("hi"))

#소수점 표현하기
print("{0:0.4f}".format(3.12134234))

# {또는} 문자 표현하기
print("{{ and }}".format())


# f 문자열 포매팅
name = '홍길동'
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age} 입니다.')
print(f'나의 이름은 {name}입니다. 나이는 {age + 1} 입니다.')

# 왼쪽 정렬
print(f'{"hi":<10}')
# 오른쪽 정렬
print(f'{"hi":>10}')
# 가운데 정렬
print(f'{"hi":=^10}')

# 소수점
print(f'{3.12345678:0.4f}')

print(f'{{ and }}')

# 문자 개수 세기
a = "hobby"
print(a.count('b')) # 문자열 a에 b가 몇개 있는지

# 문자 위치 알려주기
a = "Python is the best choice"
print(a.find('b'))
# 존재하지 않으면 -1
print(a.find("i")) # 여러개가 존재한다면, 가장 앞에 인덱스 리턴


# find는 존재하지 않으면 오류가 발생하지 않는다.
# index는 존재하지 않으면 오류를 발생시킨다.
print(a.index('t'))


#문자열 삽입
print(",".join('abcd'))
# join 함수는 문자열 뿐만 아니라 튜플, 리스트에도 사용 가능하다.
print(",".join(['a', 'b', 'c', 'd']))

# 소문자 -> 대문자
print("hi".upper())

# 대문자 -> 소문자
print("HI".lower())

# 왼쪽 공백 지우기
print(" hi ".lstrip())
# 오른쪽 공백 지우기
print(" hi ".rstrip())
# 양쪽 공백 지우기
print(" hi ".strip())


# 문자열 바꾸기
print("Life is too short".replace("Life", "Your leg"))

# 문자열 나누기
a = "Life is too short"
print(a.split(""))





