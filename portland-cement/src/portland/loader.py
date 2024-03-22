"""A Dynamic import function to load modules from a folder using the importlib.

    load_dir('./commands/')

As this exists current context, the runtime is manipulated and any loaded
modules register for later recall by the arguments executor.
"""

import sys
import importlib.util

from pathlib import Path

def load_dir(path, module_name='portland.apps'):
    for filename in path.glob('*.py'):
        load_module(filename, module_name)

def load_module(filename, module_name, exec_module=True):
    filename = Path(filename)
    mn = f'{module_name}.{filename.stem}'
    spec = importlib.util.spec_from_file_location(mn, filename)
    module = importlib.util.module_from_spec(spec)
    if exec_module:
        spec.loader.exec_module(module)
    # Verify contents of the module:
    # print(module.__name__, dir(module))
    return module