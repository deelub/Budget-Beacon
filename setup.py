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

# Currency selection
# Default categories
# Data storage location

#Figure out python database connection - Afterwards use that connection to get the sum of everything

#Catgegories:
# A. groceries
# B. Transport
# C. Toiletrics
# D.Elec + Water
# E/Housing/Rent
#Leisure