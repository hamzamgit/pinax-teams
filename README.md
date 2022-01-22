![](http://pinaxproject.com/pinax-design/patches/pinax-teams.svg)

# Pinax Teams

This project is designed to use for those applications who are already using django allauth for their projects and facing trouble with duplicate app (account) while isntalling pinax-invitations.

[![](https://img.shields.io/pypi/v/pinax-teams.svg)](https://pypi.python.org/pypi/pinax-teams/)


## Table of Contents

* [About Pinax](#about-pinax)
* [Important Links](#important-links)
* [Overview](#overview)
  * [Dependencies](#dependencies)
  * [Supported Django and Python Versions](#supported-django-and-python-versions)
* [Documentation](#documentation)
  * [Installation](#installation)
  * [Usage](#usage)
  * [Settings](#settings)
  * [Models](#models)
  * [Middleware](#middleware)
  * [Template Tags](#template-tags)
  * [Signals](#signals)
  * [Views](#views)
* [Change Log](#change-log)
* [Contribute](#contribute)
* [Code of Conduct](#code-of-conduct)
* [Connect with Pinax](#connect-with-pinax)
* [License](#license)

## About Pinax

Pinax is an open-source platform built on the Django Web Framework. It is an ecosystem of reusable Django apps, themes, and starter project templates. This collection can be found at http://pinaxproject.com.


## Important Links

Where you can find what you need:
* Releases: published to [PyPI](https://pypi.org/search/?q=pinax) or tagged in app repos in the [Pinax GitHub organization](https://github.com/pinax/)
* Global documentation: [Pinax documentation website](https://pinaxproject.com/pinax/)
* App specific documentation: app repos in the [Pinax GitHub organization](https://github.com/pinax/)
* Support information: [SUPPORT.md](https://github.com/pinax/.github/blob/master/SUPPORT.md) file in the [Pinax default community health file repo](https://github.com/pinax/.github/)
* Contributing information: [CONTRIBUTING.md](https://github.com/pinax/.github/blob/master/CONTRIBUTING.md) file in the [Pinax default community health file repo](https://github.com/pinax/.github/)
* Current and historical release docs: [Pinax Wiki](https://github.com/pinax/pinax/wiki/)


## pinax-teams

### Overview

`pinax-teams` is an app for Django sites that supports open, by invitation, and by application teams.

#### Dependencies

* django-appconf
* django-reversion
* pillow
* pinax-invitations
* six
* python-slugify

See [`setup.py`](https://github.com/pinax/pinax-teams/blob/master/setup.py) for specific required versions of these packages.


#### Supported Django and Python Versions

Django / Python | 3.6 | 3.7 | 3.8
--------------- | --- | --- | ---
2.2  |  *  |  *  |  *
3.0  |  *  |  *  |  *


## Documentation

### Installation

To install pinax-teams:

```shell
    $ pip install pinax-teams
```

Add `pinax.teams` and other required apps to your `INSTALLED_APPS` setting:

```python
    INSTALLED_APPS = [
        # other apps
        "pinax.account",
        "pinax.invitations",
        "pinax.teams",
        "reversion",
    ]
```

Optionally add `TeamMiddleware` to your `MIDDLEWARE` setting:

```python
    MIDDLEWARE = [
        # other middleware
        "pinax.teams.middleware.TeamMiddleware",
    ]
```

Add `pinax.teams.urls` to your project urlpatterns:

```python
    urlpatterns = [
        # other urls
        url(r"^account/", include("account.urls")),
        url(r"^teams/", include("pinax.teams.urls", namespace="pinax_teams")),
    ]
```
