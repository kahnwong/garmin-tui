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
