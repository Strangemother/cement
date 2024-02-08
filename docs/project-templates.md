# Project Templates

> When running `portland create ...`, the tool copies a template project into your target directory. This doesn't need to be a Cinderblock project


Portland Cement is designed to very-pluggable. All _commands_, and _apps_ are modules loaded dynamically, allowing a library developer or end-user, to create addons without difficult integration.


The command `portland create` generates a new project within a target directory:

```bash
$> cd projects
$> portland create newsite
# newsite created
$> cd newsite/
$> python manage.py run
# runserver 127.0.0.1:8000/ ...
```

The `create` command calls upon a _project template_ and copies the content into a new directory. The default project template is an extension of the Wagtail base project (of which in-turn is built intop of Django's base project).

We can provide any template project to the application

```bash
$> cd workspace/
$> portland create derek --template ../portland-cement/src/portland/project_templates/blank
# derek created
```

Fundamentally the project template can be any content, it doesn't need to be a "cinderblock" style application. For example if you create a `flask` base - this can be used as a project template.

## Building a Project Template

A project template is a directory full of assets to deploy as the "base" of work. Some template commands are available for string replacement within directory names and files.

Here is an example of (a very old!) [torchbox project template](https://github.com/torchbox/wagtail-template/tree/develop/project_name/). As we can see it's a standard django setup with the work `project_name` in places.

1. Create a directory as the _root_ of the project content

    ```bash
    project_template
        project_name
            run.py
            assets/
                css/
        readme.md
        .gitignore
    ```

2. Then install it

    ```bash
    $> portland create derek --template project_template/
    ```

3. It's ready

    ```bash
    $> cd derek/
    $> ls
    derek/
        run.py
    .gitignore
    .readme.md
    ```

## Deploy and Install

Once a project template is prepared it can be packaged as a `.tar` file and installed locally or from a remote location:

```bash
$> portland create derek --template project_template/
$> portland create derek --template project_template.tar
$> portland create derek --template project_template.zip
$> portland create derek --template https://cinderblock/project_template.zip
```

Other installation types and routines are possible through the django template command.

1. once the project template is ready, zip it
2. Provide to users through a local or remote distribution method


# Reason

Cinderblock is a project template to build out a base package. Adhering to the philospohy of relying upon the underlying technology, we use django templating.

With this we can create a company based django template - and easily supplied through internal or custom packaging solutions. It's key to allow adoption across the eco-system and although Cinderblock is currently a django tool, there's no reason to assume that'll always be the case.

As such the _Cement_ for Cinderblocks can work on just-about anything :)

Therfore it can be instantly utilised for:

+ Deploying templates of other framework bases
+ Distributing _examples_, tech-starters or key-notes
+ Deploying multiple base project types under one app