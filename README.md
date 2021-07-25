# nome

A Python CLI to check if a package name is available in PyPI or npm.

## References

- Ewen Le Bihan's [check_availability](https://github.com/ewen-lbh/check-availability) CLI.
- Anton Zhiyanov's [How to make an awesome Python package in 2021](https://antonz.org/python-packaging/) blog post ([repo](https://github.com/nalgeon/podsearch-py)).
- [Development - Contributing](https://fastapi.tiangolo.com/contributing/) page (FastAPI documentation).

## Development

Current version of Python used for development: `Python 3.6.13`.

- `python -m venv env`.
- `source ./env/bin/activate`.
  - Run `which pip` to see if it worked. The path must end in `env/bin/pip`.
  - **Note**: Whenever you install a new package with `pip` in this environment, activate it again.

## Notes

- [Why isn't my desired project name available?](https://pypi.org/help/#project-name):
  - `requirements.txt` is a prohibited project name.
- [stdlib-list](https://github.com/jackmaney/python-stdlib-list) package.
- [Python (3.6) Module Index](https://docs.python.org/3.6/py-modindex.html).
- [Flit](https://flit.readthedocs.io/en/latest/):
  - Python packaging tool.
  - [FastAPI](https://github.com/tiangolo/fastapi) uses it.
- [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/).
- `python -m venv env` or `python3 -m venv env` (virtual environment with `venv`).
