from abc import ABC, abstractmethod

class AbstractStyle(ABC):
    @abstractmethod
    def get_style(self) -> str:
        pass

class ModernStyle(AbstractStyle):
    def get_style(self) -> str:
        return "세련된"
    
class AntiqueStyle(AbstractStyle):
    def get_style(self) -> str:
        return "고풍스러운"
    
class AbstractFurniture(ABC):
    def __init__(self, style:AbstractStyle) -> None:
        self.style:AbstractStyle = style
        self.furniture:str

    def introduce(self):
        return f"{self.style.get_style()} {self.furniture}"

class Chair(AbstractFurniture):
    def __init__(self, style: AbstractStyle) -> None:
        super().__init__(style)
        self.furniture = "의자"

    def sit(self):
        print(f"{self.introduce()}에 앉다")

class Table(AbstractFurniture):
    def __init__(self, style: AbstractStyle) -> None:
        super().__init__(style)
        self.furniture = "탁자"

    def put(self, object:str):
        print(f"{self.introduce()}에 {object}(를)을 놓는다.")

    def work(self, chair:Chair, object:str):
        chair.sit()
        self.put(object)
        print("일을 시작한다.")

class AbstractFactory(ABC):
    def __init__(self) -> None:
        self.style:AbstractStyle

    @abstractmethod
    def create_chair(self) -> Chair:
        pass

    @abstractmethod
    def create_table(self) -> Table:
        pass

    def work(self, name:str, object:str): # Factory Method와 같이 사용되었다.
        chair = self.create_chair()
        table = self.create_table()

        print(f"{name}(이)가 {object}(를)을 들고 온다.")
        table.work(chair=chair, object=object)


class ModernFactory(AbstractFactory):
    def __init__(self) -> None:
        self.style:AbstractStyle = ModernStyle()

    def create_chair(self) -> Chair:
        return Chair(self.style)

    def create_table(self) -> Table:
        return Table(self.style)

class AntiqueFactory(AbstractFactory):
    def __init__(self) -> None:
        self.style:AbstractStyle = AntiqueStyle()

    def create_chair(self) -> Chair:
        return Chair(self.style)

    def create_table(self) -> Table:
        return Table(self.style)

def work(factory:AbstractFactory, name:str, object:str):
    print("========================")
    factory.work(name, object)
    print(f"{name}(이)가 일을 끝냈다.")
    print("========================")

if __name__ == "__main__":
    work(ModernFactory(), "대호", "노트북")
    work(AntiqueFactory(), "세희", "볼팬과 노트")




