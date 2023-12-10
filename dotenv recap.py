# https://levelup.gitconnected.com/4-tools-to-add-to-your-python-project-before-shipping-to-production-c324f2fb8444
# https://pypi.org/project/python-dotenv/

# Install 
# conda install -c conda-forge python-dotenv

import os
from dotenv import load_dotenv

test = os.getenv("TEST")