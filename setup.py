from setuptools import setup
from db_connection import create_DB

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

def DB_setup(): #We should check for database name in users file. If it does not exist then DB was not set up
    create_DB()