import abc


class IElectronicDevice(abc.ABC):
    '''
    Receiver interface method
    '''

    @abc.abstractmethod
    def volume(self):
        pass

    @abc.abstractmethod
    def name(self):
        pass


class TVDevice(IElectronicDevice):
    volume = 0
    name = ''

    def __init__(self, name):
        self.name = name
        self.volume = 0

    def turn_on(self):
        print(f'{self.name} is ON')

    def turn_off(self):
        print(f'{self.name} is OFF')

    def volume_down(self):
        if self.volume > 0:
            self.volume -= 1
        print(f'{self.name} is Volume down Volume: {self.volume}')

    def volume_up(self):
        self.volume += 1
        print(f'{self.name} is Volume up Volume: {self.volume}')


class MobileDevice(IElectronicDevice):
    volume = 0
    name = ''

    def __init__(self, name, model):
        self.model = model
        self.name = name
        self.volume = 0

    def switch_on(self):
        print(f'{self.name} with model {self.model} is ON')

    def switch_off(self):
        print(f'{self.name} with model {self.model} is OFF')

    def sound_down(self):
        if self.volume > 10:
            self.volume -= 10
        print(
            f'{self.name} with model {self.model} is Volume down, Volume: {self.volume}')

    def sound_up(self):
        self.volume += 10
        print(
            f'{self.name} with model {self.model} is Volume up, Volume: {self.volume}')


class IAdapaterReicever(abc.ABC):

    def __init__(self, Device: IElectronicDevice):
        self.Device = Device

    @abc.abstractmethod
    def on():
        pass

    @abc.abstractmethod
    def off():
        pass

    @abc.abstractmethod
    def down():
        pass

    @abc.abstractmethod
    def up():
        pass


class TVAdapaterReicever(IAdapaterReicever):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def on(self):
        self.Device.turn_on()

    def off(self):
        self.Device.turn_off()

    def down(self):
        self.Device.volume_down()

    def up(self):
        self.Device.volume_up()


class MobileAdapaterReicever(IAdapaterReicever):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def on(self):
        self.Device.switch_on()

    def off(self):
        self.Device.switch_off()

    def down(self):
        self.Device.sound_down()

    def up(self):
        self.Device.sound_up()


class ICommand(abc.ABC):
    '''
    Comand Interface
    '''

    def __init__(self, Receiver: IAdapaterReicever):
        self.Receiver = Receiver

    @abc.abstractmethod
    def execute(self):
        pass

    @abc.abstractmethod
    def undo(self):
        pass


class OnCommand(ICommand):
    '''
    On command class
    '''
    def __init__(sefl, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def execute(self):
        self.Receiver.on()

    def undo(self):
        self.Receiver.off()


class OffCommand(ICommand):
    '''
    On command class
    '''
    def __init__(sefl, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def execute(self):
        self.Receiver.off()

    def undo(self):
        self.Receiver.on()


class UpCommand(ICommand):
    '''
    On command class
    '''
    def __init__(sefl, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def execute(self):
        self.Receiver.up()

    def undo(self):
        self.Receiver.down()


class DownCommand(ICommand):
    '''
    On command class
    '''
    def __init__(sefl, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def execute(self):
        self.Receiver.down()

    def undo(self):
        self.Receiver.up()


class Invoker():

    def __init__(self,
                 Adapter: IAdapaterReicever):

        self.__history = []
        self.Receiver = Adapter

    def press(self, Command: ICommand):

        command = Command(self.Receiver)
        self.__history.append(command)
        command.execute()

    def undo(self):
        if len(self.__history) == 0:
            return False

        command = self.__history.pop()
        command.undo()

    def undoAll(self):
        self.__history.reverse()
        for command in self.__history:
            command.undo()

        self.__history = []


if __name__ == '__main__':

    print('='*39)
    sonyTV = Invoker(TVAdapaterReicever(TVDevice('Sony')))

    sonyTV.press(OnCommand)
    sonyTV.press(OffCommand)
    sonyTV.press(UpCommand)
    sonyTV.press(UpCommand)
    sonyTV.press(DownCommand)
    sonyTV.press(DownCommand)
    sonyTV.press(DownCommand)

    print('Undoing all the commands')
    sonyTV.undoAll()

    print('='*39)
    iphone = Invoker(MobileAdapaterReicever(MobileDevice('Iphone', 'X')))

    iphone.press(OnCommand)
    iphone.press(OffCommand)
    iphone.press(UpCommand)
    iphone.press(UpCommand)
    iphone.press(DownCommand)
    iphone.press(DownCommand)
    iphone.press(DownCommand)

    print('Undoing all the commands')
    iphone.undoAll()

    print('='*39)
