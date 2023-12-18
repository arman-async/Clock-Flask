from datetime import datetime
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


def DateNow():
    pass


if __name__ == '__main__':
    print(TimeNow())