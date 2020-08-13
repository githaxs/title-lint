import re

class Task():
    def __init__(self, raw_event, task_settings, github):
        self.raw_event = raw_event
        self.task_settings = task_settings
        self.github = github

    def run(self):
        check_regex = re.compile(self.task_settings.get('regex'))
        
        return check_regex.match(self.raw_event.get('pull_request').get('title'))
