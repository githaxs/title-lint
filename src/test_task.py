from .task import Task


def test_bad_title_check():
    task = Task({})
    task.settings = {"regex": "fix: .*"}
    assert task._execute({"pull_request": {"title": " bad bug"}}) is False


def test_good_title_check():
    task = Task({})
    task.settings = {"regex": "fix: .*"}
    assert task._execute({"pull_request": {"title": "fix: bad bug"}}) is True


def test_no_settings():
    task = Task({})

    assert task._execute({}) is False


def test_malformed_body():
    task = Task({})

    task.settings = {"regex": "fix: .*"}

    assert task._execute({}) is False
