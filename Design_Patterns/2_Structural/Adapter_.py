import abc


class Client():

    """
    The Target defines the domain-specific interface used by the client code.
    """

    def __init__(self, data):
        self.data = data

    def get_data(self):
        return self.data


class Adaptee():
    """
    The Adaptee contains some useful behavior, but its interface is incompatible
    with the existing client code. The Adaptee needs some adaptation before the
    client code can use it.
    """

    def dict_to_list(self, dict_param):
        result = []
        for key, value in dict_param.items():
            result.append(key)
            result.append(value)
        return result


class Adapter(Adaptee):
    """
    The Adapter makes the Adaptee's interface compatible with the Target's
    interface via multiple inheritance.
    """

    def __init__(self, client):
        self.client = client

    def get_data(self):
        return Adaptee().dict_to_list(self.client.get_data())


if __name__ == "__main__":
    from pprint import pprint
    data = {'some': 'data'}

    client = Client(data)
    print('Data from client as dict:')
    pprint(client.get_data())

    print('Data from client as dict:')
    pprint(Adapter(client).get_data())
