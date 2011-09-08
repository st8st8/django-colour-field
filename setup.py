#!/usr/bin/env python
from setuptools import setup

setup(
    name = "django-colour-field",
    version = "1.0",
    description = "JS Colour Field and Picker for django",
    url = "http://bitbucket.org/schinckel/django-colour-field/",
    author = "Matthew Schinckel",
    author_email = "matt@schinckel.net",
    packages = ["colour_field"],
    include_package_data = True,
    zip_safe=False,
)
