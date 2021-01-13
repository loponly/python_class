import os
import pytest
import Website1


@pytest.fixture(scope='session')
def smtp_connection():
    import smtplib

    smtp_connection = smtplib.SMTP('smtp.gmail.com', 587, timeout=5)
    yield smtp_connection
    print('tear down')
    smtp_connection.close()


@pytest.fixture
def fixt(request):
    marker = request.node.get_closest_marker('fixt_data')
    if marker is None:
        data = None
    else:
        data = marker.args[0]

    return data


def idfn(fixture_value):
    if fixture_value == 0:
        return 'Egg'
    else:
        return None


@pytest.fixture(params=[0, 1], ids=idfn)
def b(request):
    return request.param


@pytest.fixture
def cleandir():
    import os
    import tempfile
    import shutil

    old_cwd = os.getcwd()
    newpath = tempfile.mkdtemp()
    os.chdir(newpath)
    yield
    os.chdir(old_cwd)
    shutil.rmtree(newpath)


@pytest.fixture
def username():
    print('with our parameter')
    return 'username'


@pytest.fixture
def other_username(username):
    print('with parameter')
    return 'other-' + username


@pytest.fixture
def project_file(tmp_path):
    import shutil
    d = tmp_path / 'sub'
    d.mkdir()
    yield d

    shutil.rmtree(str(d))


with open(os.path.join(os.path.dirname(__file__), 'data.sql'), 'rb') as f:
    _data_sql = f.read().decode('utf8')


@pytest.fixture
def app():
    import tempfile
    db_fd, db_path = tempfile.mkstemp()

    app = Website1.create_app({
        'TESTING': True,
        'DATABASE': db_path,
    })

    with app.app_context():
        Website1.db.init_db()
        Website1.db.get_db().executescript(_data_sql)

    yield app
    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()
