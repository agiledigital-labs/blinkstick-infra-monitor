# From: https://github.com/dbader/schedule/issues/69#issuecomment-310128995

import threading
import schedule
import time

class ScheduleThread(threading.Thread):
    def __init__(self, *pargs, **kwargs):
        super().__init__(*pargs, daemon=True, name="scheduler", **kwargs)

    def run(self):
        while True:
            schedule.run_pending()
            time.sleep(schedule.idle_seconds())

