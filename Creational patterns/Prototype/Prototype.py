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