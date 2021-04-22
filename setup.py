from setuptools import setup, find_packages

# Get Long Description
with open("README.md", "r") as readme:
    long_description = readme.read().replace("Â", "")

setup(
    name="BetterString",
    version="2.9.5",
    # Major version 2
    # Minor version 9
    # Maintenance version 5

    author="DerSchinken (aka DrBumm)",
    description="Like a normal string but with more functionality",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires=">=3.6",
    url="https://github.com/DrBumm/BetterString",
    keyword=[
        "Better String",
        "String",
        "BetterString",
    ],
    classifiers=[
        'Intended Audience :: Developers',

        "Programming Language :: Python :: 3.6",
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
#  https://drbumm.github.io/BetterString/
