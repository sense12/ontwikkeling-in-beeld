from flask import Blueprint, render_template

from studygrow_api import version

mod = Blueprint('entry', __name__, template_folder='views')
#the entry points only supports get as a purpose of documentation


@mod.route('/v' + version.get('mayor'))
def v1():
    return render_template("hello.xml")
