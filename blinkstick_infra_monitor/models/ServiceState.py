from enum import Enum, unique

@unique
class ServiceState(Enum):
    NOT_RUNNING = 1     # The service hasn't started yet
    PENDING = 2         # The service is in progress (building/loading)
    WARNING = 3         # The service is running/completed but with errors
    ERROR = 4           # The service failed to run/complete
    RUNNING = 5         # The service is running/completed without errors
