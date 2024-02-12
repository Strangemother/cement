from portland import log, args
from portland.loader import load_dir

from pathlib import Path

def main(**kw):
    """Executed by running _this module_

        py portland/run.py
        py -m portand.run
    """
    return terminal_main(**kw)


def entry_main(**kw):
    """Executed through the __main__ entry, as the `portland` module:

        $> py -m portland create -h

    Or the _directory_:

        $> ls
        portland/ readme.md
        $> py portland create -h
    """
    return terminal_main(**kw)


def bin_main(**kw):
    """Executed through the global terminal installation

        portland create -h
        portland-cement create -h
    """
    return terminal_main(**kw)



HERE = Path(__file__).parent


def terminal_main(**kw):
    """Run the terminal application - the portland tools

    First collapse the known arguments and configure the logger level
    Load the apps directory
    execute the handler function (if any)

    At this point the main offloads to the _command_ (such as create).
    """


    # Double parse the raw parser, collecting log level first.
    parser = args.get_parser(False, add_help=False)
    pargs = parser.parse_known_args()
    log.configure_from_args(pargs[0])

    # Must run before the parser, else the parser cannot announce these items
    load_dir(HERE / 'commands/', module_name='portland.commands')
    # Configure the internal plugin parts.
    load_dir(HERE / 'apps/')

    parser = args.get_parser()
    pargs = parser.parse_known_args()

    # log.configure_from_args(pargs[0])

    log.i(f'terminal_main {pargs}')

    if hasattr(pargs[0], 'func'):
        return pargs[0].func(pargs)

    log.w(f'No function to execute for command: {pargs[0]}')
    parser.print_help()

if __name__ == '__main__':
    main()