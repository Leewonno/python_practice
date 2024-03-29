# if문

money = True
if money:
    print("택시를 탄다")
else:
    print("걸어간다")


# and, or, not
# x and y
# x or y
# not x

a = True
if not a:
    print("큼")
else:
    print("작음")


# in, not in
# x in 리스트	x not in 리스트
# x in 튜플	    x not in 튜플
# x in 문자열	x not in 문자열
    
# 조건문에서 아무 일도 하지 않게 설정하고 싶다면?
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
    pass 
else:
    print("카드를 꺼내라")


# 조건부 표현식
score = 60

if score >= 60:
    message = "success"
else:
    message = "failure"

# ▼
message = "success" if score >= 60 else "failure"