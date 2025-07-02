import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    ### Tells Flask to use the ProxyFix middleware
    # This is necessary if your app is behind a reverse proxy (like Nginx)
    # from werkzeug.middleware.proxy_fix import ProxyFixq

    # app.wsgi_app = ProxyFix(
    # app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
    # )

    ###
    # a simple page that says hello

    #2
    from . import db
    db.init_app(app)

    #3 
    from . import auth
    app.register_blueprint(auth.bp)

    #4 blog
    from . import blog
    app.register_blueprint(blog.bp)

    from . import routes
    app.register_blueprint(routes.bp)

    return app