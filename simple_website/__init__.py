import flask
import os


from simple_website.views import general

application = flask.Flask(__name__)
# application.debug = True
application.register_blueprint(general.mod)
