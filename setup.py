from setuptools import find_packages, setup

setup(
    name="system_connector_package",
    packages=find_packages(include=["system_connector_package.client.samos"]),
    version="1.0.0",
    description="A library that provides clients to communicate with SAMOS, MAAS, XAMA systems",
    author="onurkybsi",
    install_requires=["arrowhead-client==0.4.4a0"],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests'
)