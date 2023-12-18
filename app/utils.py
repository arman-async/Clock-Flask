from datetime import datetime
import pytz


def TimeNow(_tz:str='Asia/Tehran')-> tuple[int, int, int] | None:
    
    try:
        now = datetime.now(
            tz=pytz.timezone(_tz))
    except pytz.exceptions.UnknownTimeZoneError:
        return None
    
    return now.hour, now.minute, now.second 

def DateNow():
    pass


if __name__ == '__main__':
    print(TimeNow())