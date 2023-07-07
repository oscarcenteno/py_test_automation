# py_test_automation

This repo contains a web and api test automation framework in Python, including configuration for use within vscode.

It also allows for integration to a ReportPortal instance (assuming you have a ReportPortal project already configured).

## Installation

https://note.nkmk.me/en/python-pip-install-requirements/

```bash
pip install -r requirements.txt
```

## Testing

```bash
pytest -v -m web
pytest -v -m api
pytest -v -m unit
```

## Report Portal

https://github.com/reportportal/agent-python-pytest

To run tests with Report Portal you must provide '--reportportal' flag:

```bash
$ pytest -c report_portal.cfg
pytest -c report_portal.cfg -v -m api --reportportal 
```

See report_portal.cmd.
