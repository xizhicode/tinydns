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
    version='0.2.2',
    description='this project is a tiny dns server implementation by python, it is very easy to use',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/xizhicode/tinydns.git',
    author='zhaohengping',
    author_email='18438697706@163.com',
    maintainer='zhoukunpeng',
    maintainer_email='18749679769@163.com',
    install_requires=["docopt", "gevent", "dnslib"],
    include_package_data=True,
    entry_points={
                  'console_scripts': [
                      'tinydns=tinydns.__init__:main',
                  ],
              },
    package_data={
            '': ['*.rst'],
        },
    python_requires='>=2.6, <=3',
    license='GPL-2.0',
    classifiers=[
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ]
)
