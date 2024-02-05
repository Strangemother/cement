# Readme

Many sites built upon the base cement. To integrate a site, we should depend upon `portland-cement` and build a _site_ from the base of this.

---

## Dev Notes

To incoporate this, whilst adhering to the django solution. A base _site_ should copy the wagtail format, then _concat_ the additional project template content.

cement maintains a `portlandcement startproject` acting like the wagtail.
It will ask a _set_ of questions, aggregated from an inclusive script.

The includes add _additional modules_ to the base; These copy into the root and apply configs.

### Assets

+ Trim
+ Brickbase: CSS Grid base

#### Core tools

+ Accounts
    + Social Login
    + IDA login

### Sites

sites to build the base upon

#### Cinderblock advert

A 'home' with themed blocks. Links to docs.
the docs should associte markdown

##### Persona Page

+ Generate a character image for a person. This could be a face or asset. Combine with knowledge around the person; e.g for me; math, AI, dones, python, sciences, etc.

This is listed in the people page as a grid and name

    |=====| |=====| |=====|
    |     | |     | |     |
    |  A  | |  B  | |  C  |
    |=====| |=====| |=====|


A persona page present this

    |============|=======|
    | Name A     |       |
    | Stuff..    |  IMG  |
    |            |       |
    |--------------------|
    |  etc...            |

With the graphic, A bio, text and links to other internal pages.
The links present their successes.

The site-wide menu should present this and the sub content for nav:

    Home
     |- About
     |- Personas
        |- Jay
           |- python
           |- drones
        |- Eric
           |- java

#### Intelij Dev Docs

They're proven to be delightful. Copy the structre for a demo of the css grid structuing.

#### Personal Blog

#### porthouse view

#### Book store

#### PS