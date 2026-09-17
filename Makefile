clean: .PHONY
	yes | rm -rf build_dist dist hep_olll.egg-info/

pypi: clean
	python -m pip install build
	rm -rf dist
	python -m build .
	twine check --strict dist/*
	twine upload dist/hep_olll*.tar.gz

testpypi: clean
	python -m pip install build
	rm -rf dist
	python -m build .
	twine check --strict dist/*
	twine upload -r pypitest dist/hep_olll*.tar.gz

.PHONY:
