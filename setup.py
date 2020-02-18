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
    version='0.1.1',
    description='this project is a tiny dns server implementation by python, it is very easy to use',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/xizhicode/tinydns.git',
    author='zhaohengping',
    author_email='18438697706@163.com',
    maintainer='zhoukunpeng',
    maintainer_email='18749679769@163.com',
    install_requires=["docopt", "gevent", "dnslib"],
    entry_points={
                  'console_scripts': [
                      'tinydns=tinydns.__init__:main',
                  ],
              },
    package_data={
            '': ['*.rst'],
        },


)
