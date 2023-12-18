from flask import render_template, abort, request
from datetime import datetime
from .utils import TimeNow, DateNow, GetNameDay
from main import app

# Index Route
@app.route('/')
def index():
    # Get Time Zone
    _tz = request.args.get('TZ', default='Asia/Tehran', type=str)
    
    today= datetime.today()
    # Get Time 
    time_now = TimeNow(_tz=_tz)
    
    date_now = DateNow(year=today.year, 
                       month=today.month, today=today.day)
    # What day is today - ex. Monday
    name_day = GetNameDay(date_now['days'])

    # Invalid time zone
    if not time_now:
        return abort(404)
    
    return render_template(
        template_name_or_list='index.html',
        time=time_now, date=date_now, _day=today.day, _name_day=name_day)


