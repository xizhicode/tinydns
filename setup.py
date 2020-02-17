import shutil
from pkg_resources import Requirement, resource_filename
try:
    from setuptools import setup,find_packages
except ImportError:
    from distutils.core import setup,find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="tinydns",
    packages=find_packages(),
    version='0.0.7',
    description='this project is a tinydns automaton implementation by python',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/xizhicode/tinydns.git',
    author='zhaohengping',
    author_email='18438697706@163.com',
    data_files = [('/etc', ['tinydns.conf'])],
    install_requires=["gevent","dnslib"],
    entry_points={
                  'console_scripts': [
                      'tinydns=tinydns.__init__:main',
                  ],
              },
    package_data={
            '': ['*.rst'],
        }

)
