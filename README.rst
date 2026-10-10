.. SPDX-License-Identifier: GPL-2.0+

U-Boot Python Library
=====================

This is a Python library used by various U-Boot tools, including
`patman <https://github.com/nxtboot/patman>`_,
`binman <https://github.com/nxtboot/binman>`_ and
`buildman <https://github.com/nxtboot/buildman>`_. It provides:

- ``command`` and ``cros_subprocess``: running commands and pipelines,
  capturing their output
- ``tools``: running tools and handling files and temporary directories
- ``gitutil``: working with git repositories
- ``terminal``: coloured output and capturing output in tests
- ``tout``: logging at different verbosity levels
- ``test_util``: running test suites, in parallel if possible, and checking
  their coverage
- ``claude``: running Claude agents

Install it with pip::

    pip install u-boot-pylib

To run the tests::

    python3 -m u_boot_pylib test

The library was split out of the U-Boot source tree, where it lived in
``tools/u_boot_pylib``, so that tools maintained outside U-Boot can share it.
