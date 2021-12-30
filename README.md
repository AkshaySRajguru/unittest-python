# unittest-python
## installation:
pip install pytest
pip install pytest-cov 

# Note: Rename test files as 'test_<filename>' in order to run below commands.

## pytest command:
pytest -v test_sample.py

### pytest code coverage command: 
### pytest --cov=<package (directory) or  module (file)> 
### below command runs the unit tests with code coverage tracking enabled for the <sample> module:
pytest --cov=sample

### to check lines of code that were not 
pytest --cov=sample --cov-report=term-missing
