# todo


## Home Page + Changes

The first home page should be an advert for portland cement/cinderblock

+ home image
+ admin icon
+ page links


## first-time

Provide a 'first-time' script for users, this will:

+ Ensure env
+ only for dev
+ run migrate
+ run createsuperuser
+ define the 'runserver.bat'

Then the user can perform `run.bat`, booting the first Portland service locally.

For the next stage, this step will implement the portland configuration to ensure first-runs include loaded assets.

## package-index, project-template-index

The `package-index` will be a Portland and pip installable package to provide a "install layer" for portland packages. This package provides a model for a "package", and views to list them.
An endpoint within the site can be used leverage the portland installer:

    portland fetch package-name
    # downloading "package-name" from https://short/portland
    # Configuring "package-name"

The `project-template-index` is a location to host many shared project templates. Portland can prepare a base application for a range of projects. Therefore the package index can list _alternative_ projects such as `flask` or `fastapi`, leveraging the portland projects template for blueprints for other products with a free UI.

### Properties

A package item should contain:

+ The name
+ Description
+ Readme information (linked or preferably pulled)
    + What it does
    + how it installs
    + required commands for install
+ The package link: bitbucket, github, package-index (pypi)

The package link connects to the product the user will apply to their installation (pip). such as `portland-cement` or `https://github`. I hope to advocate a direct connection to the installable unit here, rather than a link to a brand or marketing webite. As such another option is S3, stashing 'latest' assets.

## Centralise errors and prints

Error messages and _print-outs_ should be applied from a central set of strings. This is useful for unified documenting and easier for the user to extend.

```py

def get_default_template_path():
    try:
        import wagtail
    except ImportError as e:
        raise ImportError(messages.wagtail_import) from e

    wagtail_path = os.path.dirname(wagtail.__file__)
    return os.path.join(wagtail_path, "project_template")
```

```bash
$> py -m portland.example
! Error: Wagtail is not installed
    To perform this command, perform "pip install wagtail"
```