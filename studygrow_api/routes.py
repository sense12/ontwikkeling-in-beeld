from studygrow_api.entry.resource import mod as entry
from studygrow_api.activity.resource import mod as activity
from studygrow_api.user.resource import mod as user


def init(app):
    app.register_blueprint(entry)
    app.register_blueprint(activity)
    app.register_blueprint(user)
