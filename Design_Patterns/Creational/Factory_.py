from abc import ABC, abstractmethod


class Transport(ABC):
    """
    The Product interface declares the operations that all concrete products
    must implement.
    """
    @abstractmethod
    def planDelivery(self) -> str:
        pass


class Logistics(ABC):
    """
    The Creator class declares the factory method that is supposed to return an
    object of a Product class. The Creator's subclasses usually provide the
    implementation of this method.
    """

    @abstractmethod
    def create_Transport(self) -> Transport:
        """
        Note that the Creator may also provide some default implementation of
        the factory method.
        """
        pass

    def deilver(self) -> str:
        """
        Also note that, despite its name, the Creator's primary responsibility
        is not creating products. Usually, it contains some core business logic
        that relies on Product objects, returned by the factory method.
        Subclasses can indirectly change that business logic by overriding the
        factory method and returning a different type of product from it.
        """

        transport = self.create_Transport()

        result = f"Creator: The same creator's code has just worked with {transport.planDelivery()}"

        return result


class ShipTransport(Transport):
    def planDelivery(self) -> str:
        return 'Delivering method is Ship'


class TruckTransport(Transport):
    def planDelivery(self) -> str:
        return 'Delivering method is Truck'


class SeaLogistic(Logistics):

    def create_Transport(self) -> Transport:
        return ShipTransport()


class RoadLogistic(Logistics):

    def create_Transport(self) -> Transport:
        return TruckTransport()


def client_code(creator):
    """
    The client code works with an instance of a concrete creator, albeit through
    its base interface. As long as the client keeps working with the creator via
    the base interface, you can pass it any creator's subclass.
    """

    print(f"App: Launched with the {type(creator).__name__}.")
    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f'{creator.deilver()}')

    print("\n")


if __name__ == "__main__":
    client_code(SeaLogistic())

    client_code(RoadLogistic())
