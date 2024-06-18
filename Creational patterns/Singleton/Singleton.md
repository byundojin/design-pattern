# Singleton
Singleton은 class의 instance가 하나만 존재하게 하는 기법이다.

instance의 생성을 제한하여 공유 자원에 접근을 제어할 수 있다.
## 예시 
### 상황 설명
당신은 은행을 만들어야 합니다.<br>
은행의 돈은 모든 은행의 돈과 동일해야 합니다.

### 코드
```py
class SingletonMeta(type):
    # Metaclass 생성
    _instances = {}

    # __call__ 재정의
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
    
# metaclass를 SingletonMeta로 설정
class Bank(metaclass=SingletonMeta):
    def __init__(self) -> None:
        self.b:dict[str, int] = {}

    def 조회(self, name):
        if not name in self.b:
            print("등록되지 않은 사용자")
        else:
            print(f"{name}님의 통장 잔액 : {self.b[name]}")
    
    def 개설(self, name):
        if name in self.b:
            print("이미 등록된 사용자")
        else:
            self.b[name] = 0
            print(f"{name}님의 통장이 개설됨")

    def 입금(self, name, money):
        if not name in self.b:
            print("등록되지 않은 사용자")
        else:
            self.b[name] += money
            print(f"{money}원을 입금(현재 잔액) : {self.b[name]}")

    def 출금(self, name, money):
        if not name in self.b:
            print("등록되지 않은 사용자")
        else:
            if self.b[name] < money:
                print(f"잔액 부족(현재 잔액) : {self.b[name]}")
            else:
                self.b[name] -= money
                print(f"{money}원을 출금(현재 잔액) : {self.b[name]}")

print("-----------------------")
Bank().개설("dodo")
print("-----------------------")
Bank().입금("dodo", 10000)
print("-----------------------")
Bank().조회("dodo")
print("-----------------------")
Bank().출금("dodo", 5000)
print("-----------------------")
Bank().조회("dodo")
print("-----------------------")
```
### 결과

```
-----------------------
dodo님의 통장이 개설됨
-----------------------
10000원을 입금(현재 잔액) : 10000
-----------------------
dodo님의 통장 잔액 : 10000
-----------------------
5000원을 출금(현재 잔액) : 5000
-----------------------
dodo님의 통장 잔액 : 5000
-----------------------
```

쉬운 방법
### 코드
```py
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
```
### 결과
```
-----------------------
dodo님의 통장이 개설됨
-----------------------
10000원을 입금(현재 잔액) : 10000
-----------------------
dodo님의 통장 잔액 : 10000
-----------------------
5000원을 출금(현재 잔액) : 5000
-----------------------
dodo님의 통장 잔액 : 5000
-----------------------
```
## 정리
Singleton을 사용하여 객체를 쉽게 제어하길 바란다.
# 참조
#### Singleton
https://refactoring.guru/ko/design-patterns/singleton
#### metaclass
https://www.youtube.com/watch?v=NEpVvBGPhLU