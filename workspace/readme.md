# Workspace

When developing or working with `portland-cemement`, it's key to develop the library setup in a manner similar to the user experience. Rather than using `portland-cement/src/` as our working directory, `workspace/` provides a nice place.

Here we can work with new commands in a "live" state, whilst also developing `portland/` within another _relative_ directory.

## Setup

Install the primary package in _development_ mode.

```bash
cd portland-cement/
# src, pyproject.toml here.
pip install -e .
```

The `-e` applies _editable_ to the installed resources and essentially sim-links the content. With this, when a file within the `src/` directory changes, the effects are automatically applied to the _installed_ package.

```py
import portand
# With -e, changes to the src/ affect the import here.
```

Without the `-e` switch, changes to the original `src/` do not affect any installation, and another `pip install .` would be necessary.

---

### Source Code

Given this is a test location, full of personal edits (such as testing the `portland create`), do not commit code within this directory. Only this file is applied within the git content.