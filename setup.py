from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in label_print_gc/__init__.py
from label_print_gc import __version__ as version

setup(
	name="label_print_gc",
	version=version,
	description="label",
	author="admin@greycube.in",
	author_email="admin@greycube.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
