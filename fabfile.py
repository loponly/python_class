from fabric.api import *

# the user to use for the remote commands
env.user = 'root'
# the servers where the commands are executed
env.hosts = ['95.217.211.178']
# pack file


def pack():
    # build the package
    local('python setup.py sdist --formats=gztar', capture=False)


def deploy():
    # figure out the package name and version
    dist = local('python setup.py --fullname', capture=True).strip()
    filename = '%s.tar.gz' % dist

    # upload the package to the temporary folder on the server
    put('dist/%s' % filename, '/tmp/%s' % filename)

    # install the package in the application's virtualenv with pip
    run('/var/www/yourapplication/env/bin/pip install /tmp/%s' % filename)

    # remove the uploaded package
    run('rm -r /tmp/%s' % filename)

    # touch the .wsgi file to trigger a reload in mod_wsgi
    run('touch /var/www/yourapplication.wsgi')


def connection_test():
    run('sudo apt-get install libapache2-mod-wsgi python-dev')
    run('sudo a2enmod wsgi')


def init_build():
    run('sudo apt-get install libapache2-mod-wsgi python-dev')
    run('sudo a2enmod wsgi')

    put('Website1', '/var/www/Website1')


def re_deploy():
    try:
        put('Website1', '/var/www/Website1')
        run('service apache2 restart')
        get('/var/log/apache2/error.log', 'log/error.log')
    except OSError:
        pass
