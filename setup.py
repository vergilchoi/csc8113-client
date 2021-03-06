from setuptools import setup

setup(
    name='csc8113',
    version='0.1.0',
    packages=['client', 'utils', 'user', 'document', 'status'],
    install_requires=['click', 'ecdsa', 'requests', 'sqlalchemy', 'prompt-toolkit'],
    entry_points={
        'console_scripts': [
            'csc8113 = client.__main__:cli'
        ]
    })
