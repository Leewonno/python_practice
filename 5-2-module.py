import mod1
print(mod1.add(1, 1))

# 만약 모듈 이름 없이 함수만 쓰고 싶다면, 함수를 직접 import
from mod1 import sub
print(sub(2, 1))

# 만약 함수를 한번에 모두 import 하고 싶다면
from mod1 import *
print(add(2, 2))


# 클래스나 변수 등을 포함한 모듈
import mod2
a = mod2.Math()
print(a.solv(5))


# 다른 디렉토리에 있는 모듈 사용하기
# import sys
# sys.path.append("C:/doit/mymod")

# PYTHONPATH 환경 변수 사용하기
# set PYTHONPATH=C:\doit\mymod
# 맥이나 유닉스 환경에서는 set 대신 export 명령을 사용

