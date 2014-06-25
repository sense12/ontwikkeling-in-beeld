from studygrow_api import config

from flask import Flask, jsonify, request, abort

import xml.parsers.expat as Expat
import xmltodict


class MyFlask(Flask):

    def process_response(self, response):
        exception_message = "Could not convert body to %s\norigal status_code: %r\noriginal data:\n%r"
        mime = request.headers['Content-Type']

        if response.status_code == 302:
            body = """
<redirect location="%s">
<message>You should be redirected automatically to target URL</message>
</redirect>
""" % response.headers.get('Location')
            response.data = body 

        # some browsers don't give an content type? so this is our default
        if mime in config.mime_types['other']:
            mime = 'application/xml'

        if mime in config.mime_types['json']:
            #don't replace the response object only modify
            try:
                resp = jsonify(xmltodict.parse(response.data))
                response.data = resp.data
            except Expat.ExpatError:
                #todo log or send an email..
                response.data = exception_message % ('JSON', response.status_code, response.data)
                response.status_code = 500

        if mime in config.mime_types['xml']:
            xmlparser = Expat.ParserCreate()
            try:
                xmlparser.Parse(response.data)
                response.data = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n" + response.data
            except Expat.ExpatError:
                #todo log or send an email..
                response.data = exception_message % ('XML', response.status_code, response.data)
                response.status_code = 500

        response.mimetype = mime + '; charset=utf8'
        return response
