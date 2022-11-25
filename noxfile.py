import nox

source_dirs = ["rcon", "rconweb", "tests"]


@nox.session
def install(session):
    session.install("-r", "requirements.txt")
    session.install("-r", "requirements-dev.txt")


@nox.session(tags=["style"])
def black(session):
    session.run("black", *source_dirs)


@nox.session(tags=["isort"])
def isort(session):
    session.run("isort", *source_dirs)
