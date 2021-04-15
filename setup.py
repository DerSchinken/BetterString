from setuptools import setup, find_packages

# Get Long Description
with open("README.md", "r") as readme:
    long_description = readme.read()

setup(
    name="BetterString",
    version="2.5.0",
    # Major version 2
    # Minor version 5
    # Maintenance version 0

    author="DerSchinken (aka DrBumm)",
    description="Like a normal string but with more functionality",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires=">=3",
)
