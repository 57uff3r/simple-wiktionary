from setuptools import setup

setup(
    name='simplewiktionary',
    version='0.1',
    description='Provides access to simple definitions of English words from  Wiktionary',
    url='https://github.com/57uff3r/simple-wiktionary',
    packages=['simplewiktionary'],
    zip_safe=False,
    install_requires=[
        'beautifulsoup4>=4.5.3',
        'lxml>=4.1.1',
    ],
    license='MIT',
    author='Andrey Korchak',
    author_email='57uff3r@gmail.com'
)