from glob import glob

import nox


PY_FILES = glob("**/*.py", recursive=True)
IPYNB_FILES = glob("**/*.ipynb", recursive=True)


@nox.session
def flake8(session):
    """Lint code with Flake8."""
    session.install("flake8")
    session.run("flake8", *PY_FILES)


@nox.session
def black(session):
    """Check code formatting with black."""
    session.install("black==18.9b0")
    if session.posargs:
        session.run("black", *session.posargs)
    else:
        session.run("black", "--check", "--line-length", "79", *PY_FILES)


@nox.session
def black_nb(session):
    """Check code formatting in notebooks with black."""
    session.install("black-nb")
    if session.posargs:
        session.run("black-nb", *session.posargs)
    else:
        session.run("black-nb", "--check", "--clear-output", *IPYNB_FILES)
