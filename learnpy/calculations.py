"""This module implements custom calculations."""

# Imports go here...
import numpy as np
import sqlite3
from sqlite3 import Error

from . import config

# Your custom calculations start here...
def circular_land_area(radius):
    return config.PI * radius**2

def create_database(db_path = config.DEFAULT_DB_PATH):
    # Code to create the initial database goes here...
    print(db_path)

def main():
    area = circular_land_area(2)
    db = create_database()

if __name__ == "__main__":
    main() 