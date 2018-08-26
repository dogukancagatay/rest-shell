from setuptools import setup


setup(
    name='py3-rest-shell',
    version='0.3',
    author = 'Mitsuko Megumi',
    author_email = 'mitsukomegumii@gmail.com',
    url = 'https://github.com/mitsukomegumi/rest-shell',
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
