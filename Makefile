.PHONY: clean clean-build clean-pyc clean-test coverage dist docs help install lint lint/flake8 test

.DEFAULT_GOAL := help

define BROWSER_PYSCRIPT
import os, webbrowser, sys

from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-build clean-pyc clean-test clean-assets clean-npm ## remove all build, test, coverage, Python and npm artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

clean-assets: ## remove copied assets from src/daksh/
	rm -rf src/daksh/assets

lint/flake8: ## check style with flake8
	flake8 daksh tests


lint: lint/flake8 ## check style

test: ## run tests quickly with the default Python
	pytest tests

test-all: ## run tests on every Python version with tox
	tox

coverage: ## check code coverage quickly with the default Python
	coverage run --source daksh -m pytest
	coverage report -m
	coverage html
	$(BROWSER) htmlcov/index.html

publish-python: dist ## package and upload a release
	twine upload --repository divami dist/*

publish-npm: npm-pack ## package and upload npm release
	npm publish

publish: sync-version dist npm-pack ## package and upload to both Python and npm registries
	@echo "🚀 Publishing to Python registry..."
	twine upload --repository divami dist/*
	@echo "🚀 Publishing to npm registry..."
	npm publish
	@echo "✅ Published to both registries successfully!"

dist: clean ## builds source and wheel package
	python scripts/build_prep.py
	python -m build
	ls -l dist

npm-pack: clean-npm ## builds npm package
	@echo "📦 Building npm package..."
	npm pack
	@echo "✅ npm package built successfully"
	ls -l *.tgz

npm-test: npm-pack ## test the npm package locally
	@echo "🧪 Testing npm package locally..."
	npm install -g ./daksh-ai-*.tgz
	@echo "Testing CLI command..."
	daksh --help
	@echo "✅ npm package test completed"

sync-version: ## sync npm version with Python version
	@echo "🔄 Syncing package versions..."
	@PYTHON_VERSION=$$(grep '^version = ' pyproject.toml | sed 's/version = "\(.*\)"/\1/'); \
	echo "Python version: $$PYTHON_VERSION"; \
	npm version $$PYTHON_VERSION --no-git-tag-version; \
	echo "✅ Versions synchronized"

clean-npm: ## remove npm artifacts
	rm -f *.tgz
	rm -rf node_modules

install: clean ## install the package to the active Python's site-packages
	python setup.py install

docs:
	mkdocs build

serve-docs: docs ## serve the documentation with mkdocs
	mkdocs serve

export:
	nbdev_exportpreview:
	mkdocs serve

build-docs:
	mkdocs build