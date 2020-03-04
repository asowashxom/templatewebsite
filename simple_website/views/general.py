import flask

mod = flask.Blueprint('general', __name__)

@mod.route('/', methods=['GET'])
def Index():
    return flask.render_template('index.html', nav_item='home')
