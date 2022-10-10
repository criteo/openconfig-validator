#!/usr/bin/env python3
# type: ignore
"""Configure all the PEX."""

import os
import subprocess
import sys

from setuptools import find_packages, setup
from setuptools.command.build_py import build_py


class CustomBuild(build_py):
    """Customized setuptools build command - builds shared library."""

    def run(self):
        build_cmd = ["./build.sh"]
        if subprocess.call(build_cmd) != 0:
            sys.exit(1)
        build_py.run(self)


setup(
    name="openconfig_validator",
    version="0.4",
    include_package_data=True,
    dependency_links=[],
    packages=find_packages(),
    cmdclass={"build_py": CustomBuild},
)
