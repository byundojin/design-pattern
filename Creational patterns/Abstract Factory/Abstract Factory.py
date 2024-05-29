from abc import ABC, abstractmethod

class AbstractChair(ABC):
    @abstractmethod
    def sit(self):
        pass

class Modernchair(AbstractChair):
    def sit(self):
        print("세련된 의자에 앉는다.")

class AntiqueChair(AbstractChair):
    def sit(self):
        print("고풍스러운 의자에 앉는다.")

class AbstractTable(ABC):
    @abstractmethod
    def put(self, object:str):
        pass

    def work(self, chair:AbstractChair, object:str): 
        chair.sit()
        self.put(object)
        print("일을 시작한다.")

class ModernTable(AbstractTable):
    def put(self, object: str):
        print(f"세련된 탁자에 {object}(를)을 놓는다.")

class AntiqueTable(AbstractTable):
    def put(self, object: str):
        print(f"세련된 탁자에 {object}(를)을 놓는다.")

class AbstractFactory(ABC):
    @abstractmethod
    def create_chair(self) -> AbstractChair:
        pass

    @abstractmethod
    def create_table(self) -> AbstractTable:
        pass

    def work(self, name:str, object:str): # Factory Method와 같이 사용되었다.
        chair = self.create_chair()
        table = self.create_table()

        print(f"{name}(이)가 {object}(를)을 들고 온다.")
        table.work(chair=chair, object=object)

class ModernFactory(AbstractFactory):
    def create_chair(self) -> AbstractChair:
        return Modernchair()
    
    def create_table(self) -> AbstractTable:
        return ModernTable()
    
class AntiqueFactory(AbstractFactory):
    def create_chair(self) -> AbstractChair:
        return AntiqueChair()
    
    def create_table(self) -> AbstractTable:
        return AntiqueTable()
    
def work(factory:AbstractFactory, name:str, object:str):
    print("========================")
    factory.work(name, object)
    print(f"{name}(이)가 일을 끝냈다.")
    print("========================")

if __name__ == "__main__":
    work(ModernFactory(), "대호", "노트북")
    work(AntiqueFactory(), "세희", "볼팬과 노트")