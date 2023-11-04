# Getting Started With Testing in Python - https://realpython.com/python-testing/

# install pytest
# pip install pytest

# testing script must always follow the rule
# tests/test_stack.py for testing the stack.py file

from learnpy.mysum import mysum

def test_sum():
    assert mysum([1, 2, 3]) == 6, "Should be 6"

def test_sum_tuple():
    assert mysum((1, 2, 2)) == 5, "Should be 5"
    
# to run a test from terminal
# python -m pytest -v

# or if want to see the coverage (amount of code run for performing the tests, ideally 100%)
# python -m pytest -v --cov

# or in vscode: https://pytest-with-eric.com/introduction/how-to-run-pytest-in-vscode/
# click on the Testing button on the left side 