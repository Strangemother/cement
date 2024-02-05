# Cement Modules

> Pip installable modules built specifically for the the portland cememnt buildout.

Portland Cement incoporates _other_ libraries without the hassle for the end-user, packing units into "pip installable" modules, to ensure they're easily installed in a users.

For example a Cement developer may opt to use:

+ Django core user functionality
+ Wagtail layer
+ Cement[accounts]
+ A custom package

As Portant Cement relies upon Wagtail, of which in-turn uses Django. The end-user is _installing django addons_. Making development easier for the supplier and consumer.

## How does it work.

1. A Developer creates a _cement addon_, of which is actually a pip installable module.
    a. The 'addons' are typical assets, with a config file for portland-cement
2. The Developer deploys the addon to their preferred packaging library
3. The User discovers the package and installs it
    e.g. `portand collect cement[accounts]`
4. The User installs any changes

In the general case this is generally easy for a developer, but when deploying to a low-code environment, end-users may struggle to configure settings. Cement addons supplies these settings in a manifest format.

### End user experiance

The end-user should recieve a low-code install, with a QA session to configure the addon after _collection_. The name of the package is arbitrary

    # Install our accounts module - it's configured for inside the company
    $> portland install cement[accounts]
    # pip install cement[accounts] ...
    ... downloading
    # running post collect script...
    $> Would you like to use the company defined Single Sign on [Y/n]? Y
    # Installing "custom-auth.conf"

    ... cement[accounts] Installed.
    This package requires a database migration. Run now [Y/n]? Y
    ... Done.
    $>


The goal for a package:

1. Auto hook into the portland deployed site: e.g. no `INSTALLED_APPS` for cement addons)
2. configured for closed source environments: Custom package locations, configurable settings for site-specific changes.
3. low-code install: It's preferred the end-user need only to _install_ and _migrate_ those changes.
    More can be done for advanced install. But "plug-and-play" for safe configs.


## Developing an addon

There is no 'sure-fire' method to developing an addon. A cement addon is a django app. The extra 'hook' layer applies site-prepared configurations for the deployed config. In some cases packages including many hooks and adaptions to the app (e.g a custom rendering layer). Other packages may need a simple _include_ (such as dynatrace)

In all cases the developer should opt for modularity, by developing a standard python package of which would install through normal channels.

---

The name of a package isn't important. `portland` is the app running many `cement` tools. Generally the name of a package would be `cememnt[app]`, allowing a user to pip install that target name.

The developer may opt to rename the entire stack; `portland` becomes `webstarter` and the `cement` moniker becomes `megacorp`:

    $> webstarter create coolapp
    $> cd coolapp/
    $> webstarter install megacorp[accounts]
    $> webstarter install megacorp[analytics]
    $> webstarter install megacorp[databases]
    # Installing configs from "myteam-info.txt"
    # ... accounts are internal OAuth
    # ... Setup 'adobe analytics' account "team-webdevs"
    # ... Installing Database Configuration "company default"
    # ... Performing migrations ...
    # Done.
    $> python manage.py run
    # Running on http://localhost:8000/


Notice here the end-user has active account, analytics, and database setup


# package index

The package index is a django app with an app, allowing models for file upload (wheels and packages) and a searchable index.

This is a a cement addon, serving the first _package_ in the suite of tools.

    pip install cememt[package-index]

Then we have new urla `packages/index/`, `packages/search/`,
of which the `portland collect ...` can access.

The backend is a "manual" repository cheeseshop, therefore easily rendered raw or abstract (a simulated access package index)

+ https://packaging.python.org/en/latest/guides/hosting-your-own-index/



# Expected Packages

Some packages mandated for the cement packaging:

+ Plausible/Adobe-analytics
+ wagtail 'blocks'
+ Accounts: for a custom OAuth endpoint and Social
+ Databases: Configured for on-site configs (auto sqlite and mysqls for example.)
+ Votes: voting on any page
+ mail
+ package-index