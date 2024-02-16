# Template Architecture

The templating scheme allows a developer to integrate style choices and _switchable_ updates through templating. Cinderblock by default will utilise the Django templating language.


**base template**

The base template incorporates the root technology of the page, specific to a HTML 5 web-page. The root page is predominantly template variables, is Django _blocks_ for the incoming inherited sections.

**selected template**

The selected template is defined by the admin layer, utilising a base root selector for the page. Within the interface we apply a list of developer applied "template-names". When the end-user saves the base, the selected template is implemented

**sub template**

Each type of page aligns with a view type, such as _list_, _edit_, or even _template_ (defining no subtype). The selection of this type is done by the developer to iterate or present models in the Django fashion.

**Customised layer**

The customised layer defines the additional assets to style the webpage for the end-user preferences. This includes JS, CSS, and _components_ installed by the end-user through the admin interface.


## Concept A (*Previous*)

Integrated within the template architecture is a _wagtail template_ integration, providing an admin-tool to switch a template.

    base -> selected template -> sub-template -> customized layer
                              -> sub-template -> customized layer
                                              -> customized layer

---

Notes and Concerns

The "selected template" proves a minor inconvenience. In previous examples (the Cinderblock 4) templates override at the "customized layer" and this works well, allowing each page to define a sub-template of its own preference. However this also causes concerns when serving the page, as the dynamic inheritance is costly. When a base-layer changes, it's tricky to ensure this works across all upper ancestors.

The solution is to provide a seat of styles to refit a single page, but this proves troublesome if an underlying include requires HTML changes specific to a template.


## Concept B (*\*implementing*)

The second methodology allows the end-user to select any template. The developer ensures the specific template has a functioning base.


    alt-base -> sub-template      ->  selected template -> customized layer
                                                        -> customized layer
    base     -> selected template -> sub-template       -> customized layer
                                  -> sub-template       -> customized layer
