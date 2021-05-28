import re

from task_interfaces import MetaTaskInterface
from task_interfaces import SubscriptionLevels


class Task(MetaTaskInterface):
    """
    Verifies the Title of a Pull Request matches a provided regex.
    """

    name = "Title Lint"
    slug = "title-lint"
    pass_summary = "Your Pull Request Title passes the check."
    pass_text = ""
    fail_text = ""
    actions = None
    subscription_level = SubscriptionLevels.FREE

    def execute(self, github_body, settings) -> bool:
        if settings is None or settings.get("regex") is None:
            self.fail_message = "Could not find valid settings for Title Lint. Please refer to the [documentation](https://github.com/githaxs/title-lint#installation) and ensure you have configured it correctly."
            return False

        originator = github_body.get("pull_request", {}).get("user", {}).get("login")

        if originator in settings.get("exclude_users", []):
            return True

        self.regex = settings["regex"]
        check_regex = re.compile(self.regex)

        return bool(
            check_regex.search(github_body.get("pull_request", {}).get("title", ""))
        )

    @property
    def fail_summary(self) -> str:
        return "Pull Request Title must match regex: %s" % self.regex
