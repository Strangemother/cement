# Mock Site

> A site to develop mock sites.

This is a standard wagtail + trim base allowing the easy development of components in one site.

Run the server as per a normal django app.

1. activate the env (`../activate.bat`)
2. `cd website`
3. `run.bat` (dev mode)

---

The `website` mock-site is not special. the primary application `website` serves a useful `mockups` app.

Within mockups is a URL and view for each in-progress UI component.
Other component can be created around this mockups directory such as `search` or other larger packages.