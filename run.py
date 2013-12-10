import os
from flask import Flask, jsonify, request, abort

from studygrow_api import config
from studygrow_api.lib import MyFlask
from studygrow_api import routes

# use the name application so it will work with beanstalk
application = MyFlask(__name__) 
app = application


def main():
	port = int(os.environ.get('PORT', 8000))
	app.run(debug=True, host='0.0.0.0', port=port)


# TBD move all this hook methos to a bootstrap file
error_xml = """
<error>
    <message>%s</message>
</error>"""

@app.before_request
def before_request():
    mime = request.headers['Content-Type']
    if mime not in config.supported_mimes:
        abort(415)


@app.errorhandler(404)
def not_found(error=None):
    return error_xml % ('Resource not found: ' + request.url), 404


@app.errorhandler(415)
def not_supported(error=None):
    mime = request.headers['Content-Type']
    return error_xml % ('Unsupported mime type: ' + mime), 415


@app.errorhandler(405)
def not_allowed(error=None):
    return error_xml % 'Method not allowed', 405


@app.errorhandler(500)
def server_error(error=None):
    return error_xml % 'The server encountered an internal error. Please retry the request', 500

@app.errorhandler(501)
def not_implemented(error=None):
    return error_xml % 'Not Implemented (yet). Please contact the developer stefano@tomato.com', 500

routes.init(app)

if __name__ == '__main__':
    main()
