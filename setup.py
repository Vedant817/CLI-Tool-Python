from setuptools import setup, find_packages

setup(
    name='my_cli_tool',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'weather=cli_tool:main',
        ],
    },
)
