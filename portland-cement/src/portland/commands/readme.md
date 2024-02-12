# Commands

Apply a file within this directory to _automatically_ collect and run within the same context. The module should install itself into the runtime portland hooks, such as the `pre_parser_subparsers` hook.


## Creating Commands

Create a file within the `commands/` directory; preferrably called something distinct to the functionality. We'll create a `run_command.py` to dumbly execute django-admin commands as a passthrough.

within `commands/run_command.py`, We can install a subparser:

```py
from portland import register, log

def run_command_hook(subparsers):
    """Run a passthrough django command
    """
    log.d('Executing')
    run_parser = subparsers.add_parser('run',
                    aliases=('r',),
                    help='run a manage.py command directly')
    run_parser.set_defaults(func=run_command)
    # run_parser.add_argument() ...
    return run_parser

# Install the hook,
register.add('pre_parser_subparsers', run_command_hook)

def run_command(namespace):
    ...

```

We install _command hooks_ to the `pre_parser_subparsers` register.

The `run_command` is executed when the user performs `portland run ...`

```bash
$> portland -h
positional arguments:
  {create,startproject,c,run,r,ping,p}
                        sub-command help
    create (startproject, c)
                        Run
    run (r)             run a manage.py command directly
    ping (p)            Ping

optional arguments:
  -h, --help            show this help message and exit
  -l LOG_LEVEL, --log-level LOG_LEVEL
                                log level
```