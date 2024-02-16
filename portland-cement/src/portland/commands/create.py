"""The general "portland create appname" command

References:

+ https://docs.wagtail.org/en/stable/reference/project_template.html
+ https://github.com/wagtail/wagtail/blob/f32c321cdd19f047d30449e493b22eff6adfe9b3/wagtail/bin/wagtail.py#L58
+ https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-startproject-template
"""
import sys, os
from portland import register, log
from wagtail.bin import wagtail as WB
from pathlib import Path


def create_command_hook(subparsers):
    """A function to accept a subparsers entity and add a new parser.
    return the newly created sub parser.
    """
    log.d('Executing')
    run_parser = subparsers.add_parser('create',
                    aliases=('startproject', 'c'),
                    help='Run')
    run_parser.set_defaults(func=create_command)

    run_parser.add_argument("project_name", help="Name for your project")
    run_parser.add_argument("dest_dir",
                        nargs="?",
                        help="Destination directory inside which to create the project",
    )

    run_parser.add_argument('--special',
        help="A keyname to collect a new project from a %(prog)s package index",
        default=None)

    run_parser.add_argument('--template',
        help="The path or URL to load the template from.",
        default=None)

    return run_parser

log.d('Installing pre_parser_subparsers')
register.add('pre_parser_subparsers', create_command_hook)


class CinderblockCreateProject(WB.CreateProject):
    description = "Creates the directory structure for a new Cinderblock project."
    template_version = 'v6'

    def __init__(self, namespace=None):
        self._namespace = namespace[0]
        self.unknown_args = namespace[1]
        self.default_template_path = self.get_default_template_path()

    def get_default_template_path(self):
        return self.get_wagtail_template_path()

    def get_cinderblock_template_path(self):
        portland_path = self.get_cinderblock_template_dir()
        # Location of the internal project. Later this will be dyanmic.
        sub_path = f"wagtail/{self.template_version}/project_template"
        template_path = portland_path / sub_path
        return template_path

    def get_cinderblock_template_dir(self):
        import portland
        portland_path = Path(os.path.dirname(portland.__file__))
        sub_path = "project_templates/"
        return portland_path / sub_path

    def get_blank_template_path(self):
        portland_path = self.get_cinderblock_template_dir()
        sub_path = "blank/project_template"
        return portland_path / sub_path

    def get_wagtail_template_path(self):
        """Return the _wagtail_ default path project_template"""
        import wagtail
        wagtail_path = os.path.dirname(wagtail.__file__)
        default_template_path = os.path.join(wagtail_path, "project_template")
        return default_template_path

    # def add_arguments(self, parser):
    #     super().add_arguments(parser)

    def execute(self, argv):
        if self._namespace is None:
            # Default wagtail options.
            parser = self.create_parser()
            options = parser.parse_args(sys.argv[2:])
            self.run(**options_dict)

        options_dict = vars(self._namespace)
        self.run(**options_dict)

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

        # converted_template = self.resolve_template_name(options["template"])
        converted_template = self.discover_resolve_template_name(
                options["special"],
                options["template"]
            )
        template_name = converted_template

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
            f"--template={converted_template}",
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

    def discover_resolve_template_name(self, name=None, template=None):
        """Return a resolved template name. If `name` is given, assume a special
        terminal key. Attempt to resolve the _special_ name.
        If only the `template`, assume the --switch tooling and use the default
        (django --template=name)

            cement create cinderblock # name
            cement create --template=https://...
            cement create # default_template_path
        """
        if name in [None, 'default', 'cinderblock']:
            # If name is None we default to the template.
            # Of course the _default template_ is cinderblock
            # providing --name and --template results in --template
            return template or self.get_cinderblock_template_path()

        if name == 'wagtail':
            # Override 'cinderblock' addons in favour of the raw.
            # for advanced users.
            return self.get_wagtail_template_path()

        if name == 'blank':
            # Override 'cinderblock' addons in favour of the raw.
            # for advanced users.
            return self.get_blank_template_path()

        return self.remote_resolve(name)

    def remote_resolve(self, name):
        """Return a string for the template path matching the given `name`.

        This _remote_ resolve reads an external list of possible templates.
        Options include the cement package index or a local addon package.

        If None is returned, the cli will error-out (the safe option).
        The same applies for an unknown string.

        It's better to return the  unhandled string if a remote cannot be found,
        as this passes off to Django and Wagtail for more options.
        """
        print('Resolve special name:', name)
        # check for specials "flask", "fastapi",
        # should include a version or subswitch: "flask@5.1" or flask>=5.1.0
        return name

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
    proj_command = CinderblockCreateProject(ns)
    proj_command.execute(props)


def tech_test(ns):
    """Perform any "pre_test_hook" functions _before_ the execute.

    These functions include testing the venv etc.
    """
    print('Test the platform for any requirements')
    print(register.run_key('pre_test_hook', ns))