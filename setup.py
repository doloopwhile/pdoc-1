from setuptools import setup
import os.path

setup(
    use_scm_version={
        'write_to': os.path.join('pdoc', '_version.py'),
    },
)