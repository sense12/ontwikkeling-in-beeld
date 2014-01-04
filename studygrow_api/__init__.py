__version__ = '1.0.1'

version = dict(zip(['mayor', 'minor', 'patch'], __version__.split('.')))


# THESE MUST BE EASY TO IMPORT BECAUSE THEY ARE STATIC

from flask import Flask
from studygrow_api.lib import MyFlask
from flask.ext.sqlalchemy import SQLAlchemy

app = MyFlask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = config.mysql_uri

# register DB
db = SQLAlchemy(app)

import MySQLdb

def db_cursor():
    db = MySQLdb.connect(host=config.mysql['host'], user=config.mysql['user'],
                    passwd=config.mysql['pswd'], db=config.mysql['dbname'])
    return db.cursor()
