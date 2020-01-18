# projecteuler
Solutions to problems on projecteuler.net

## Requirments
*recommend entering [virtual environment](#Manage-Environment) first*
```
pip install -r requirements.txt
```

## Styling
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) 
[Documentation](https://black.readthedocs.io/en/stable/index.html)
```
black --help
black {source_file_or_directory}
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
deactive
```

**Help**
```
python3 -h venv
```