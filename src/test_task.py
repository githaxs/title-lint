from .task import Task


def test_bad_title_check():
    task = Task()
    settings = {"regex": "fix: .*"}
    assert task.execute(
        {"pull_request": {"title": " bad bug"}}, settings) is False


def test_good_title_check():
    task = Task()
    settings = {"regex": "fix: .*"}
    assert task.execute(
        {"pull_request": {"title": "fix: bad bug"}}, settings) is True


def test_no_settings():
    task = Task()

    assert task.execute({}, None) is False


def test_malformed_body():
    task = Task()

    settings = {"regex": "fix: .*"}

    assert task.execute({}, settings) is False


def test_regex_shorthands():
    task = Task()
    settings = {"regex": "\\w+-\\d+"}

    assert task.execute(
        {"pull_request": {"title": "fix: bad bug (OPS-000)"}}, settings) is True
    assert task.execute({"pull_request": {
                        "title": "feat: upgrade to latest githaxs(OPS)"}}, settings) is False


def test_exclude_users():
    task = Task()
    settings = {"regex": "fix: .*", "exclude_users": "dependabot,bar"}
    github_body = {
        "pull_request": {"title": "fix deps", "user": {"login": "dependabot"}}
    }

    assert task.execute(github_body=github_body, settings=settings) is True
