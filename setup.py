from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in uc/__init__.py
from uc import __version__ as version

setup(
	name="uc",
	version=version,
	description="Umaima Communication",
	author="Tech Ventures",
	author_email="safdar211@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
