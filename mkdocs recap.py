# https://towardsdatascience.com/full-guide-to-build-a-professionnal-portfolio-with-python-markdown-git-and-github-page-for-66d12f7859f0
# This is for the User-level Pages - see further down for the Project-level Pages

# conda install conda-forge::mkdocs
# conda install conda-forge::mkdocstrings
# conda install conda-forge::mkdocstrings-python
# conda install conda-forge::mypy

# Create the working folder - run in conda terminal:
# mkdocs new "pcava.github.io" # create the subfolder \pcava.github.io OR
# mkdocs new . # in case you have already created the pcava.github.io folder and are running this from within that folder

# Adjust the mkdocs.yml 

# To preview your website with live changes via local URL:
# mkdocs serve

# To create the html locally in the \site subfolder:
# mkdocs build

# Create a pcava/pcava.github.io repository in GitHub as per https://pages.github.com/

# When happy deploy:
# mkdocs gh-deploy

# and commit to pcava.github.io:
# git add .
# git commit -m "Create website"

# and push to GitHub:
# git push origin master



# https://realpython.com/python-project-documentation-with-mkdocs/#step-5-build-your-documentation-with-mkdocs
# This is for the Project-level Pages - see further up for the User-level Pages

# With MkDocs you can create different documentation pages (eg. tutorials, how-to guides, reference, and explanations) 
# along with auto-generated info from docstrings using mkdocstring

# test examples in docstrings using doctest in terminal:
# python -m doctest learnpy\mkdocs_calculations.py
# If you don’t see any output, then all tests passed!

# test type hints in functions using mypy in terminal:
# mypy learnpy\mkdocs_calculations.py
# If you don’t see any output, then all tests passed!

# to create the default MkDocs project structure run in terminal:
# mkdocs new .
# create a docs/ folder as well as the mkdocs.yml file

# to preview:
# mkdocs serve

# Use mkdocstrings to add docstring information from your code to MkDocs
# by adding these 2 lines to mkdocs.yml:
# plugins:
#   - mkdocstrings
# and the identifier ::: learnpy.mkdocs_calculations where you want to render all docstrings in that module
# or the identifier ::: learnpy where you want to render the package docstring

# when finalized you can build the html file within the /site/ folder typing:
# mkdocs build

# and finally deploy to GitHub directly using :
# mkdocs gh-deploy
# This command rebuilds the documentation from your Markdown files and source code 
# and pushes it to the gh-pages branch on your remote GitHub repository
# Remind to set gh-pages under Repository->Settings->Pages->Branch
# Final documentation available at https://pcava.github.io/LearnPy/

