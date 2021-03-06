from flask import Flask
import os

from . import db
from . import auth
from .import blog


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'blog.db')
    )
    if test_config:
        app.config.from_mapping(test_config)

    db.init_app(app)

    app.register_blueprint(auth.bp)
    app.register_blueprint(blog.bp)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return 'Hello, World! '

    return app


# if __name__ == "__main__":
app = create_app()


# scp -r -i /Users/macbookpro/.ssh/website-security /Users/macbookpro/Documents/python_class/python_class/Website1 root@95.217.211.178:/var/www/Website1
