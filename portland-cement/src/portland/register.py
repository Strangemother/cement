"""A 'register' space for incoming application and auto executables
Any import can append itself to an available slot, When required Portland Cement
will execute the hooks.
"""
from portland import log


CACHE = {
    'pre_test_hook':[],
    'pre_parser_subparsers':[],
}

def get_cache(key=None):
    if key:
        return CACHE[key]
    return CACHE


def add(key, item):
    log.info(f'Adding item to {key}')
    CACHE[key].append(item)


def run_key(key, ns):
    res = ()
    log.i(f'Executing functions for {key}')
    for execute_func in get_cache(key):
        v = execute_func(ns)
        res += (v,)
    return res
