from .task import Task


def test_bad_title_check():
    task = Task()
    settings = {"regex": "fix: .*"}
    assert task._execute({"pull_request": {"title": " bad bug"}}, settings) is False


def test_good_title_check():
    task = Task()
    settings = {"regex": "fix: .*"}
    assert task._execute({"pull_request": {"title": "fix: bad bug"}}, settings) is True


def test_no_settings():
    task = Task()

    assert task._execute({}, None) is False


def test_malformed_body():
    task = Task()

    settings = {"regex": "fix: .*"}

    assert task._execute({}, settings) is False
