# cement

First draft of a new app base.

## Websites

Each folder is content, reseatch, and assets for distinct websites.

## portland-cement

The open source user terminal app and component aggregator; essentially a helper tool to facilitate the 'cement' tools. This includes commands like _startproject_ and packages built for install (SSO auth clients etc...)

## mock-site

An active area to work upon integrated components - This includes page mockups.


---

# Getting started

When working on the tool here, prepping assets for a new site, the content is built into mock-site.

Once the mock work is complete we transfer the assets to the existing or new site.
Given it's django, the new site can be built through:

+ Django (django-admin)
+ Wagtail (wagtail-admin)
+ Cement (portland-cement) \*preferred.


Cement leverages the most, where Django is the core tooling. Obviously this tool will recommend `portland-cement`, as it will perform a wagtail startproject, with cement addons.

## Review:

1. mock something out in `mock-site`
2. Transfer changes into _the new or existing project_

Other projects are built upon `cement` and `cinderblock` package addons.

# Demo Integration

The mockups within the site should be transfered into the primary build, this is done through the portland-cement cli tool:

1. Make some ideas
2. `portland-cement startproject cinderblock`
3. `portland-cement package add sso-interal-product`
4. `cd cinderblock/`
5. `activate.bat`
6. `run.bat`

The tool utilises django, many selected packages, some custome tools and the ability to run them,


