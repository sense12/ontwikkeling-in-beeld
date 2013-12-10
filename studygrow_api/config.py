
#supported content types for request and response
mime_types = {
    'other': ['', 'text/html', 'text/plain'],
    'xml': ['text/xml', 'application/xml'],
    'json': ['application/json']
}

supported_mimes = sum(mime_types.values(), [])
