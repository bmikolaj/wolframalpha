#!/usr/bin/env python
# Generated by jaraco.develop (https://bitbucket.org/jaraco/jaraco.develop)
import setuptools

with open('README.md') as f:
	long_description = f.read()

setup_params = dict(
	name='wolframalpha',
	use_hg_version=True,
	description="Wolfram|Alpha 2.0 API client",
	long_description = long_description,
	author="Brian Mikolajczyk",
	author_email="brianm12@gmail.com",
	url="https://github.com/p014k/wolframalpha",
	packages=setuptools.find_packages(),
	zip_safe=False,
	install_requires=[
		'six',
	],
	setup_requires=[
		'hgtools',
		'pytest-runner',
	],
	tests_require=[
		'pytest',
	],
)
if __name__ == '__main__':
	setuptools.setup(**setup_params)
