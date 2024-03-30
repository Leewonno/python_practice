# 클래스
# 과자틀 = 클래스 / 과자 = 객체

# 사칙연산 클래스
class Calculation:
    
    # 메서드의 첫 번째 매개변수 self에는 setdata 메서드를 호출한 객체가 자동으로 전달
    # 파이썬 메서드의 첫 번째 매개변수 이름은 관례적으로 self를 사용한다.
    # 생성자
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b
    
    def mul(self):
        return self.a * self.b
    
    def sub(self):
        return self.a - self.b
    
    def div(self):
        return self.a / self.b
    

a = Calculation(1 , 2)
print(a.a)

b = Calculation(2, 3)
print(b.a)

# 클래스로 만든 객체의 객체변수는 다른 객체의 객체변수에 상관없이 독립적인 값을 유지



# 상속
class MoreCalculation(Calculation):
    def pow(self):
        return self.a ** self.b

c = MoreCalculation(2, 5)
print(c.add())
print(c.pow())


# 메소드 오버라이딩
# 부모 클래스(상속한 클래스)에 있는 메서드를 동일한 이름으로 다시 만드는 것
class SafeCalculation(Calculation):
    def div(self):
        if self.b == 0:
            return 0
        else:
            return self.a / self.b

s = SafeCalculation(1, 0)
print(s.div())


# 클래스 변수
# 같은 클래스로 만든 객체의 lastname 값도 모두 변경된다
class Family:
    lastname = "이"

d = Family()
e = Family()

print(d.lastname)
print(e.lastname)

Family.lastname = "박"

print(d.lastname)
print(e.lastname)

# 객체변수 생성
d.lastname = "이"

print(d.lastname)
print(e.lastname)
