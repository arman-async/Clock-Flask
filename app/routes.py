from flask import render_template, abort, request
from .utils import TimeNow, DateNow
from main import app


@app.route('/')
def index():
    _tz = request.args.get('TZ', default='', type=str)
    time_now = TimeNow(_tz=_tz)
    date_now = DateNow()

    return render_template(
        template_name_or_list='index.html')


