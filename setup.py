import re
from setuptools import find_packages, setup

with open('eodms_api_client/__init__.py') as f:
    init_txt = f.read()
name = re.search(r"__name__ = \s*'([\S.*]+)'", init_txt).group(1)
version = re.search(r"__version__ = \s*'([\d.*]+)'", init_txt).group(1)

setup(
    name=name,
    version=version,
    description='Tool for querying and submitting image orders to Natural Resources Canada\'s Earth Observation Data Management System (EODMS)',
    packages=find_packages(exclude=['']),
    entry_points='''
    [console_scripts]
    eodmsapi=eodms_api_client.cli:cli
    '''
)
