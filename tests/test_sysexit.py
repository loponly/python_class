import pytest
import os


class TestClass:
    def test_one(self):
        x = 'this'
        assert 'h' in x


def f():
    raise ZeroDivisionError


def test_mytest():
    with pytest.raises(ZeroDivisionError):
        f()


def f_3():
    return 3/0


def test_f_3():
    assert 4 % 2 == 0, "value was odd,should be even"


def test_tmpfile(tmpdir):
    print(tmpdir)
    assert True


def value_error():
    raise ValueError('Exception 123 raised')


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        f_3()


def test_match():
    with pytest.raises(ValueError, match=r'.* 123 .*'):
        value_error()


def test_set_compaire():
    set1 = set('8531')
    set2 = set('8135')
    assert set1 == set2


class Foo():
    def __init__(self, val):
        self.val = val

    def __eq__(self, other):
        return self.val == other.val


def pytest_assertrepr_compare(config, op, left, right):
    if isinstance(left, Foo) and isinstance(right, Foo) and op == '==':
        return [
            "Comparing Foo instances:", f"vals: {left.val}!={right.val}"
        ]


def test_compare():
    f1 = Foo(1)
    f2 = Foo(2)
    assert f1 == f1


# def test_eclo(smtp_connection):
#     respose, msg = smtp_connection.ehlo()
#     assert respose == 250
#     assert b"smtp.gmail.com" in msg

# @pytest.mark.fixt_data(42)
# def test_fixt(fixt):
#     assert fixt == 42


def test_b(b):
    print(b)
    # assert 0


@pytest.mark.usefixtures("cleandir")
class TestDirectoryInit:
    def test_cwd_starts_empty(self):
        assert os.listdir(os.getcwd()) == []
        with open("myfile", "w") as f:
            f.write("hello")

    def test_cwd_again_starts_empty(self):
        assert os.listdir(os.getcwd()) == []


@pytest.mark.parametrize('username', ['directly-overridden-username'])
def test_username(username):
    assert username == 'directly-overridden-username'


@pytest.mark.parametrize('username', ['directly-overridden-username-other'])
def test_username_other(other_username):
    assert other_username == 'other-directly-overridden-username-other'


pytest.main()
