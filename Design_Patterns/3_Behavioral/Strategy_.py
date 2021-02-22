import abc
from typing import List


class Strategy(abc.ABC):

    @abc.abstractmethod
    def execute(self, data: List):
        pass


class Context():

    def __init__(self, __strategy: Strategy = None):
        self.__strategy = __strategy

    @property
    def strategy(self):
        return self.__strategy

    @strategy.setter
    def strategy(self, __strategy: Strategy):
        self.__strategy = __strategy

    def do_something(self, data):

        print('='*10, type(self.__strategy), '='*10)
        print(list(self.strategy.execute(data)))


class ConcreteStrategyA(Strategy):

    def execute(self, data: List):
        return sorted(data)


class ConcreteStrategyB(Strategy):

    def execute(self, data: List):
        return reversed(sorted(data))


if __name__ == '__main__':

    context = Context()
    data = [5, 3, 2, 7, 9, 1, 2, 11]

    context.strategy = ConcreteStrategyA()
    context.do_something(data)

    context.strategy = ConcreteStrategyB()
    context.do_something(data)
