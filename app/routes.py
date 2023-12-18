from flask import render_template, abort, request
from datetime import datetime
from .utils import TimeNow, DateNow, GetNameDay
from main import app


@app.route('/')
def index():
    _tz = request.args.get('TZ', default='Asia/Tehran', type=str)
    today= datetime.today()
    time_now = TimeNow(_tz=_tz)
    date_now = DateNow(year=today.year, 
                       month=today.month, today=today.day)

    name_day = GetNameDay(date_now['days'])

    if not time_now:
        return abort(404)
    
    return render_template(
        template_name_or_list='index.html',
        time=time_now, date=date_now, _day=today.day, _name_day=name_day)


