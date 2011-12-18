#!/usr/bin/env python
from setuptools import setup
from colour_field import __version__

setup(
    name = "django-colour-field",
    version = __version__,
    description = "JS Colour Field and Picker for django",
    url = "http://bitbucket.org/schinckel/django-colour-field/",
    author = "Matthew Schinckel",
    author_email = "matt@schinckel.net",
    packages = ["colour_field"],
    include_package_data = True,
    zip_safe=False,
)
