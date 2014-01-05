
#supported content types for request and response
mime_types = {
    'other': ['', 'text/html', 'text/plain'],
    'xml': ['text/xml', 'application/xml'],
    'json': ['application/json']
}

supported_mimes = sum(mime_types.values(), [])


mysql = dict(
    user='root',
    pswd='',
    host='127.0.0.1',
    dbname='studygrow'
)

mysql_uri = "mysql://{user}:{pswd}@{host}/{dbname}".format(
    user=mysql['user'],
    pswd=mysql['pswd'],
    host=mysql['host'],
    dbname=mysql['dbname']
)
