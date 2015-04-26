from setuptools import setup


setup(
    name="pygun",
    version="0.1",
    description="Simple python module for communicating with Mailgun API.",
    license="New BSD License",
    author="Pavel Hrdina",
    author_email="hrdina.pavel@gmail.com",
    url="https://github.com/grafa/pygun",
    keywords="mailgun",
    packages=["pygun"],
    requires=["requests"],
)
