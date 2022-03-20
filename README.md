# Cofi Code Challenge

The solution for this challenge has been implemented using Python 3 and an object oriented paradigm. At high level, the design
of this solution contains two main classes, a `Checkout` as an interface between the user and the system and a class
`Promotion` used as base interface for the concrete promotions to be added to the system. A set of promotions can be linked 
in an ordered pipeline.

![UML diagram](/doc/UML.drawio.png)

### Execution
In order to test the implementation of the challenge, you can execute the main file `cofi-store.py` from the root directory:
```
$ python3 cofi-store.py
$ total: 30.0
```

### Unit testing
The unit tests can be executed via a Python 3 virtual environmnet.

First of all, install virtual in case it's not installed in your system
```bash
$ pip3 install virtualenv
```

Then, you can execute the test following the next commands:
```bash
$ cd test
$ python3 -m venv pytest-env
$ source pytest-env/bin/activate
$ pip install pytest
$ python3 -m pytest
$ deactivate
```