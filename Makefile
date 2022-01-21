PY       ?= python3
VENV_PY  ?= venv/bin/python3
PYTEST   ?= venv/bin/pytest

VENV         ?= venv
REQUIREMENTS  = requirements.txt
_PYTHONPATH    = .

PROJECT_NAME = code.golf
HTML_STATIC_PATH = static
HTML_REPORT_PATH = docs

PYTEST_OPTS = --durations=0 -v -n 4 --color=yes

install: env
	${VENV_PY} -m pip install -r "${REQUIREMENTS}"

env:
	${PY} -m venv "${VENV}"

all: test render

test:
	PYTHONPATH="${_PYTHONPATH}:${PYTHONPATH}" ${PYTEST} ${PYTEST_OPTS} --html="${HTML_REPORT_PATH}/index.html" tests/

new:
	test -n ${name} \
	&& echo ${name} \
	&& cp -r solutions/skeleton solutions/${name} \
	&& cp -r tests/solutions/skeleton tests/solutions/${name}