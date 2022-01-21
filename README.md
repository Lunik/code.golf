# code.golf

[![Tests](https://github.com/Lunik/code.golf/actions/workflows/tests.yml/badge.svg)](https://github.com/Lunik/code.golf/actions/workflows/tests.yml)

[Tests & performance report](https://lunik.github.io/code.golf/)

[Challenge source](https://code.golf/)

## Setup

```shell
make install
```


## Solutions

Solution algorithm can be found in [solutions](./solutions) folder.

Execute solution and profiler :
```shell
PYTHONPATH=".:$PYTHONPATH" ./venv/bin/python3 solutions/challenge_XXXX.py
```


## Test

```shell
make test
```

### lint

```shell
make lint
```
