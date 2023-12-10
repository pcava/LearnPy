"""This module implements custom calculations."""

# Imports go here...
import numpy as np
import sqlite3
from sqlite3 import Error

# Rel. vs Abs. Imports
# from . import config # works only when imported as a module, not run directly
# from config import PI, DEFAULT_DB_PATH # works only when used directly, not as a module
# from learnpy.config import PI, DEFAULT_DB_PATH # works only when imported as a module, not run directly
import learnpy.config as config # works only when imported as a module, not run directly
# import config as config # works only when used directly, not as a module

# can be run directly from terminal using the -m switch (run module as main)
# python -m learnpy.calculations

# Your custom calculations start here...
# def circular_land_area(radius):
#     return config.PI * radius**2

# def create_database(db_path = config.DEFAULT_DB_PATH):
#     # Code to create the initial database goes here...
#     print(db_path)

def main():
    # area = circular_land_area(2)
    # db = create_database()
    print(f"The pi value is : {config.PI}")

if __name__ == "__main__":
    main()