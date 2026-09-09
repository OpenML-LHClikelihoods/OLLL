clean:
	yes | rm -rf build_dist dist olll.egg-info

pypi: clean
	python -m pip install build
	rm -rf dist
	python -m build .
	twine check --strict dist/*
	twine upload dist/olll-*.tar.gz

testpypi: clean
	python -m pip install build
	rm -rf dist
	python -m build .
	twine check --strict dist/*
	twine upload -r pypitest dist/olll-*.tar.gz

clean:
	rm -rf build dist oll.egg*
