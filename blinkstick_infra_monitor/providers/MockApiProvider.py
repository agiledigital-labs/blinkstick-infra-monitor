"""
BlickStick Infrastructure Monitor - API Health Provider

This provider connects to the dedicated API server
"""

import schedule
import random
from modules.models.ServiceState import ServiceState
import requests

API_URL="http://localhost:3000/health_data"

class ApiHealthProvider:

    slot_count = 0
    current_status = []
    job = None

    def __init__(self, slot_count):
        self.slot_count = slot_count

    def updateMockState(self):
        body = requests.get(API_URL)
        self.current_status = [ServiceState[string_value] for string_value in body.json()["health_data"]]

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
