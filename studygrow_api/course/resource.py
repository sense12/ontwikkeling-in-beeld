from flask import Blueprint, render_template, request

from studygrow_api import url_version
from studygrow_api import db

mod = Blueprint('course', __name__, url_prefix=url_version, template_folder='views')

from studygrow_api.course import Course
from studygrow_api.course import Assignment


@mod.route('/courses')
def collection():
    result = Course().query.all()
    return render_template("course.xml", courses=result)

@mod.route('/course/<course_id>')
def resource(course_id):
    result = Course().query.filter_by(uid=course_id).first()
    assignments = Assignment().query.filter_by(course_id=course_id).all()

    parents = {}
    for obj in assignments:
        if obj.parent_id is None:
            obj.childs = []
            parents[obj.uid] = obj
            continue  # ensure a parent doesn't have any parents

        if obj.parent_id in parents:
            parents[obj.parent_id].childs.append(obj)

    return render_template('detail.xml', course=result, assignments=parents.values())
