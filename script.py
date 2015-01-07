#!/usr/bin/python
import os
import signal
import time
import logbook

# fake import. we only test PYTHONPATH val
from somelib.constants import SIGABRT

log = logbook.Logger('APP')
handler = logbook.FileHandler('script.log')


def log_info(msg):
    with handler.applicationbound():
        log.info(msg)


def log_err(msg):
    with handler.applicationbound():
        log.warn(msg)


def sigterm_handler(signum, frame):
    log_err('Process was killed. {0} - {1}'.format(signum, frame))
    exit(0)


if __name__ == "__main__":
    signal.signal(signal.SIGTERM, sigterm_handler)

    while True:
        log_info('i am running as {0} process'.format(os.getpid()))
        time.sleep(1)