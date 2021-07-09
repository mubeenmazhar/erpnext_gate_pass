from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in erpnext_gate_pass/__init__.py
from erpnext_gate_pass import __version__ as version

setup(
	name='erpnext_gate_pass',
	version=version,
	description='Issue gate pass for warehouses.',
	author='Mubeen',
	author_email='m@m.m',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
