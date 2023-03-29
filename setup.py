from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in monetize_ai/__init__.py
from monetize_ai import __version__ as version

setup(
	name="monetize_ai",
	version=version,
	description="game payment",
	author="Muneeb Mohammed",
	author_email="muneebmuhammed99@gamil.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
