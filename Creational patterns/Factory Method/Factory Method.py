from abc import ABC, abstractmethod

class Transportation(ABC):
    def __init__(self) -> None:
        super().__init__()
        print("Transportation 생성")

    @abstractmethod
    def transport(self, object):
        pass

class Truck(Transportation):
    def __init__(self) -> None:
        super().__init__()
        print("Truck 생성")

    def transport(self, object):
        print(f"Truck 운송 -> {object}")

class Ship(Transportation):
    def __init__(self) -> None:
        super().__init__()
        print("Ship 생성")

    def transport(self, object):
        print(f"Ship 운송 -> {object}")

class Airplane(Transportation):
    def __init__(self) -> None:
        super().__init__()
        print("Airplane 생성")

    def transport(self, object):
        print(f"Airplane 운송 -> {object}")

class TransportationCreator(ABC):

    @abstractmethod
    def create(self) -> Transportation:
        pass

    def transport(self, object):
        print("운송 준비")
        transportation = self.create()
        transportation.transport(object)
        print("운송 완료")

class TruckCreator(TransportationCreator):
    def create(self) -> Transportation:
        return Truck()

class ShipCreator(TransportationCreator):
    def create(self) -> Transportation:
        return Ship()
    
class AirplaneCreator(TransportationCreator):
    def create(self) -> Transportation:
        return Airplane()
    
def order_fruit(creator:TransportationCreator, fruit:str):
    print(f"{fruit} 주문")
    creator.transport("apple")


if __name__ == "__main__":
    orders = [("apple", "육지"), ("banana", "육지"), 
              ("apple", "바다"), ("banana", "바다"), 
              ("apple", "하늘"), ("banana", "하늘")]
    
    for fruit, address in orders:
        if address == "육지":
            order_fruit(TruckCreator(), fruit)
        elif address == "바다":
            order_fruit(ShipCreator(), fruit)
        elif address == "하늘":
            order_fruit(AirplaneCreator(), fruit)
        else:
            raise "지원하지 않는 주소"
        print("--------------------------------")