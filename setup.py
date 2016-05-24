from setuptools import setup


setup(
    name='rest-shell',
    version='0.3',
    author = 'Trey Tabner',
    author_email = 'kejiqing@gmail.com',
    url = 'https://github.com/passionke/rest-shell',
    packages=['rest_shell'],
    entry_points={
        'console_scripts': [
            'rest-shell = rest_shell:main',
        ],
    },
    install_requires=[
        'Flask',
        'requests',
    ],
    license='GPLv3',
    description='RESTful shell for your server without shell access'
)
