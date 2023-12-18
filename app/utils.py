import calendar
import datetime
import pytz


def TimeNow(_tz:str='Asia/Tehran')-> list[int, int, int] | None:
    
    try:
        now = datetime.now(
            tz=pytz.timezone(_tz))
    except pytz.exceptions.UnknownTimeZoneError:
        return None
    
    # Add a zero before the number - 5 -> 05
    _temp = map(lambda n: f'0{n}' if len(str(n)) == 1  else f'{n}',
                (now.hour, now.minute, now.second ))
    return [t for t in _temp]



def DateNow(year:int=datetime.date.today().year,
        month:int= datetime.date.today().month,
        today:int=datetime.date.today().day ) -> dict[any]:
    """
    return {
        'year' : year,
        'month': datetime.datetime.now().strftime('%B'), #ex. November
        'days': days # [(int,<False, None, True>), ....] 
                -> True->today, False->this month,  None->Last month | next month
    }
    """
    
    obj = calendar.Calendar()
    
    # If we are in the first month of the year
    if month-1 == 0:
        last_year = year - 1
        last_month = 12
    else :
        last_year = year
        last_month = month - 1

    last_month = [day for day in obj.itermonthdays(last_year, last_month) if not (day == 0)]
    now_month = [day for day in obj.itermonthdays(year, month)]


    # Get the previous number of days (before the start of the month)
    zero_dayes = 0
    for day in now_month:
        if day == 0 : zero_dayes += 1
        if day == 1 : break

    # Filling the days before the beginning of the month with the last days of the last month
    _index = 0
    for day in last_month[-zero_dayes:]:
        now_month[_index] = (day, None)
        _index += 1

    # Fill in the days of the next month, after the completion of this month
    now_month += [0 for i in range(42 - len(now_month))] 
    _day = 1
    for day in now_month:
        if day == 0 :
            now_month[now_month.index(day)] = (_day, None)
            _day += 1
    # Controlling the volume of days
    now_month = now_month[:42]

    days = now_month # Just for more readability of the code
    
    for day in days:
        if type(day) == int:
            if day == today:
                days[days.index(day)] = (day, True)
            else :
                days[days.index(day)] = (day, False)

    return {
        'year' : year,
        'month': datetime.datetime.now().strftime('%B'),
        'days': days
    }



if __name__ == '__main__':
    print(TimeNow())
    print(DateNow())