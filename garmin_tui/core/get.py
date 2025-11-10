import datetime
from typing import Any

from garmin_tui.core import auth


class Garmin:
    def __init__(self):
        self.garmin = auth.init_api()  # type: ignore

        self.today = datetime.date.today()
        self.start_date = self.today - datetime.timedelta(days=7)  # past week
        self.date_all = [
            self.start_date + datetime.timedelta(days=x)
            for x in range((self.today - self.start_date).days + 1)
        ]

    def body_battery(self) -> list[dict[str, Any]]:
        data = self.garmin.get_body_battery(
            self.start_date.isoformat(), self.today.isoformat()
        )
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

    def sleep(self) -> list[dict[str, Any]]:
        r = []
        for date in self.date_all:
            r.append(self.garmin.get_sleep_data(date.isoformat()))

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

    def stress(self) -> list[dict[str, Any]]:
        r = []
        for date in self.date_all:
            r.append(self.garmin.get_stress_data(date.isoformat()))

        r_filtered = []
        for i in r:
            try:
                d = {
                    "date": i["calendarDate"],
                    "max": i["maxStressLevel"],
                    "avg": i["avgStressLevel"],
                }
                r_filtered.append(d)
            except KeyError:
                pass

        return r_filtered

    def resting_heart_rate(self) -> list[dict[str, Any]]:
        r = []
        for date in self.date_all:
            r.append(self.garmin.get_rhr_day(date.isoformat()))

        r_filtered = []
        for i in r:
            try:
                d = {
                    "date": i["statisticsStartDate"],
                    "restingHeartRate": i["allMetrics"]["metricsMap"][
                        "WELLNESS_RESTING_HEART_RATE"
                    ][0]["value"],
                }
                r_filtered.append(d)
            except KeyError:
                pass

        return r_filtered
