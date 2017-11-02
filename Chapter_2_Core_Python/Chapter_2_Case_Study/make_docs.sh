sphinx-quickstart  # accept all defaults except choose yes for automatically discovering docstrings
sphinx-apidoc -o . rate_table  # automatically generates the .rst documentation files from teh docstrings
make html  # actually generates the html documentation files.  Click on _build/index.html to verify
