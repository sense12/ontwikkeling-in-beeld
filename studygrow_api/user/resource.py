from flask import Blueprint, render_template, request

from studygrow_api import version
from studygrow_api import db

api_version = '/v' + version.get('mayor')
mod = Blueprint('user', __name__, url_prefix=api_version, template_folder='views')

from studygrow_api.user import User


@mod.route('/users')
def collection():

    params = dict(request.args)

    if 'class' in params:
        user = User()
        results = user.get_by_class(params.get('class'))
    else:
        results = (User.query
                   .filter_by(is_student=True)
                   .all())

    return render_template("users.xml", users=results)


@mod.route('/user/<user_id>')
def resource(user_id):
    users = User().query.all()
    return render_template("users.xml", users=users)
