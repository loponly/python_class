from abc import ABC, abstractclassmethod


class BuilderQuery(ABC):

    def __init__(self):
        self.table = None
        self.fields = None
        self.filters = None

    @abstractclassmethod
    def set_table(self, table: object):
        pass

    @abstractclassmethod
    def set_fields(self, fields: list):
        pass

    @abstractclassmethod
    def set_filters(self, filters: dict):
        pass

    @abstractclassmethod
    def get_query(self) -> str:
        pass

    @staticmethod
    def wrap_string_with_quote(string):
        if isinstance(string, str):
            return f"'{string}'"
        return str(string)


class BuilderQueryMysql(BuilderQuery):

    def __init__(self):
        BuilderQuery.__init__(self)

    def set_table(self, table: object = None):
        if table is None:
            raise ValueError('Please enter your table!')
        self.table = table

    def set_fields(self, fields: list = None):
        if fields and isinstance(fields, list):
            self.fields = ','.join(fields)
            return
        self.fields = '*'

    def set_filters(self, filters: dict = None):
        if filters and isinstance(filters, dict):
            self.filters = 'WHERE '
            for k, v in filters.items():
                if isinstance(v, list):
                    self.filters += f"{k} IN "
                    self.filters += f"({','.join([self.wrap_string_with_quote(string) for string in v])})"
                elif isinstance(v, str):
                    self.filters += f"{k} = {self.wrap_string_with_quote(v)}"

            return
        self.filters = ''

    def get_query(self) -> str:
        return f"SELECT {self.fields} FROM {self.table} {self.filters} "


class BuilderQueryJSON(BuilderQuery):

    def __init__(self):
        BuilderQuery.__init__(self)

    def set_table(self, table: object = None):
        if table is None:
            raise ValueError('Please enter your table!')
        self.table = table

    def set_fields(self, fields: list = None):
        if fields is None or not isinstance(fields, list):
            raise ValueError('Please enter your fields!')

        self.fields = ''
        self.fields += ','.join(
            [f'row[{self.wrap_string_with_quote(v)}]' for v in fields])

    def set_filters(self, filters: dict = None):
        self.filters = ''
        i = 0
        if filters and isinstance(filters, dict):
            for k, v in filters.items():
                if i > 0:
                    self.filters += 'and '
                if isinstance(v, list):
                    self.filters += f"row[{self.wrap_string_with_quote(k)}] in "
                    self.filters += f"({','.join([self.wrap_string_with_quote(string) for string in v])})"
                elif isinstance(v, str):
                    self.filters += f"row[{self.wrap_string_with_quote(k)}] == {self.wrap_string_with_quote(v)}"
                i += 1
            return
        self.filters = 'True'

    def get_query(self) -> str:
        return {'for': self.table,
                'if': self.filters,
                'output': self.fields
                }


users = [
    {'firstname': 'John', 'age': '17'},
    {'firstname': 'John', 'age': '16'},
    {'firstname': 'Bob', 'age': '18'},
]


def queryBuild(builder: BuilderQuery):
    from pprint import pprint
    builder.set_table('users')
    builder.set_fields(['firstname', 'age'])
    builder.set_filters({'firstname': 'John', 'age': '17'})

    pprint(builder.get_query())


queryBuild(BuilderQueryMysql())
queryBuild(BuilderQueryJSON())
