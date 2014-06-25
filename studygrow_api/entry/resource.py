from flask import Blueprint, render_template, request, url_for, redirect

from studygrow_api import url_version

mod = Blueprint('entry', __name__, template_folder='views')
#the entry points only supports get as a purpose of documentation


@mod.route(url_version)
def v1():
    return render_template("hello.xml")

@mod.route('/')
def root():
    return redirect('/api/v1')
