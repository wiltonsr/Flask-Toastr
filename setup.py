"""
Flask-Toastr
-------------

Showing non-blocking notifications in Flask templates using toastr.
"""
import io
from setuptools import setup

with io.open('README.md', 'rt', encoding='utf8') as f:
        readme = f.read()

setup(
    name='Flask-Toastr',
    version='0.5.8',
    url='https://github.com/wiltonsr/Flask-Toastr/',
    license='MIT',
    author='Wilton Rodrigues',
    author_email='wiltonsr94@gmail.com',
    description='Showing non-blocking notifications in Flask templates using toastr.',
    long_description=readme,
    long_description_content_type='text/markdown',
    py_modules=['flask_toastr'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'Jinja2',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
