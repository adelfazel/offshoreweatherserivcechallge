from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="weather_data_converter",
    version="0.0.1",
    author="Adel Fazel",
    author_email="adel.fazel86@gamil.com",
    description="programming challenge by ows",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/adelfazel/offshoreweatherserivcechallge",
    packages=find_packages(),
    python_requires='>=3.8',
)