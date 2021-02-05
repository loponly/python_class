import abc


class ACollection():

    def __init__(self, data):
        if isinstance(data, list):
            self.data = data
            self.data.sort()
            self.end_iter = len(self.data)

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        self.__has_move__()
        d = self.data[self.__index]
        self.__index += 1
        return d

    def __has_move__(self):
        if self.__index == self.end_iter:
            raise StopIteration


if __name__ == '__main__':
    for d in ACollection(['k', 'c', 'a', 'b']):
        print(d)
