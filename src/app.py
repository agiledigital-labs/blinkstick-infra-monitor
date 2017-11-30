#!/usr/bin/env python3
"""
BlickStick Infrastructure Monitor
"""

__author__ = "Sean Dawson <spdawson@agiledigital.com.au"
__version__ = "0.1.0"
__license__ = "MIT"

import argparse
import time
from modules.providers.ApiHealthProvider import ApiHealthProvider
from modules.utils.ColourUtils import mapStateToColour
from blinkstick import blinkstick
from modules.utils.ScheduleThread import ScheduleThread

LED_COUNT=32

modules = []

def main(args):
    """ Main entry point of the app """
    print("BlinkStick Infrastructure Monitor")
    print(args)

    bstick = blinkstick.find_first()
    if bstick is None:
        print("Error: No BlinkStick devices found.")
        exit(1)
    bstick.set_led_count(LED_COUNT)

    mockHealthProvider = ApiHealthProvider(LED_COUNT)
    register(mockHealthProvider)

    ScheduleThread().start()

    print("Entering monitoring loop...")
    while True:
        status = mockHealthProvider.getHealth()
        print("Status: {}".format(status))
        for index in range(len(status)):
            state = status[index]
            colour = mapStateToColour(state)
            print("Setting channel {} to colour {}".format(index, colour))
            bstick.set_color(index=index, hex=colour)
            time.sleep(0.1)

        time.sleep(1)

def register(provider):
    provider.start()
    modules.append(provider)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser()

    # Required positional argument
    #parser.add_argument("arg", help="Required positional argument")

    # Optional argument flag which defaults to False
    parser.add_argument("-f", "--flag", action="store_true", default=False)

    # Optional argument which requires a parameter (eg. -d test)
    parser.add_argument("-n", "--name", action="store", dest="name")

    # Optional verbosity counter (eg. -v, -vv, -vvv, etc.)
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="Verbosity (-v, -vv, etc)")

    # Specify output of "--version"
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__))

    args = parser.parse_args()
    main(args)
