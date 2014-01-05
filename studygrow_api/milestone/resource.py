from flask import Blueprint, Response, request, url_for, abort, render_template

from studygrow_api.milestone.milestone_model import Milestone
from studygrow_api import version

api_version = '/v{0}'.format(version.get('mayor'))
mod = Blueprint('milestone', __name__,
                url_prefix=api_version + '/user/<user_id>',
                template_folder='views')


@mod.route('/milestone/<id>', methods=['GET'])
def resource(user_id, pkid):
    print '{"error": 405", "msg": "not implemented"}'
    abort(405)


@mod.route('/milestones', methods=['GET'])
def collection(user_id):
    Milestone.query.all()
    #a.url = url_for('milestone.milestone_resource', username=username, milestoneid=a.id)
    return render_template("milestone.xml", item=a)
