# Installing addons

portland-cement allows the additional installation of package during and after a project creation project.

This includes "sub packages" of cement, and cinderblock of which are built specifically for plug and play. Fundamentally these components are _standard packages_ but built within a micro eco-system to support future upgrades

## OMG Yet another ecosystem!?

Great question. No.

I'm a django developer. But love building websites, so I utilise off-the-shelf packages. This is easy for me but difficult to a new developer or even _non_-developers.

Therefore rather than provide a giant, creeking, product-bound monolith of our own design, we 101% fully embrace the open packaging from fresh environments.

This means _not_ providing custom built packages - but apply auto-plugin features allowing devs to built upon **django** and **wagtail** - not _cinderblock_ and _cement_


## Installing

Addons are configured before deployment. They can be applied pre or post creation. `portland-cement startproject` will ask a range of optional questions, resulting in a configuration file.

Upon first boot the db is configured. after this, an update to the config, followed by any general migrations applies the new config:

    portland-cement startproject demo
    # Looking for available components ... Found 6
    1/6 - install `cinderblock[accounts]` for user accounts [Y/n]: y
    2/6 - install `cinderblock[sheets]` for data-presentation [Y/n]: n
    ...
    6/6 - install `cinderblock[company-sso]` for SSO Auth [Y/n]: y
    # Building ./config.json of 5 items
    # ... create project ...

We can update as per normal packaging:

    $> portland-cement addons add cinderblock[advert-cells]
    # downloading.. from configured pypi...
    # addon 1 item to ./config.json
    $> python manage.py migrate
    # ...

In some cases developer additions may be required. But the packages should be ready to go.


## How Addons are made.

We utilise the existing packaging solutions (pypi), and create clean installable modules.

These are installed and configured in place. The plug-in nature of the addon ensures the tool is already configured.

For example:

+ Logins
  Using all the core features of django, but supply the views and URLS.
  This can also include optional domain specific pre-configurations.
+ Auth
  SSO integration can be a range of settings installations. For `cinderblock` packages the user can install site specific configurations, and adapt their app.
+ UI?
  No UI, Only optional CSS with the user recommendation to bring their preferred frontend.
  Therefore cinderblock is not vendor locked, or _react X.XX specific_ for example.
+ Blocks
  `cinderblocks` extends wagtails `streamfields` to produce plug and play HTML solutions.
  This allows highly extendable, business complex admin UI (django/wagtail) with the a hot swappable feature-set of inner components.

  These blocks include "images", "paragraphs", and other server based presentation components.

Finally all django and wagtail packages are available within the same eco-system if a developer wishes to step away from the cemented solutions.


## Custom Addons

The user will develop their own source such markdown tools or business logic. portland-cement provides packaging commands - of which are standard packaging tools.

The user will develop upon their own app, or then build upon custom components;

---

So no custom addons.