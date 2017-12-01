
from blinkstick_infra_monitor.models.ServiceState import ServiceState

def mapStateToColour(state):
    if state == ServiceState.NOT_RUNNING:
        return "#d3d3d3"    # Grey
    elif state == ServiceState.PENDING:
        return "#5ee6ff"     # Blue
    elif state == ServiceState.WARNING:
        return "#ffe900"     # Yellow
    elif state == ServiceState.ERROR:
        return "#ff0000"     # Red
    elif state == ServiceState.RUNNING:
        return "#43ff00"     # Green
    print("Warning: Invalid state: {}".format(state))
    return "#000000"
