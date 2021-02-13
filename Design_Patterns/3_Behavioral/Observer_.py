import abc
import typing


class IObserver(abc.ABC):

    @abc.abstractmethod
    def update(self):
        pass


class IObservable(abc.ABC):

    @abc.abstractmethod
    def subscribe(self, observer: IObserver):
        pass

    @abc.abstractmethod
    def unsubscribe(self, observer: IObserver):
        pass

    @abc.abstractmethod
    def notify(self, msg):
        pass


class Observable(IObservable):

    Observers: typing.List[IObserver] = list()

    def subscribe(self, observer: IObserver):
        self.Observers.append(observer)
        print(f'{observer} is subscribed')

    def unsubscribe(self, observer: IObserver):
        self.Observers.remove(observer)
        print(f'{observer} is unsubscribed')

    def notify(self, msg):
        for observer in self.Observers:
            observer.update(msg)


class AObserver(IObserver):

    def update(self, msg):
        print(f'{AObserver.__name__} got msg {msg}')

    def __str__(self):
        return AObserver.__name__


class BObserver(IObserver):

    def update(self, msg):
        print(f'{BObserver.__name__} got msg {msg}')

    def __str__(self):
        return BObserver.__name__


if __name__ == '__main__':
    observable = Observable()
    a = AObserver()
    observable.subscribe(a)

    observable.subscribe(BObserver())

    observable.notify('Hello')

    observable.unsubscribe(a)
