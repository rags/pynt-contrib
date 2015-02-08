from setuptools import setup
from pynt import contrib
setup(
    name="pynt-contrib",
    version= contrib.__version__,
    author="Raghunandan Rao",
    author_email="r.raghunandan@gmail.com",
    url= contrib.__contact__, 
    packages=["pynt.contrib"],
    license="MIT License",
    description="Common pynt tasks.",
    long_description=open("README.rst").read()+"\n"+open("CHANGES.rst").read()
)
