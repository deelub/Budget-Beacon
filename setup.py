from setuptools import setup

setup(
    name='budget-beacon',
    version='0.1',
    py_modules=['app'],
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        budget-beacon=app:cli
    ''',
)