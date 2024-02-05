"""Hit the install endpoint to ensure it's available for package collaction.
"""

import sys
from portland import register, log

def ping_command_hook(subparsers):
    """A function to accept a subparsers entity and add a new parser.
    return the newly created sub parser.
    """
    log.d('Executing')
    run_parser = subparsers.add_parser('ping',
                    aliases=('p',),
                    help='Ping')
    run_parser.set_defaults(func=ping_command)
    # add = run_parser.add_argument
    return run_parser


log.d('Installing pre_parser_subparsers')
register.add('pre_parser_subparsers', ping_command_hook)


def ping_command(ns):
    """Hit a target endpoint using any pre-configured url.
    """
    tech_test(ns)
    props = sys.argv
    log.info(f'Run with: {props}')


def tech_test(ns):
    """Perform any "pre_test_hook" functions _before_ the execute.

    These functions include testing the venv etc.
    """
    log.d('Test the platform for any requirements')
    register.run_key('pre_test_hook', ns)