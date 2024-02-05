from portland import register, log

def run_command_hook(subparsers):
    """Run a passthrough django command
    """

    run_parser = subparsers.add_parser('run',
                    aliases=('r',),
                    help='run a manage.py command directly')
    run_parser.set_defaults(func=run_command)
    # run_parser.add_argument() ...
    return run_parser


from django.core.management import call_command

def run_command(ns):
    args = ns[1]
    print('Run args:', args)
    call_command(*args)


register.add('pre_parser_subparsers', run_command_hook)