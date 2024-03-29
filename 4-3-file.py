
# 파일 생성하기
# f = open("새파일.txt", 'w')
# f.close()

# 파일을 쓰기 모드로 열어 내용 쓰기
# f = open("새파일.txt", 'w')
# for i in range(1, 11):
#     data = "%d번째 줄입니다. \n" % i
#     f.write(data)
# f.close()


# 파일을 읽는 여러 가지 방법
# 1. readline 함수 이용하기
# 한 줄씩 읽어 출력

f = open("새파일.txt", 'r')
while True:
    line = f.readline()
    if not line : break
    print(line, end="")
f.close()

# 2. readlines 함수 사용하기
f = open("새파일.txt", 'r')
lines = f.readlines()
print(lines) # 리스트로 들어있다.
for line in lines:
    print(line)
f.close()

# 줄바꿈(\n) 문자를 제거하고 싶다면, line.strip() 을 이용한다.

# 3. read 함수 사용하기
# 파일 내용 전체를 문자열로 리턴
f = open("새파일.txt", 'r')
data = f.read()
print(data)
f.close()

# 4. 파일 객체를 for 문과 함께 사용하기
f = open("새파일.txt", 'r')
for line in f:
    print(line)
f.close()


# 파일에 새로운 내용 추가하기
f = open("새파일.txt",'a')
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()


# with문
# with문을 사용하면, 자동으로 파일을 닫아준다.
with open("foo.txt", "w") as f:
    f.write("Life is too short, you need python")

