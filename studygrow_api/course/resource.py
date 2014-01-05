from flask import Blueprint, render_template, request

from studygrow_api import version
from studygrow_api import db

api_version = '/v' + version.get('mayor')
mod = Blueprint('course', __name__,
                url_prefix=api_version, template_folder='views')

from studygrow_api.course import Course


@mod.route('/courses')
def collection():
    result = Course().query.all()
    return render_template("course.xml", courses=result)

@mod.route('/course/<uid>')
def resource(uid):
    return "<msg>hello world %s</msg>" % uid
