rem Create the Package
python setup.py sdist bdist_wheel

rem Upload it to PyPI
twine upload dist/*

rem Cleanup
rmdir /Q /S BetterString.egg-info\
rmdir /Q /S build\
rmdir /Q /S dist\
