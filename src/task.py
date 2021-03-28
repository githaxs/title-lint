import re

from base_task import BaseTask


class Task(BaseTask):
    """
    Verifies the Title of a Pull Request matches a provided regex.
    """

    def _execute(self, github_body) -> bool:
        if self.settings is None or self.settings.get("regex") is None:
            return False

        self.regex = self.settings["regex"]
        check_regex = re.compile(self.regex)

        return bool(
            check_regex.search(github_body.get("pull_request", {}).get("title", ""))
        )

    def _requested_action(self):
        pass

    def _get_task_name(self):
        return "Title Lint"

    def _get_task_slug(self) -> str:
        return "title-lint"

    def _get_fail_summary(self) -> str:
        return "Pull Request Title must match regex: %s" % self.regex

    def _get_fail_text(self) -> str:
        return ""

    def _get_pass_summary(self) -> str:
        return ":+1:"

    def _get_pass_text(self) -> str:
        return ""

    def _get_actions(self):
        return None
