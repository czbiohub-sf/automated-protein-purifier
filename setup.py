import setuptools

setuptools.setup(
    name="czpurifier",
    version="0.0.2",
    author="Robert R. Puccinelli",
    author_email="robert.puccinelli@outlook.com",
    description="Automated protein purifier project and utilities.",
    url="https://github.com/czbiohub/ProteinPurifier.git",
    packages=setuptools.find_packages(exclude=["*.tests", "*.tests.*",
                                               "tests.*", "tests"]),
    install_requires=[
        'smbus2',
        'zmq',
        'pymotors@git+https://github.com/czbiohub/PyMotors#egg=pymotors',
        'pyconfighandler@git+https://github.com/czbiohub/PyConfigHandler#egg=pyconfighandler',
#        'vext.pyqt5',
    ],
    test_suite="tests",
    classifiers=[
        "CZ Biohub :: Bioengineering",
    ],
)
