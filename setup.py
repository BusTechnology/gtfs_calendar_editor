from setuptools import setup, find_packages

setup(
    name='gtfs_calendar_editor',
    packages=find_packages(),
    include_package_data=True,
    tests_require=[
        'unittest',
    ],
)
