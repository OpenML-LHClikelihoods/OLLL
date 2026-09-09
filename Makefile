pypi: clean
	python -m pip install build
	rm -rf dist
	python -m build .
	twine check --strict dist/*
	twine upload dist/oll-*.tar.gz

testpypi: clean
	python -m pip install build
	rm -rf dist
	python -m build .
	twine check --strict dist/*
	twine upload -r pypitest dist/oll-*.tar.gz

clean:
	rm -rf build dist oll.egg*
