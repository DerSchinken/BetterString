from setuptools import setup, find_packages

# Get Long Description
with open("README.md", "r") as readme:
    long_description = readme.read().replace("Â", "")
# Get requirements.txt
# with open("requirements.txt", "r") as requirements:
#    reqs = requirements.read().splitlines()

setup(
    name="BetterString",
    version="2.16.9",
    # Major version 2
    # Minor version 16
    # Maintenance version 8

    author="DerSchinken",
    description="Like a normal string but with more functionality",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    # install_requires=reqs,
    python_requires=">=3.6",
    url="https://GitHub.com/DerSchinken/BetterString",
    keyword=[
        "Better String",
        "String",
        "BetterString",
    ],
    classifiers=[
        'Intended Audience :: Developers',

        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        "Programming Language :: Python :: 3.10"
    ],
)
#  https://DerSchinken.GitHub.io/BetterString/
