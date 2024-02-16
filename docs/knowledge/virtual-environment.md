# Virtual Environments

A python "virtual environment" is a unique copy of the target runtime (such as python 3.12) dedicated to this application. It allows _sandboxing_ of your application dependencies to ensure your installed packages don't pollute your other application imports.

Cinderblock is designed to run in an `venv` (virtual environment) and provides some tools to help

## Our Practices

We recommend you keep you environment directory **local** and unique to the application. You create a new environment for every unique python application.

1. If you have one environment, call it `env/`
2. Put it next to your app, either within the project root, or its parent.
3. Use a unique env for unique each python version 1e.g. `3.10` and `3.11`

Use the standard python command to create a new environment:

```bash
$> python -m venv env
```

Once done, activate it:

```bash
$> env/Scripts/activate.bat
(env) $> which python
/cygdrive/root/projects/concrete/env/Scripts/python
```

When installing new packages (such as the requirements.txt), the packages are stored within this `env/` directory, rather than the python global package directory.