import datetime
from typing import Any

from garmin_tui.core import auth

# init
garmin = auth.init_api()  # type: ignore

# set params
today = datetime.date.today()
start_date = today - datetime.timedelta(days=7)  # past week
date_all = [
    start_date + datetime.timedelta(days=x)
    for x in range((today - start_date).days + 1)
]


def body_battery() -> list[dict[str, Any]]:
    data = garmin.get_body_battery(start_date.isoformat(), today.isoformat())
    r = []
    for i in data:
        r.append(
            {
                "date": i["date"],
                "charged": i["charged"],
                "drained": i["drained"],
            }
        )
    return r


def sleep() -> list[dict[str, Any]]:
    r = []
    for date in date_all:
        r.append(garmin.get_sleep_data(date.isoformat()))

    r_filtered = []
    for i in r:
        try:
            d = {
                "date": i["dailySleepDTO"]["calendarDate"],
                "deep": i["dailySleepDTO"]["deepSleepSeconds"],
                "light": i["dailySleepDTO"]["lightSleepSeconds"],
                "rem": i["dailySleepDTO"]["remSleepSeconds"],
                "awake": i["dailySleepDTO"]["awakeSleepSeconds"],
            }
            r_filtered.append(d)
        except KeyError:
            pass

    return r_filtered
