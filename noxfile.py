import nox

nox.options.default_venv_backend = "uv"


@nox.session(python=["3.11"], tags=["test"])
def tests(session):
    session.install("pytest")
    session.install("-e", ".")
    session.run("pytest")


@nox.session(tags=["style"])
def lint(session):
    session.install("ruff")
    session.run("ruff", "check", ".")
    session.run("ruff", "format", ".")


@nox.session(python=["3.11"], tags=["style"])
def typecheck(session):
    session.install("mypy")
    session.run("mypy", "src")
