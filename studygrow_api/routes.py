from studygrow_api.entry.resource import mod as entry
from studygrow_api.milestone.resource import mod as milestone
from studygrow_api.user.resource import mod as user
from studygrow_api.course.resource import mod as course


def init(app):
    app.register_blueprint(entry)
    app.register_blueprint(milestone)
    app.register_blueprint(user)
    app.register_blueprint(course)
