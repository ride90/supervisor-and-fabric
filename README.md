supervisor-and-fabric
--------

Simple example app for controlling process with supervisor. Use fabric to run supervisor commands.

Installation
---------

- virtualenv .env
- source .env/bin/activate
- pip install -r requirements.txt

Usage
---------
- fab start (start process)
- fab stop (stop process)

You can check working processes with:
- ps aux | grep python

You can kill process script.py and supervisor will run it again
