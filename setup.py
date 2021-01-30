from setuptools import setup

setup(
    name='py3-rest-shell',
    version='0.4',
    author = 'Dogukan Cagatay',
    author_email = 'dcagatay@gmail.com',
    url = 'https://github.com/dogukancagatay/rest-shell',
    packages=['rest_shell'],
    entry_points={
        'console_scripts': [
            'rest-shell = rest_shell:main',
        ],
    },
    install_requires=[
        'Flask',
        'requests',
        'simplejson',
    ],
    license='GPLv3',
    description='RESTful shell for your server without shell access'
)
