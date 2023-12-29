venv:
	python3 -m venv venv
	source venv/bin/activate ; pip install --upgrade pip ; python3 -m pip install -r requirements-dev.txt
	source venv/bin/activate ; pip freeze > requirements_freeze.txt

clean:
	rm -rf venv

run:
	source venv/bin/activate ; PYTHONPATH='./src' python -m app reqarg1

jupyter:
	source venv/bin/activate; PYTHONPATH='./src' jupyter lab

black-check:
	source venv/bin/activate ; black src --check --verbose --line-length 120

black:
	source venv/bin/activate ; black src --line-length 120

ruff-check:
	source venv/bin/activate ; ruff check .

ruff:
	source venv/bin/activate ; ruff check . --fix

test:
	source venv/bin/activate ; PYTHONPATH='./src' pytest -vv --capture=no tests

.DEFAULT_GOAL := help
.PHONY: help
help:
	@LC_ALL=C $(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'
