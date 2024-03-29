# while문

prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number: """

number = 0

while number != 4:
    print(prompt)
    number = int(input())


# while문 강제로 빠져나가기
# break
    

coffee = 10
while True:
    money = int(input("돈을 넣어주세요"))
    if money == 300:
        print("커피 제공")
        coffee -= 1
    elif money > 300:
        print("커피 제공, 거스름돈은 %d원 입니다." % (money - 300))
        coffee -= 1
    else:
        print("돈이 부족합니다.")
    
    if coffee == 0:
        print("커피가 떨어졌습니다. 판매 중지")
        break


# while 문의 맨 처음으로 돌아가기
# continue


# 무한루프
while True:
    print("Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.")

