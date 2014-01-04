from studygrow_api.entry.resource import mod as entry
from studygrow_api.milestone.resource import mod as milestone
from studygrow_api.user.resource import mod as user


def init(app):
    app.register_blueprint(entry)
    app.register_blueprint(milestone)
    app.register_blueprint(user)
