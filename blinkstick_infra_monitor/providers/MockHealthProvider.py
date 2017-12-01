"""
BlickStick Infrastructure Monitor - Mock Health Provider

This provider is used for testing purposes
"""

import schedule
import random
from models.ServiceState import ServiceState


class MockHealthProvider:

    slot_count = 0
    current_status = []
    job = None

    def __init__(self, slot_count):
        self.slot_count = slot_count

    def updateMockState(self):
        slot = random.randrange(self.slot_count)
        new_state = random.choice(list(ServiceState))
        self.current_status[slot] = new_state

    def start(self):
        self.tearDown()

        self.current_status = [ServiceState.NOT_RUNNING] * self.slot_count
        self.job = schedule.every(5).seconds.do(self.updateMockState)

    def tearDown(self):
        if (self.job):
            schedule.cancel_job(self.job)
            self.job = None

    def getHealth(self):
        return self.current_status
