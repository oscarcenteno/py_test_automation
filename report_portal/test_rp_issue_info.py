import pytest


@pytest.mark.issue(issue_id="111111", reason="Some bug", issue_type="PB")
@pytest.mark.rp
def test():
    assert False