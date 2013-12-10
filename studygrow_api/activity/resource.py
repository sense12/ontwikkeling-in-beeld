from flask import Blueprint, Response, request, url_for, abort, render_template

from studygrow_api.activity.model import Activity
from studygrow_api import version

api_version = '/v{0}'.format(version.get('mayor'))
mod = Blueprint('activity', __name__, url_prefix= api_version + '/user/<username>', template_folder='views')


@mod.route('/activity', methods=['GET', 'POST'])
def resource(username):
    if request.method == 'POST':
        abort(501)

    a = Activity().find(100)
    a.set_url(url_for('activity.activity_resource', username=username, activityid=a.id))
    return render_template("activity.xml", item=a)


@mod.route('/activity/<activityid>', methods=['GET', 'HEAD', 'PUT', 'DELETE'])
# always returns 200 (Ok) in successfull cases
def activity_resource(username, activityid):
    a = Activity().find(activityid)
    a.set_url(url_for('activity.activity_resource', username=username, activityid=a.id))

    if request.method == 'GET' or request.method == 'HEAD':
        if a.found is False:
            abort(404)

        body = render_template("activity.xml", item=a)
        return body, 200

    elif request.method == 'PUT':
        #TODO
        abort(501)

    elif request.method == 'DELETE':
        return '', 204  # no content, anymore ;)

    else:
        abort(405)
