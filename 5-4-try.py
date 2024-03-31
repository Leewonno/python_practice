try:
    4 / 0
except:
    print("error")
    pass
finally:
    print("중간에 오류가 발생해도 무조건 실행")

# raise 를 통해 에러를 발생시키기도함