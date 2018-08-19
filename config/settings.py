from dotenv import load_dotenv

import os
import sys

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Read .env variables
RESOURCES_FOLDER = os.environ.get("RESOURCES_FOLDER")
DRIVER_FOLDER = os.environ.get("DRIVER_FOLDER")
DRIVER_NAME = os.environ.get("DRIVER_NAME")
CONNECTION_STRING = os.environ.get("CONNECTION_STRING")

# Project absolute path
PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

# Constants
CURRENT_OS = sys.platform if sys.platform not in ["win32", "cygwin"] else "win"
DRIVER_EXTENSION = ".exe" if "win" in CURRENT_OS else ""


class Settings(object):

    class Database(object):
        connection_string = CONNECTION_STRING

    class Selenium(object):
        driver = os.path.join(PROJECT_DIR, RESOURCES_FOLDER, DRIVER_FOLDER, CURRENT_OS, DRIVER_NAME + DRIVER_EXTENSION)
