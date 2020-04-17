import os
# Base Url
BASE_PATH = "http://zzzscore.com/color/en/"

# Defines the if headless is enabled/disabled. default: False
HEADLESS = os.environ.get("HEADLESS", False)

# Drivers directory
DRIVERS_DIR = os.getcwd() + "/drivers"

# All possible drivers to be used
AVAILABLE_DRIVERS = dict({
    "chrome": DRIVERS_DIR + "/chromedriver",
    "firefox": DRIVERS_DIR + "/geckodriver"
})

# Environment driver if given. default: chrome
ENV_DRIVER = os.environ.get("DRIVER", "chrome")

# Driver path of the selected one
DRIVER_PATH = AVAILABLE_DRIVERS[ENV_DRIVER]