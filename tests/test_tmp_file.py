import pytest


CONTENT = 'content'


def test_create_file(project_file):
    d = project_file

    p = d / "hello.txt"
    p.write_text(CONTENT)

    assert p.read_text() == CONTENT
    assert len(list(d.iterdir())) == 1


pytest.main(['tests/test_tmp_file.py'])
