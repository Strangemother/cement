# DataBase user `admin`, `pass`... Seriously?

**Yes!**

"Ooh but No!" I hear you cry! _Security Security Security?!_

**YES!** It's soooo much better when done safely.


## Reasoning

Over decades we've been taught _"Don't do X because it's very insecure"_. This span across everything within our lives - but focusing on the digital.

_Don't write down passwords_: Except but maybe it's usually the [best method](https://blog.1password.com/safe-write-down-your-passwords/)

Or _make sure password is a crazy unreadable string_: Except computer are _really good_ at random chars. [Probably best to use a simple sentence](https://www.keepersecurity.com/blog/2022/12/01/top-myths-about-password-security/)

... And so on. These gates existed for good reason in the past. But as technology progresses and developer experiences change, these rules become outdated.


## But The Database Password

Right? The database password _should_ be a completely incomprehensible key exchange, including some sort of [super sized prime number split in two](https://www.atlassian.com/git/tutorials/git-ssh#:~:text=At%20a%20very%20high%20level,derived%20from%20the%20public%20key.) Avoiding `admin` is a sure-fire method to defend against rainbow attacks or other brute force.

But brute force and rainbow attacks don't happen in local dev.

---

Cinderblock is built on-top of Django - complete with it's mature, sure-fire _development_/_production_ settings separation. When done correctly - it's tricky mix the two environments. Settings for `dev` (including its unique database configuration) are refocused during a `prod` deployment.

Production Settings include a database (perhaps targeting `Oracle`) of which does not have this `admin` user. Instead the users are managed through an OAuth (3rd party provider), and administrators are recreated in the production environment.

    # A literal different when deploying.
    > python manage.py runserver --settings=acme_product.settings.dev
    > python manage.py runserver --settings=acme_product.settings.prod


Including this, we have other gates:

+ `dev` database settings are local:

    # https://docs.djangoproject.com/en/4.2/ref/settings/#databases

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }

+ `prod` is remote...