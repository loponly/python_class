import abc


class Button(abc.ABC):

    """
    Concret Button 
    """
    @abc.abstractmethod
    def render(self):
        pass


class WinButton(Button):

    def render(self):
        return 'This is button for windows.'


class MacButton(Button):
    def render(self):
        return 'This is button for mac.'


class TextBox(abc.ABC):
    """
    Concret TextBox
    """

    @abc.abstractmethod
    def draw(abc):
        pass


class WinTextBox(TextBox):

    def draw(self):
        return 'This is textbox for windows.'


class MacTextBox(TextBox):
    def draw(self):
        return 'This is textbox for mac.'


class GUI(abc.ABC):

    @abc.abstractmethod
    def createButton(self):
        pass

    @abc.abstractmethod
    def createTextBox(self):
        pass


class WinGUI(GUI):

    def createButton(self) -> Button:
        return WinButton()

    def createTextBox(self) -> TextBox:
        return WinTextBox()


class MacGUI(GUI):

    def createButton(self) -> Button:
        return MacButton()

    def createTextBox(self) -> TextBox:
        return MacTextBox()


class Application(object):
    def __init__(self, factory):

        self.factory = factory()
        print(f'Drawing the {type(self.factory).__name__}')
        self.textBox = self.factory.createTextBox()
        self.button = self.factory.createButton()

    def paint(self):
        print(self.button.render())
        print(self.textBox.draw())


if __name__ == "__main__":
    app = Application(WinGUI)
    app.paint()

    app = Application(MacGUI)
    app.paint()
