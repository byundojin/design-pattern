from __future__ import annotations
from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self) -> None:
        self.재료 = []
    
    def add_재료(self, 재료):
        self.재료.append(재료)

    @abstractmethod
    def 설명(self):
        pass

class 김밥(Product):
    def 설명(self):
        print(", ".join(self.재료)+"(를)을 말아 만든 김밥")

class 비빔밥(Product):
    def 설명(self):
        print(", ".join(self.재료)+"(를)을 비벼 만든 비빔밥")

class BuilderIterface(ABC):
    def __init__(self) -> None:
        self._product:Product|None = None

    @property
    @abstractmethod
    def product(self) -> Product:
        pass

    @abstractmethod
    def add_김(self) -> BuilderIterface:
        pass
    
    @abstractmethod
    def add_밥(self) -> BuilderIterface:
        pass

    @abstractmethod
    def add_당근(self) -> BuilderIterface:
        pass

    @abstractmethod
    def add_햄(self) -> BuilderIterface:
        pass

    @abstractmethod
    def create(self) -> Product:
        pass

class 김밥Builder(BuilderIterface):
    @property
    def product(self):
        if self._product:
            pass
        else:
            self._product = 김밥()
        return self._product
    
    def add_김(self):
        print("김을 깔아줍니다.")
        self.product.add_재료("김")
        return self

    def add_밥(self):
        print("밥을 깔아줍니다.")
        self.product.add_재료("밥")
        return self

    def add_당근(self):
        print("당근을 길게 썰어줍니다.")
        self.product.add_재료("당근")
        return self

    def add_햄(self):
        print("햄을 길게 썰어줍니다.")
        self.product.add_재료("햄")
        return self

    def create(self) -> product:
        print("잘 말아주면 김밥 완성.")
        return self.product
    
class 비빔밥Builder(BuilderIterface):
    @property
    def product(self):
        if self._product:
            pass
        else:
            self._product = 비빔밥()
        return self._product
    
    def add_김(self):
        print("김가루를 뿌려줍니다.")
        self.product.add_재료("김")
        return self

    def add_밥(self):
        print("밥을 넣습니다.")
        self.product.add_재료("밥")
        return self

    def add_당근(self):
        print("당근을 작게 썰어줍니다.")
        self.product.add_재료("당근")
        return self

    def add_햄(self):
        print("햄을 작게 썰어줍니다.")
        self.product.add_재료("햄")
        return self

    def create(self) -> product:
        print("잘 비벼주면 비빔밥 완성.")
        return self.product

def 햄세트(builder:BuilderIterface):
    return builder.add_김().add_밥().add_햄().create()

def 당근세트(builder:BuilderIterface):
    return builder.add_김().add_밥().add_햄().create()

if __name__ == "__main__":
    햄세트(김밥Builder()).설명()
    print("========================")
    햄세트(비빔밥Builder()).설명()
    print("========================")
    당근세트(김밥Builder()).설명()
    print("========================")
    당근세트(비빔밥Builder()).설명()