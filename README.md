# projecteuler
Solutions to problems on projecteuler.net

## Styling
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)  
[Documentation](https://black.readthedocs.io/en/stable/index.html)
```
black --help
black {source_file_or_directory}
```

## Requirements
*recommend entering [virtual environment](#Manage-Environment) first*
```
pip install -r requirements.txt
```

## Virtual Environment

### Venv in Windows Subsystem for Linux
**Install**
```
sudo apt-get update
sudo apt-get install python3-venv
```
### Manage Environment
**Create**
```
python3 -m venv eulerenv
```

**Enter**
```
source eulerenv/bin/activate
```

**Exit**
```
deactivate
```

**Help**
```
python3 -h venv
```

## Run a problem
1. enter the problem directory
```
cd problems/[problem-folder]
```
2. run the problem.  
*all problems have main as the starting file.*
```
python main.py
```
*To time the programs on linux systems*
```
time python main.py
```

## Unit Test a problem
1. enter the problem directory
```
cd problems/[problem-folder]
```
2. test the functions of the problem
```
python -m unittest test
```
