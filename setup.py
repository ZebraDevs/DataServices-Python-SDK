import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Savanna-Python-SDK",
    version="1.0.0",
    author="Declan Buhrsmith",
    author_email="dbuhrsmith@zebra.com",
    description="This is the source code for the Savanna Python Software Development Kit (SDK).",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Zebra/Savanna-Python-SDK",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)