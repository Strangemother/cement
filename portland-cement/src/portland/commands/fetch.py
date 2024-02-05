"""Download a package and drop it into the correct location ready for install.

This accesses the _internal_ portland searchable endpoint, not pypi.
"""

import sys
from portland import register, log

def collect_command_hook(subparsers):
    """A function to accept a subparsers entity and add a new parser.
    return the newly created sub parser.
    """

    run_parser = subparsers.add_parser('fetch',
                    aliases=('f',),
                    help='Collect a remote package')
    run_parser.set_defaults(func=collect_command)
    # add = run_parser.add_argument
    return run_parser

register.add('pre_parser_subparsers', collect_command_hook)


def collect_command(ns):
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