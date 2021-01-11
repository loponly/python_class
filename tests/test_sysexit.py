import pytest


class TestClass:
    def test_one(self):
        x = 'this'
        assert 'h' in x


def f():
    raise ZeroDivisionError


def test_mytest():
    with pytest.raises(ZeroDivisionError):
        f()


def test_tmpfile(tmpdir):
    print(tmpdir)
    assert True
