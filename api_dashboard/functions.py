from . import app
from datetime import datetime


@app.template_filter('from_timestamp')
def from_timestamp(timestamp):
    return datetime.fromtimestamp(timestamp)
