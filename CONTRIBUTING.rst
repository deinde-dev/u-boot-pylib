Contributing to the U-Boot Python Library
=========================================

Development setup
-----------------

Work in a virtual environment::

    python -m venv .venv
    . .venv/bin/activate
    pip install -r requirements.txt
    pip install -e .[test]

Running the tests
-----------------

::

    python -m u_boot_pylib test             # the whole suite
    python -m u_boot_pylib test <name>      # one test

The tests run in parallel if ``concurrencytest`` is installed. Some of them
create git repositories in temporary directories, so ``git`` is needed.

Building the documentation
--------------------------

::

    pip install -r doc/requirements.txt
    make -C doc html        # output in doc/_build/html

The module reference is generated from the docstrings.

Building the package
--------------------

::

    python -m build
    twine check --strict dist/*

Continuous integration
----------------------

The *Tests* workflow runs the suite on Python 3.10-3.13 and builds and
checks the package on every push and pull request.

Making a release
----------------

Releases are published to PyPI automatically by the *Release* workflow
when a version tag is pushed. The flow is:

1. Update ``CHANGELOG.rst``: move the ``Unreleased`` entries under a new
   ``X.Y.Z - <date>`` heading.
2. Bump ``version`` in ``pyproject.toml``.
3. Commit the changes.
4. Tag it. The tag must be ``v`` followed by the exact version, for
   example::

       git tag v0.1.0
       git push origin v0.1.0

   A tag containing ``rc`` (for example ``v0.1.0rc1``) publishes to
   TestPyPI; a final tag publishes to the real PyPI. The workflow
   refuses to publish if the tag does not match the project version.

   You can also trigger the *Release* workflow manually (the
   ``workflow_dispatch`` option) to publish the current branch to
   TestPyPI for a dry run, without a tag.

Publishing uses PyPI Trusted Publishing (OIDC), so no API tokens are
stored. The PyPI and TestPyPI projects must each be configured to trust
this repository's ``release.yml`` workflow (environments ``pypi`` and
``testpypi``).
