"""The general "portland create appname" command
"""
import sys
from portland import register, log
from wagtail.bin import wagtail as WB


def create_command_hook(subparsers):
    """A function to accept a subparsers entity and add a new parser.
    return the newly created sub parser.
    """
    log.d('Executing')
    run_parser = subparsers.add_parser('create',
                    aliases=('startproject', 'c'),
                    help='Run')
    run_parser.set_defaults(func=create_command)
    # add = run_parser.add_argument
    return run_parser

log.d('Installing pre_parser_subparsers')
register.add('pre_parser_subparsers', create_command_hook)


def create_command(ns):
    """In this raw functionality, the command runs the django admin (or wagtail admin.)
    """
    tech_test(ns)

    props = sys.argv
    log.info(f'Run with: {props}')
    """
    In this case we can import and use the default wagtail site generator
    (of which uses standard django)

    user options are given in a passthrough routine:

        portland create projectname
        wagtail start projectname

    If the entry signature changes, the `sys.argv` will need editing
    """
    proj_command = WB.CreateProject()
    proj_command.execute(props)


def tech_test(ns):
    """Perform any "pre_test_hook" functions _before_ the execute.

    These functions include testing the venv etc.
    """
    print('Test the platform for any requirements')
    print(register.run_key('pre_test_hook', ns))