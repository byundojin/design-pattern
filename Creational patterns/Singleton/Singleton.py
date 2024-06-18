class Bank():
    # Python의 Object와 달리 TypeObject는 하나만 생성된다.
    # 그것을 이용하여 TypeObject인 class를 instance처럼 사용하는 방법이다.

    b:dict[str, int] = {}

    def 조회(name):
        if not name in Bank.b:
            print("등록되지 않은 사용자")
        else:
            print(f"{name}님의 통장 잔액 : {Bank.b[name]}")
    
    def 개설(name):
        if name in Bank.b:
            print("이미 등록된 사용자")
        else:
            Bank.b[name] = 0
            print(f"{name}님의 통장이 개설됨")

    def 입금(name, money):
        if not name in Bank.b:
            print("등록되지 않은 사용자")
        else:
            Bank.b[name] += money
            print(f"{money}원을 입금(현재 잔액) : {Bank.b[name]}")

    def 출금(name, money):
        if not name in Bank.b:
            print("등록되지 않은 사용자")
        else:
            if Bank.b[name] < money:
                print(f"잔액 부족(현재 잔액) : {Bank.b[name]}")
            else:
                Bank.b[name] -= money
                print(f"{money}원을 출금(현재 잔액) : {Bank.b[name]}")

print("-----------------------")
Bank.개설("dodo")
print("-----------------------")
Bank.입금("dodo", 10000)
print("-----------------------")
Bank.조회("dodo")
print("-----------------------")
Bank.출금("dodo", 5000)
print("-----------------------")
Bank.조회("dodo")
print("-----------------------")
