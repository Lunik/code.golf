PY       ?= python3
VENV_PY  ?= venv/bin/python3
PYLINT   ?= venv/bin/pylint
PYTEST   ?= venv/bin/pytest

VENV         ?= venv
REQUIREMENTS  = requirements.txt
_PYTHONPATH    = .

PROJECT_NAME = code.golf
HTML_STATIC_PATH = static
HTML_REPORT_PATH = docs

PYLINT_OPTS = --extension-pkg-allow-list="math"
PYTEST_OPTS = --durations=0 -v -n 4 --color=yes

install: env
	${VENV_PY} -m pip install -r "${REQUIREMENTS}"

env:
	${PY} -m venv "${VENV}"

all: test render lint

lint:
	PYTHONPATH="${_PYTHONPATH}:${PYTHONPATH}" ${PYLINT} ${PYLINT_OPTS} solutions/

test:
	PYTHONPATH="${_PYTHONPATH}:${PYTHONPATH}" ${PYTEST} ${PYTEST_OPTS} --html="${HTML_REPORT_PATH}/index.html" tests/
