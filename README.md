# Title Lint

The Title Lint task checks Pull Request titles conform to a standard regular expression.

You may want to use this application if you:

* Follow conventional commit
* Use Jira to link pull requests to Jira ticket
* Prefer to have all Pull Request titles use the similar format

### Installation
1. Install the [Githaxs Meta Application](https://github.com/apps/githaxs-meta)

2. Create a repo with the name `githaxs_settings`.

3. Add the following to `ghx.yml` within the repo:

```yaml
# githaxs_settings/ghx.yml

title-lint:
  # install on all repos
  org: true
  # install on select repos
  repos:
    - api-microservice
    - websiteservice
  # install on repos with a given topic
  repo_topics:
    - api
    - web
```

### Configuration

|parameter|description|required|
|---|---|---|
|regex| The regular expression to test Pull Request titles agains| yes


### Example Configurations

To configure global settings:

```yaml
# githaxs_settings/ghx.yml

title-lint:
  org: true
  org_settings:
    # Cannot be overriden by repo specific settings
    final:
      regex: "[A-Z]+-[0-9]+"
    # Default value if repo specific settings do not exist
    default:
      regex: "[A-Z]+-[0-9]+"
```

To configure repo specific settings:
```yaml
# <repo name>/ghx.yml

title-lint:
  repo_settings:
    regex: "fix|feat: .*"
```
