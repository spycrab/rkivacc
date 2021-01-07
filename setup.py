import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rkivacc",
    version="1.0.0",
    author="spycrab0",
    author_email="spycrab@users.noreply.github.com",
    description="A simple python library for pulling vaccination data from the RKI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/spycrab/rkivacc",
    packages=setuptools.find_packages(),
    install_requires=[
        "requests",
        "openpyxl"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.6"
)