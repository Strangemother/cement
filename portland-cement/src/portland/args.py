import argparse

from portland import register, messages


def get_parser(subparsers=True, **kw):
    parser = argparse.ArgumentParser(prog=messages.PROG,
                fromfile_prefix_chars='@',
                description=messages.DESC,
                epilog=messages.EPILOG,
                formatter_class=argparse.RawTextHelpFormatter,
                **kw,
                )

    # Porthouse Config file, _optionally_ given before any  subapp.
    # parser.add_argument('config', nargs='?', default=None)
    # parser.add_argument('--config-file', default=None) # None for real default.

    # parser.parse_args(['-f', 'foo', '@args.txt'])
    parser.add_argument('-l', '--log-level',
                action='store',
                default='warning',
                help='log level'
                )

    if subparsers:
        apply_subparsers(parser)
    # parser = apply_secret_options(parser, help=argparse.SUPPRESS)
    return parser

# from commands import create

def apply_subparsers(parser):
    subparsers = parser.add_subparsers(help='sub-command help')
    # create.create_command_hook(subparsers)
    register.run_key('pre_parser_subparsers', subparsers)
