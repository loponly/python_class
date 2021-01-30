

class BaseA():
    def __init__(self, a, **kwargs):
        self.a = a


class BaseB():
    def __init__(self, b, **kwargs):
        self.b = b


class All(BaseA, BaseB):

    def __init__(self, a, b):
        BaseA.__init__(self, a)
        BaseB.__init__(self, b)


some = All(1, 2)
print(some.b)
