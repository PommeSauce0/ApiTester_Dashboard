import json
from . import app
from bson import json_util
from datetime import datetime


# Global functions
@app.template_global('count_error_types')
def count_error_types(errors):
    error_types = dict()
    for error in errors:
        try:
            error_types[error.split(':', 1)[0]] += 1
        except KeyError:
            error_types[error.split(':', 1)[0]] = 1

    return error_types


# Filter functions
@app.template_filter('from_timestamp')
def from_timestamp(timestamp):
    return datetime.fromtimestamp(timestamp)


@app.template_filter('json_stringify')
def json_stringify(jsonstr):
    return json_util.dumps(jsonstr, indent=4, ensure_ascii=True)
