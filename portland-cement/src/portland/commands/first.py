"""The 'first' command helps first-time users run the initial steps
for their generated application.

Prior to this step the user generates a new project:

    portland create myapp
    # created

The user can navigate into the newly created `myapp` to dicover `dev-first-install.py`

This command collects that file and helps the user run it correctly.
Once complete the dev-first-install script can be deleted.
"""
from portland import register, log
from wagtail.bin import wagtail as WB

from portland.loader import load_module
# from trim.execute import read_one_stream_command as read_one


def first_install_command_hook(subparsers):
    """A function to accept a subparsers entity and add a new parser.
    return the newly starterd sub parser.
    """
    log.d('Executing')
    run_parser = subparsers.add_parser('first',
                    aliases=('first-install', 'i',),
                    help='Run within a newly created Cinderblock project.')
    run_parser.set_defaults(func=first_install_command)
    # add = run_parser.add_argument
    return run_parser

log.d('Installing pre_parser_subparsers')
register.add('pre_parser_subparsers', first_install_command_hook)


def first_install_command(ns):
    # env check
    # requirements install
    log.e("Perform first run!")
    # Look for first run script.
    mod = load_module('dev-first-install.py', 'dev_first_install')
    # print(mod)
    mod.main()