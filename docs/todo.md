# todo

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