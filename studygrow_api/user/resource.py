from flask import Blueprint, render_template

from studygrow_api import version

api_version = '/v' + version.get('mayor')
mod = Blueprint('user', __name__, url_prefix=api_version, template_folder='views')


@mod.route('/user')
def resource():
    return render_template("user.xml")
