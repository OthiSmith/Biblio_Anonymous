from setuptools import setup, find_packages

setup(
    name='anonymizer',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'cryptography==3.4.7',
    ],
    entry_points={
        'console_scripts': [
            'anonymize=anonymizer.main:main',
        ],
    },
)