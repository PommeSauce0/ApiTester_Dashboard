import json
from . import app
from bson import json_util
from datetime import datetime


# Global functions
@app.template_global('json_stringify')
def json_stringify(jsonstr):
    return json_util.dumps(jsonstr, indent=4, ensure_ascii=True)


# Filter functions
@app.template_filter('from_timestamp')
def from_timestamp(timestamp):
    return datetime.fromtimestamp(timestamp)
