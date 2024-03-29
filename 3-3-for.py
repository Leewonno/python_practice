t_list = [1, 2, 3]

for i in t_list:
    print(i)

a = [(1,2), (3,4), (5,6)]
for (f, l) in a:
    print("plus" + str(f + l))


# for 문과 continue 문
#  continue 문을 만나면 for 문의 처음으로 돌아가게 된다.


# for 문과 함께 자주 사용하는 range 함수
    
add = 0
for i in range(1, 11): # 1 ~ 10
    add += i
print(add)


marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60: 
        continue
    print("%d번 학생 축하합니다. 합격입니다." % (number+1))


# 리스트 컴프리헨션 사용하기

a = [1, 2, 3, 4]
result = [num * 3 for num in a]
print(result)

# 짝수에만 3을 곱하여 담고 싶다면
result = [num * 3 for num in a if num % 2 == 0]
print(result)

# [표현식 for 항목 in 반복_가능_객체 if 조건문]