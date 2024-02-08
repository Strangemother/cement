"""The general "portland create appname" command

References:

+ https://docs.wagtail.org/en/stable/reference/project_template.html
+ https://github.com/wagtail/wagtail/blob/f32c321cdd19f047d30449e493b22eff6adfe9b3/wagtail/bin/wagtail.py#L58
+ https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-startproject-template
"""
import sys, os
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


class CinderblockCreateProject(WB.CreateProject):
    description = "Creates the directory structure for a new Cinderblock project."

    def __init__(self):
        self.default_template_path = self.get_default_template_path()

    def get_default_template_path(self):
        import wagtail
        wagtail_path = os.path.dirname(wagtail.__file__)
        default_template_path = os.path.join(wagtail_path, "project_template")
        return default_template_path

    def run(self, project_name=None, dest_dir=None, **options):
        # Make sure given name is not already in use by another python package/module.
        try:
            __import__(project_name)
        except ImportError:
            pass
        else:
            sys.exit(
                "'%s' conflicts with the name of an existing "
                "Python module and cannot be used as a project "
                "name. Please try another name." % project_name
            )

        template_name = options["template"]
        if template_name == self.default_template_path:
            template_name = "the default Wagtail template"

        print(  # noqa: T201
            "Creating a Cinderblock project called "
            "%(project_name)s using %(template_name)s"
            % {"project_name": project_name, "template_name": template_name}
        )

        # Call django-admin startproject
        utility_args = [
            "django-admin",
            "startproject",
            "--template=" + options["template"],
            "--ext=html,rst,md",
            "--name=Dockerfile",
            project_name,
        ]

        if dest_dir:
            utility_args.append(dest_dir)

        utility = WB.ManagementUtility(utility_args)
        utility.execute()

        print(  # noqa: T201
            "Success! %(project_name)s has been created"
            % {"project_name": project_name}
        )


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
    ## template `wagtail\project_template\`
    proj_command = CinderblockCreateProject()
    proj_command.execute(props)


def tech_test(ns):
    """Perform any "pre_test_hook" functions _before_ the execute.

    These functions include testing the venv etc.
    """
    print('Test the platform for any requirements')
    print(register.run_key('pre_test_hook', ns))