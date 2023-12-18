from flask import render_template, abort, request
from .utils import TimeNow, DateNow
from main import app


@app.route('/')
def index():
    _tz = request.args.get('TZ', default='Asia/Tehran', type=str)
    time_now = TimeNow(_tz=_tz)
    date_now = DateNow()
    
    if not time_now:
        return abort(404)
    
    return render_template(
        template_name_or_list='index.html',
        time=time_now)


