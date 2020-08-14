import re

class Task():
    def __init__(self, raw_event, task_settings, github):
        self.raw_event = raw_event
        self.task_settings = task_settings
        self.github = github

    def run(self):
        check_regex = re.compile(self.task_settings.get('regex'))
        
        result = check_regex.search(self.raw_event.get('pull_request').get('title'))


        if not result:
            return {
                "result": False,
                "message": "Pull Request Title must match regex: `%s`" % self.task_settings.get('regex')
            }

        return { "result": True }
