"""The 'starter' command to assist new users onboard with a fresh project.

This command runs through a series of questions and applies a cement config
for the output application. The helper tools should include:

+ Testing and Creating a new environment
+ [installation of a custom template]
+ Any additional cement apps (fetch and configure)
+ Destination and base config
+ First migration and admin user
+ print next steps.

The goal is to ensure a first app is prepared to run, complete with an environment
and any installed apps.

Once created the user should continue with the general tools in the compiled app.
"""
from portland import register, log
from wagtail.bin import wagtail as WB


def starter_command_hook(subparsers):
    """A function to accept a subparsers entity and add a new parser.
    return the newly starterd sub parser.
    """
    log.d('Executing')
    run_parser = subparsers.add_parser('starter',
                    aliases=('forge', 'HALP!'),
                    help='QA tool for fresh applications')
    run_parser.set_defaults(func=starter_command)
    # add = run_parser.add_argument
    return run_parser

log.d('Installing pre_parser_subparsers')
register.add('pre_parser_subparsers', starter_command_hook)


def starter_command(ns):
    log.e("Oowee. We're working on it!")
    raise NotImplementedError("Oowee. We're working on it!")

    return NotImplemented

