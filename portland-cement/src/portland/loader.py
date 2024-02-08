

import sys
import importlib.util

from pathlib import Path

def load_dir(path, module_name='portland.apps'):
    for filename in path.glob('*.py'):
        mn = f'{module_name}.{filename.stem}'
        spec = importlib.util.spec_from_file_location(mn, filename)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        # Verify contents of the module:
        # print(module.__name__, dir(module))