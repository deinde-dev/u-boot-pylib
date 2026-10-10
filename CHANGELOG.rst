Changelog
=========

All notable changes to this project are documented here. The format is
based on `Keep a Changelog <https://keepachangelog.com/en/1.1.0/>`_ and
the project follows `Semantic Versioning <https://semver.org/>`_.

Unreleased
----------

0.1.0 - 2026-10-10
------------------

Changed
~~~~~~~
- The library is now developed in its own repository at
  https://github.com/nxtboot/u-boot-pylib, with its history carried over from
  the U-Boot tree, where it lived in ``tools/u_boot_pylib``. The history of
  the modules which started out in patman is included too.
- The package is published from that repository as ``u-boot-pylib``,
  continuing the releases made from the U-Boot tree.
- Documentation is now published at https://u-boot-pylib.readthedocs.io/,
  including a reference for each module.

Fixed
~~~~~
- ``tools.run()`` and ``tools.run_result()`` use the environment given by
  their ``env`` argument. Before, this was silently ignored, so a tool always
  ran in the environment of the calling program.

Earlier releases
----------------

Versions 0.0.2 to 0.0.7 were published from ``tools/u_boot_pylib`` in the
U-Boot tree.
