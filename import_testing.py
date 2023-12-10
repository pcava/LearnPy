# Rel. vs Abs. Imports
# from . import config # does NOT work
# from config import PI, DEFAULT_DB_PATH # does NOT work
# from learnpy.config import PI, DEFAULT_DB_PATH # works
# import learnpy.config as config # works
# import config as config # does NOT work


# They all work fine
# import learnpy.calculations as calculations # works
# calculations.create_database()

# from learnpy.calculations import create_database # works
# create_database()

import learnpy.calculations as clc # works
clc.main()
