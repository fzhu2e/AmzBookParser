from setuptools import setup
import amzbkparser

setup(
    name = 'amzbkparser',
    version=amzbkparser.__version__,
    description = 'Amazon Book Parser',
    long_description=open('README.md').read(),
    author='Feng Zhu',
    author_email='fengzhu@usc.edu',
    url = 'https://github.com/lyricorpse/AmzBookParser',
    license='BSD',
    py_modules = ['amzbkparser'],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Programming Language :: Python :: 3'
    ]
)

