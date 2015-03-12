from setuptools import setup, find_packages

version = '0.7.0.dev'

long_description = (
    open('README.rst').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.rst').read()
    + '\n' +
    open('CHANGES.rst').read()
    + '\n'
)

setup(
    name='ploneintranet.core',
    version=version,
    description="Plonesocial core package",
    long_description=long_description,
    # Get more strings from
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Plone :: 4.2',
        'Framework :: Plone :: 4.3',
        'Framework :: Plone',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='plone socbiz social microblog activity stream',
    author='Bogdan Girman',
    author_email='bogdan.girman@gmail.com',
    url='http://github.com/cosent/ploneintranet.core',
    license='gpl',
    packages=find_packages(),
    namespace_packages=['ploneintranet'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        # -*- Extra requirements: -*-
        'plone.api',
        'plone.app.blocks',
        'plone.app.tiles'
    ],
    extras_require={
        'test': [
            'plone.app.testing',
            'unittest2',
        ],
    },
    entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = Plone
    """,
)
