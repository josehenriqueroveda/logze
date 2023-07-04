
# LOGZE

[![PyPI version fury.io](https://badge.fury.io/py/logze.svg)](https://pypi.python.org/pypi/logze/)
[![PyPI download month](https://img.shields.io/pypi/dm/logze.svg)](https://pypi.python.org/pypi/logze/)
![GitHub repo size](https://img.shields.io/github/repo-size/josehenriqueroveda/logze)
[![Percentage of issues still open](http://isitmaintained.com/badge/open/Naereen/badges.svg)](http://isitmaintained.com/project/logze/badges "Percentage of issues still open")
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
![GitHub top language](https://img.shields.io/github/languages/top/josehenriqueroveda/logze)


Library in Python to store logs in MongoDB and send notifications of errors to MS Teams.


## Install

Install **logze** using [PyPI](https://pypi.org/project/logze/) or directly via *pip*:

```bash
  pip install logze
```
    
## Usage

```python
from logze.recorder.logger import LogRecorder
from logze.models.log import Log


recorder = LogRecorder("{YOUR_CONN_STRING}", "{DB_NAME}", "{COLLECTION_NAME}", "{MS_TEAMS_WEBHOOK}")

log = Log("{SOURCE}", "{LOG_TYPE}", "{MESSAGE}", "{EVENT}")
recorder.record_log(log)
```

## Running unit tests

```shell
$ export MONGO_URI="mongodb://user:password@host:port/?authMechanism=DEFAULT"
$ export DB_NAME="YOUR_DB_NAME"
$ python -m unittest discover tests
...
------------------------------------------------------------------------------
Ran 3 tests in 0.144s

OK
```
## Author

- [@josehenriqueroveda](https://www.github.com/josehenriqueroveda)

