from nox import Session, options
from nox_uv import session

options.default_venv_backend = "uv"
options.pythons = ["3.14"]


@session(uv_only_groups=["lint"])
def lint(session: Session):
    session.run("ruff", "check", "--fix")
    session.run("ruff", "format")


@session(uv_groups=["test"])
def test(session: Session):
    session.run("pytest")


@session(uv_groups=["typing"])
def test(session: Session):
    session.run("ty", "check")
