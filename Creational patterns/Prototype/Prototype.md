# Prototype
Prototpye은 객체의 생성을 기존의 객체를 복사하여 생성하는 방식이다.

객체 생성의 복잡함을 간소화하고 유사한 객체를 만들때 비용을 줄일 수 있다.
## 깊은 복사 vs 얕은 복사
### 깊은 복사
깊은 복사는 객체의 모든 요소를 새로 만들어서 전달하는 방식이다.

모든 요소를 새로 만들어 전달하기에 완전히 다른 두 객체가 생긴다.
### 얕은 복사
얕은 복사는 객체의 요소를 가르키는 포인터를 전달하는 방식이다.

주소를 가르키기에 두 객체가 요소를 공유한다.
## 예제
### 코드
```py
from __future__ import annotations
from abc import ABC, abstractmethod

class Copyable():
    def copy(self) -> Copyable:
        pass

class Post(Copyable):
    def __init__(self, subject, content) -> None:
        self.subject = subject
        self.content = content
        self.comments:list[Comment] = []
    
    def copy(self) -> Post:
        proto = Post(self.subject, self.content)
        proto.comments = self.comments
        return proto
    
    def deepcopy(self) -> Post:
        proto = Post(self.subject, self.content)
        proto.comments = [comment.copy() for comment in self.comments]
        return proto
    
    def add_comment(self, comment: Comment):
        self.comments.append(comment)

    def del_comment(self, comment: Comment):
        self.comments.remove(comment)

    def print(self):
        print("=================")
        print(self.subject)
        print("-----------------")
        print(self.content)
        print("-----------------")
        for comment in self.comments:
            print(comment.content)
        print("=================")

class Comment(Copyable):
    def __init__(self, content) -> None:
        self.content = content

    def copy(self) -> Comment:
        proto = Comment(self.content)
        return proto
    
    
postA = Post("제목A", "내용")
comment1 = Comment("답글1")
comment2 = Comment("답글2")
postA.add_comment(comment1)
postA.add_comment(comment2)
postA.print()

postA_proto = postA.copy()
postA_proto.print()

postA.del_comment(comment2)
print("comment 2 삭제")

postA.print()
postA_proto.print()

print("####################")

postB = Post("제목A", "내용")
comment1 = Comment("답글1")
comment2 = Comment("답글2")
postB.add_comment(comment1)
postB.add_comment(comment2)
postB.print()

postB_proto = postB.deepcopy()
postB_proto.print()

postB.del_comment(comment2)
print("comment 2 삭제")

postB.print()
postB_proto.print()
```
### 결과
```
=================
제목A
-----------------
내용
-----------------
답글1
답글2
=================
=================
제목A
-----------------
내용
-----------------
답글1
답글2
=================
comment 2 삭제
=================
제목A
-----------------
내용
-----------------
답글1
=================
=================
제목A
-----------------
내용
-----------------
답글1
=================
####################
=================
제목A
-----------------
내용
-----------------
답글1
답글2
=================
=================
제목A
-----------------
내용
-----------------
답글1
답글2
=================
comment 2 삭제
=================
제목A
-----------------
내용
-----------------
답글1
=================
=================
제목A
-----------------
내용
-----------------
답글1
답글2
=================
```
postA는 얕은 복사를 하여 comment2를 삭제하였을때 proto도 같이 삭제되는 반면,<br>
postB는 깊은 복사를 하여 comment2를 삭제하여도 proto의 comment2가 삭제되지 않는다.
# 정리
Prototype 패턴을 사용하면 객체 생성의 복잡함을 간소화 하고,<br>
비슷한 객체의 생성 비용을 감소할 수 있다.

하지만 깊은 복사와 얕은 복사를 구분하여 사용하지 안으면,<br>
원본 객체와 복사된 객체간 의존이 발생 할 수 있으며,<br>
깊은 복사를 구현하는데에 많은 노력이 필요 할 수 있다.
# 참조
https://refactoring.guru/ko/design-patterns/prototype

https://shan0325.tistory.com/26

https://velog.io/@newtownboy/%EB%94%94%EC%9E%90%EC%9D%B8%ED%8C%A8%ED%84%B4-%ED%94%84%EB%A1%9C%ED%86%A0%ED%83%80%EC%9E%85%ED%8C%A8%ED%84%B4Prototype-Pattern