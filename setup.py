import setuptools
from setuptools.command.build_py import build_py
from setuptools.command.develop import develop

def download_server_jar():
    import os
    import sys

    if sys.version_info[0] < 3:
        from urllib import urlretrieve
    else:
        from urllib.request import urlretrieve

    SERVER_JAR_URL = 'https://github.com/ingtranet/korhal-java-server/releases/download/0.1.2/korhal-java-server-0.1.2.jar'
    CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))

    urlretrieve(
        SERVER_JAR_URL, 
        '{}/korhal/korhal-java-server-0.1.2.jar'.format(CURRENT_PATH)
    )  

class CustomBuildPyCommand(build_py):
    def run(self):
        download_server_jar()
        build_py.run(self)

class CustomDevelopCommand(develop):
    def run(self):
        download_server_jar()
        develop.run(self)

import io
with io.open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="korhal",
    # version="0.1.1",
    author="cookieshake",
    author_email="cookieshake.dev@gmail.com",
    description="KOrean Rpc-based Application for Handy Application for Language-processing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cookieshake/korhal",
    packages=setuptools.find_packages(),
    classifiers=[
    ],
    keywords='korean analysis tagger tokenizer',
    install_requires=[
        'grpcio==1.16.0',
        'googleapis-common-protos==1.5.3'
    ],
    python_requires='>=2.6, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    package_data={
        '': ['*.jar'],
    },
    cmdclass={
        'build_py': CustomBuildPyCommand,
        'develop': CustomDevelopCommand
    },
)
