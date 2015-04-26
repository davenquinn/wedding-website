from setuptools import setup, find_packages

setup(
    name="wedding-website",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        'Flask',
        'Flask-Mail',
        'Flask-WTF',
        'WTForms',
        'pathlib'
    ]
)
