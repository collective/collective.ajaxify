from setuptools import setup

import pathlib


version = "1.0.0.dev0"
long_description = "\n".join(
    [pathlib.Path(filename).read_text() for filename in ("README.md", "CHANGES.md")]
)

setup(
    name="collective.ajaxify",
    version=version,
    description="collective.ajaxify is a RESTful hypermedia API for Plone.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # Get more strings from
    # https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 6.1",
        "Framework :: Plone :: 6.2",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="plone classicui pat-ajax patternslib",
    author="Johannes Raggam",
    author_email="thet@syslab.org",
    url="https://github.com/collective/collective.ajaxify/",
    license="gpl",
    python_requires=">=3.10",
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "setuptools",
        "Products.CMFPlone>=6.1",
    ],
    extras_require={"test": []},
    entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
)
