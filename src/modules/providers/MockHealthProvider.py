"""
BlickStick Infrastructure Monitor - Mock Health Provider

This provider is used for testing purposes
"""

import schedule
import random
from modules.models.ServiceState import ServiceState

SLOTS=12

class MockHealthProvider:

    current_status = {}
    job = None

    def updateMockState(self):
        slot = random.randrange(SLOTS)
        new_state = random.choice(list(ServiceState))
        self.current_status[slot] = new_state

    def start(self):
        self.tearDown()

        for i in range(SLOTS):
            self.current_status[i] = ServiceState.NOT_RUNNING

        self.job = schedule.every(5).seconds.do(self.updateMockState)

    def tearDown(self):
        if (self.job):
            schedule.cancel_job(self.job)
            self.job = None

    def getHealth(self):
        return self.current_status
