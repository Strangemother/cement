"""Copy the wagtail (or django) base template into a location to manually edit
"""
import os, shutil
from pathlib import Path


def start_copy(dest="."):
    print('Copy', os.getcwd())
    res_dest = Path(os.getcwd()) / dest
    path = get_default_template_path()
    if Path(path).exists():
        copy(path, res_dest)

def copy(target, dest, dir_name=None):
    print('copy', target)
    dir_name = dir_name or Path(target).name
    full_dest = dest / dir_name
    print('to', full_dest)
    if full_dest.exists():
        print('Path exists:', full_dest)
        return False

    new_path = shutil.copytree(target, full_dest)
    print('Copied to:', new_path)
    # temp/dir1/file.txt

def get_default_template_path():
    import wagtail
    wagtail_path = os.path.dirname(wagtail.__file__)
    return os.path.join(wagtail_path, "project_template")


if __name__ == '__main__':
    start_copy()