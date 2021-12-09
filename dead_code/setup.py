from setuptools import setup
setup(
    name="pynt-contrib",
    version= "0.2.0",
    author="Raghunandan Rao",
    author_email="r.raghunandan@gmail.com",
    url= "http://rags.github.com/pynt-contrib/", 
    packages=["pyntcontrib"],
    license="MIT License",
    description="Common pynt tasks.",
    long_description=open("README.rst").read()+"\n"+open("CHANGES.rst").read(),
    install_requires = ['pynt>=0.8.1']
)
