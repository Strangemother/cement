"""Ensure the application Venv is created.

1. Check the current python path
2. Check the 'global' python path

if they match, infer fault.

The QA should ask (unless quiet)

"""

import sys
from portland import log, register


def execute(ns):
    log.info('Executing Ensure env')
    return in_env()


log.info('Installing prehook')
register.add('pre_test_hook', execute)


def in_env():
    return sys.prefix != sys.base_prefix


