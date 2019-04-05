import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='Darko',
    version='0.1',
    scripts=['Darko/run.py'],
    author="Utkucan Bıyıklı",
    author_email="utkucanbykl@gmail.com",
    description="Darko is lightweight Graph Key-Value store",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/UtkucanBykl/Darko",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
