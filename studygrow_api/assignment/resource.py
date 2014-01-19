from flask import Blueprint, render_template, request, abort

from studygrow_api import url_version
from studygrow_api import db

mod = Blueprint('assignment', __name__,
        url_prefix=url_version + '/course/<course_id>',
        template_folder='views')

from studygrow_api.course import Assignment

@mod.route('/assignment/<assignment_id>')
def collection(course_id, assignment_id):
    """
    foobar
    """
    abort(501)
