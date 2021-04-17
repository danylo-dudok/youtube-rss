from datetime import datetime, timedelta, date, time
from typing import List


def localize_time(dt: datetime) -> datetime:
    from pytz import utc
    return dt.replace(tzinfo=utc)


def today() -> datetime:
    return datetime.combine(datetime.today().date(), time())


def str_to_date(s: str) -> datetime:
    s = s.lower()

    if s in ('today', 'now'):
        return localize_time(today())
    if s in ('yesterday', 'day', '1day'):
        return localize_time(today() - timedelta(days=1))
    if s == 'week':
        return localize_time(today() - timedelta(days=7))
    if s == 'month':
        return localize_time(today() - timedelta(days=30))
    if s.endswith('months'):
        amount = int(s.rstrip('months'))
        return localize_time(today() - timedelta(days=30 * amount))
    if s.endswith('days'):
        amount = int(s.rstrip('days'))
        return localize_time(today() - timedelta(days=amount))

    return localize_time(datetime.fromisoformat(s))


def read_argument(arguments: List[str], prefix: str):
    location = next((x for x in arguments if x.startswith(prefix)), None)
    return location.replace(prefix, '') if location else None


def serialize(obj: any) -> str:
    from json import dumps

    def default(o):
        if isinstance(o, (date, datetime)):
            return o.isoformat()

    return dumps(obj, default=default, ensure_ascii=False, indent=4)


def deserialize(json_str: str):
    from json import loads
    return loads(json_str)

