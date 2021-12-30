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
![image](https://user-images.githubusercontent.com/46608433/147778687-3a9797db-a3cd-4a0f-9637-7087960350d1.png)
 
after adding 'testNumber':
![image](https://user-images.githubusercontent.com/46608433/147779673-91954224-eee9-4927-8ec4-1b64f5ee6cd8.png)

The code coverage analysis can also be configured to treat lines with conditionals as needing double coverage to account for the two possible outcomes. 
This is called branch coverage and is enabled with the --cov-branch option:
![image](https://user-images.githubusercontent.com/46608433/147780090-efa38a67-dc90-422c-a0d4-39ab53b8b38b.png)
