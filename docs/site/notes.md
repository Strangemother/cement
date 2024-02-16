# Notes

> Notes regarding the site components - as adverts and future content docs.

# advert

Low code developer models! don't fight the system - let it work for you...

Cinderblock comes with developer-love built-in. Build complex database modelling without the complex congitive dissidance

Wouldn't it be great if your database modelling integration layer had these features built-in:

+ Low code model creation
+ Integrated CRUD for administrators
+ Complex self-referable modelling
+ Multi-database compatible
+ built-in migrations
+ With or Without an ORM

```py
from django.db import models
from trim.models import fields

class CleverLittleFamily(models.Model):
    name = fields.chars(255)
    age = fields.int()
    bio = fields.text()
    friends = fields.m2m_self()
```

Cinderblock database modelling comes complete with resilience, mataurity, and security at the core.
