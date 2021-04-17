from setuptools import setup, find_packages

# Get Long Description
with open("README.md", "r") as readme:
    long_description = readme.read()

setup(
    name="BetterString",
    version="2.7.8",
    # Major version 2
    # Minor version 7
    # Maintenance version 8

    author="DerSchinken (aka DrBumm)",
    description="Like a normal string but with more functionality",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires=">=3.8",
    url="https://github.com/DrBumm/BetterString",
    keyword=[
        "Better String",
        "String",
    ],
    classifiers=[
        'Intended Audience :: Developers',

        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
