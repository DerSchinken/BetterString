from setuptools import setup, find_packages

# Get Long Description
with open("README.md", "r") as readme:
    long_description = readme.read().replace("Â", "")
# Get requirements.txt
with open("requirements.txt", "r") as requirements:
    reqs = requirements.read().splitlines()

setup(
    name="BetterString",
    version="2.17.0",
    # Major version 2
    # Minor version 17
    # Maintenance version 0

    author="DerSchinken",
    description="Like a normal string but with more functionality",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=reqs,
    python_requires=">=3.6",
    project_urls={
        "Homepage": "http://index12.bplaced.net/",
        "Github": "https://github.com/DerSchinken/PasswordCardGenerator",
    },
    keyword=[
        "Better String",
        "String", "str",
        "BetterString",
    ],
    classifiers=[
        'Intended Audience :: Developers',

        'Operating System :: OS Independent',

        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        "Programming Language :: Python :: 3.10"
    ],
)
#  https://DerSchinken.GitHub.io/BetterString/
