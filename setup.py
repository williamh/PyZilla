from distutils.core import setup

setup(
    name='PyZilla',
    version='0.1.0',
    author='Noufal Ibrahim',
    author_email='noufal@nibrahim.net.in',
    url='http://github.com/nibrahim/PyZilla',
    py_modules = ['pyzilla'],
    license='LICENSE.txt',
    description='Python wrapper for the BugZilla XML-RPC API',
    long_description=open('README.txt').read(),
    classifiers=[
    'Development Status :: 4 - Beta'
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU General Public License (GPL)'
    'Operating System :: POSIX',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: MacOS :: MacOS X',
    'Topic :: Software Development :: Libraries :: Python Modules'
    'Topic :: Software Development :: Quality Assurance',
    'Topic :: Utilities',
    'Programming Language :: Python'
    ]
)
