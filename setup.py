from setuptools import setup

long_description = open('README.rst').read()

# Platform specific stuff
import platform

scripts = ['scripts/linkpred']
if platform.system() == "Windows":
    scripts.append('scripts/linkpred.bat')

setup(
    name='linkpred',
    version='0.1',
    url='http://github.com/rafguns/linkpred/',
    license='New BSD License',
    author='Raf Guns',
    tests_require=['nose'],
    install_requires=[
        'matplotlib>=1.1',
        'networkx>=1.7',
        'numpy>=1.6',
        'scipy>=0.10'
    ],
    author_email='raf.guns@uantwerpen.be',
    description='Python package for link prediction',
    long_description=long_description,
    packages=[
        'linkpred',
        'linkpred.evaluation',
        'linkpred.external',
        'linkpred.external.dispatch',
        'linkpred.network',
        'linkpred.predictors',
        'linkpred.util'
    ],
    package_data={
        'linkpred': ['tests/*.py'],
        'linkpred.evaluation': ['tests/*.py'],
        'linkpred.network': ['tests/*.py'],
        'linkpred.predictors': ['tests/*.py'],
        'linkpred.util': ['tests/*.py']
    },
    platforms='any',
    classifiers=[
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'License :: OSI Approved',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development',
        'Topic :: Scientific/Engineering',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Operating System :: OS Independent',
    ],
    scripts=scripts
)
