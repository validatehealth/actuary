from setuptools import setup

setup(
    name='actuary',
    version='0.1',
    packages=['actuary', 'actuary.utils', 'actuary.regression',
              'Chapter_2_Core_Python.Chapter_2_Case_Study.rate_table'],
    url='https://github.com/validatehealth/actuary',
    license='MIT',
    author='Andrew Webster',
    author_email='andrew.webster@validatehealth.com',
    description='This is an actuarial toolkit as introduced by three Actex webinars on Python for Actuaries'
)
