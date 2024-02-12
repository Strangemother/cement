Project Template

Portland Cement inherits its base from Wagtail. The standard `wagtail create ...` is replaced with `cement start ...` with a few additions to integrate cement addons.

Generating a new base can be done through the free tool:

    $>py -m portland.get_wagtail_template
    # create project_template/

The new directory contains an unfettered copy of the Wagtail base site.

---

At this point we edit the base to include Cinderblock addons, and package it as a `template` for fresh installs. For the base package we _version_ the project template with a tag relative to the Wagtail version, and add the entire directory to `src/portland/project_templates/`

## Cement Changes

Each unique change to the Wagtail base application should be documented as an enhancement, to be reapplied on incoming versions. In addition users with existing installations may need to adopt changes manually and require a point of record for each change.

+ Each change to the base project template is documented
+ Applied during developer _project template creation_ when a new base is generated
+ And by the user with an existing app if the update isn't automatic


### Expected

It's expected cement addons are either typical django packages (with an installation manifest), or more integrated Portland Cement tools.

The hooks will be updated to reflect ongoing requirements.

+ `settings.*` hook: A `cement.settings` capture for integrated installs
+ _runhook_ for capturing a `cinderblock.py` or other  config files within sub-apps.
+ URLs hook: To install additional auto endpoints (outside the standard installation)

With these three Cement changes, we can handle most of the typical django app installation.

+ Install `INSTALLED_APPS` package
+ Add any `SETTINGS` from a sub package if required
+ Apply any `url_patterns` endpoints within the primary router

At this point other elements can be handled through the hooked processes. The user should `migrate`. However this is an easy task and can be a command to run by the CI or during a DB Deployment.

Therefore a pattern for the end-user should look like:

```bash
$> cement fetch cement[addon-name]
$> cement install cement[addon-name]
# ... Run hook settings
#   ... Install INSTALLED_APPS
#   ... Updating MIDDLEWARE
#   ... Applies 4 URL endpoints
Done! package cement[addon-name] requires a database migration after first install.
    Ensure to run `python manage.py migrate`  more info: http://cinderblock/migrate
$> python manage.py migrate
```


# Changes

## Dockerfile

The imports should be company or _site_ specific

## Readme

Apply a `readme.md` file, with an expectation for the end-user to extend it.

+ Project Name
+ Owner
+ Description
+ Installation

### Installation

Include setup instructions for end-user to run the app. Include some scripts to help with this.

## Requirements.txt

The `requirements.txt` is generated with the site. It should include an additional `-r` link to a `cinderblock-requirements.txt`. The cinderblock requirements are set by the system and advanced users.

    ...
    + manage.py
    + requirements.txt
    + cinderblock-requirements.txt

## `SETTINGS` and `INSTALLED_APPS`

### Package: django-trim

Add the `django-trim` to the INSTALLED_APPS

### Branding

+ Expose the _admin name_ (and other Django/Wagtail) default parameters within the `SETTINGS`, including:
    + Administration Site Name
    + CMS page include (Bottom right button), and CMS Admin site icons
    + CSS changes for the CMS Login and Admin site
    + Addition `HomePage`:
        + Add inline docs
        + Install a new Template (For the `welcome-page` and a site-specific base)


