"""Street Sweeper setup.py."""
from setuptools import setup


setup(
    name='street_sweeper',
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    description='A simple tool to automatically generate recuring street sweeping reminders.',
    url='https://github.com/iwoloschin/street_sweeper',
    author='Ian Woloschin',
    author_email='ian@woloschin.com',
    license='MIT',
    install_requires=[
        'holidays',
        'ics',
    ],
    entry_points={
        'console_scripts': [
            'street_sweeper=street_sweeper:main'
        ],
    },
    zip_safe=False
)
