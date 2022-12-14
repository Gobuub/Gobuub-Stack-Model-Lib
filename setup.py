from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    readme = f.read()

setup(
    name="Gobuubstackmodel",
    version="0.7",
    description="Personal Python lib for used on EDA's and train ML models",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Enrique Revuelta Garcia",
    author_email="enrique.revuelta@enriquerevueltagarcia.com",
    url="https://github.com/Gobuub/Gobuub-Stack-Model-Lib",
    packages=find_packages(),
    classifiers=[
         "Programming Language :: Python :: 3.9",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
    scripts=[]
)
